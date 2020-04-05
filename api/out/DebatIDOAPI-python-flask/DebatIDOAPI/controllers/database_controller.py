import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.quote import Quote  # noqa: E501
from DebatIDOAPI.models.quote_link import QuoteLink  # noqa: E501
from DebatIDOAPI.models.theme import Theme  # noqa: E501
from DebatIDOAPI.models.reference import Reference  # noqa: E501
from DebatIDOAPI.models.protagonist import Protagonist  # noqa: E501
from DebatIDOAPI.models.person import Person  # noqa: E501
from DebatIDOAPI.models.company import Company  # noqa: E501
from DebatIDOAPI import util

from typing import List, Dict  # noqa: F401

from flask import current_app
import inspect

import os
from sqlalchemy.engine.url import make_url
import mysql.connector

url = make_url(os.getenv('DATABASE_URL'))
mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)

classNames = {
    "quote" : Quote,
    "reference" : Reference
}

classSQLRequests = {
    Quote : {
        "List" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id;",
        "ID" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id WHERE q.id = ",
        "DELETE" : "DELETE FROM quote q WHERE q.id = ",
        "quoteMains" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID JOIN quoteLink ql ON ql.quoteMainID = q.id WHERE ql.quoteSupportID = ",
        "quoteSupports" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID JOIN quoteLink ql ON ql.quoteSupportID = q.id WHERE ql.quoteMainID = ",
    },
    QuoteLink : {
        "quoteMains" : "SELECT ql.quoteMainID, ql.quoteSupportID, ql.typeID, qlt.title as typeTitle, ql.dateUpdate FROM quoteLink ql JOIN quoteLinkType qlt ON ql.typeID = qlt.id WHERE ql.quoteSupportID = ",
        "quoteSupports" : "SELECT ql.quoteMainID, ql.quoteSupportID, ql.typeID, qlt.title as typeTitle, ql.dateUpdate FROM quoteLink ql JOIN quoteLinkType qlt ON ql.typeID = qlt.id WHERE ql.quoteMainID = ",
    },
    Reference : {
        "List" : "SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title as typeTitle, r.reliability, r.dateUpdate FROM reference r JOIN referenceType rt ON r.typeID = rt.id;",
        "ID" : "SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title as typeTitle, r.reliability, r.dateUpdate FROM reference r JOIN referenceType rt ON r.typeID = rt.id WHERE r.id =",
        "DELETE" : "DELETE FROM reference r WHERE r.id = ",
        Quote : "SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title, r.reliability, r.dateUpdate FROM reference r JOIN quoteReference qr ON r.id = qr.referenceID JOIN referenceType rt ON r.typeID = rt.id WHERE qr.quoteID = "
    },
    Theme : {
        "List" : "SELECT t.id, t.title FROM theme t;",
        "ID" : "SELECT t.id, t.title FROM theme t WHERE t.id = ",
        "DELETE" : "DELETE FROM theme t WHERE t.id = ",
        Quote : "SELECT t.id, t.title FROM theme t JOIN quoteTheme qt ON t.id = qt.themeID WHERE qt.quoteID = "
    },
    Protagonist : {
        "List" : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p;",
        "ID" : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p WHERE p.id = ",
        "DELETE" : "DELETE FROM protagonist pr WHERE pr.id = ",
        Quote : "SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM protagonist pr JOIN person pe ON pr.id = pe.id JOIN quoteAuthor qa ON qa.authorID = ",
        Reference : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p JOIN referenceAuthor ra ON p.id = ra.authorID JOIN reference r ON r.id = ra.referenceID WHERE r.id = "
    },
    Person : {
        "List" : "",
        "ID" : "SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM person pe WHERE pe.id = ",
        "DELETE" : "DELETE FROM person p WHERE p.id = ",
        Protagonist : "SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM protagonist pr JOIN person pe ON pr.id = pe.id WHERE pr.id = "
    },
    Company : {
        "List" : "",
        "ID" : "SELECT c.id, c.siret, c.dateUpdate FROM company c WHERE c.id = ",
        "DELETE" : "DELETE FROM company c WHERE c.id = ",
        Protagonist : "SELECT c.id, c.siret, c.dateUpdate FROM protagonist pr JOIN company c ON pr.id = c.id WHERE pr.id = "
    }
}

class Database:

    @classmethod
    def getOtherClassParameters(cls, classMyObject):
        dictSubClasses = {}
        for objectName, subClassObject in classMyObject.openapi_types.items():
            if type(subClassObject) is type(List):
                dictSubClasses[objectName] = subClassObject.__args__[0]
        return dictSubClasses

    @classmethod
    #TODO
    def patchObjectFromID(cls, myPatchObject, id):
        if (id == myPatchObject.id):
            dictSubClasses = Database.getOtherClassParameters(myPatchObject)
            for objectName, subClassObject in dictSubClasses.items():
                parameter = myObject.attribute_map[objectName]
                test = getattr(myPatchObject, parameter)
                current_app.logger.debug(parameter)
                current_app.logger.debug(test)
        else:
            current_app.logger.debug("Not same id")

    @classmethod
    def deleteObjectFromID(cls, classMyObject, id):
        valueReturn = 0
        if ("DELETE" in classSQLRequests[classMyObject]):
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["DELETE"]+str(id)+";")
            mydb.commit()
            valueReturn = cur.rowcount
        return valueReturn

    @classmethod
    def getObjectFromID(cls, classMyObject, id):
        myObject = None
        if ("ID" in classSQLRequests[classMyObject]):
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["ID"]+str(id)+";")
            for row in cur.fetchall() :
                myObject = classMyObject.from_dict(row)
        return myObject

    @classmethod
    def getObjectFromIDWithDetailsFromOtherClassParameters(cls, classMyObject, id):
        myObject = Database.getObjectFromID(classMyObject,id)
        Database.getDetailsFromOtherClassParameters(myObject)
        return myObject


    @classmethod
    def getList(cls, classMyObject):
        list = []
        if ("List" in classSQLRequests[classMyObject]):
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["List"])
            for row in cur.fetchall() :
                list.append(classMyObject.from_dict(row))
        return list

    @classmethod
    def getListWithDetailsFromOtherClassParameters(cls, classMyObject):
        list = Database.getList(classMyObject)
        for l in list :
            Database.getDetailsFromOtherClassParameters(l)
        return list



    @classmethod
    def getListFromOtherID(cls, classMyObject, classConstraintID, id):
        list = []
        if (classConstraintID in classSQLRequests[classMyObject]):
            cur = mydb.cursor(dictionary=True)
            current_app.logger.debug(classSQLRequests[classMyObject][classConstraintID]+str(id)+";")
            cur.execute(classSQLRequests[classMyObject][classConstraintID]+str(id)+";")
            for row in cur.fetchall() :
                list.append(classMyObject.from_dict(row))
        return list

    @classmethod
    def getListFromOtherIDWithDetailsFromOtherClassParameters(cls, classMyObject, classConstraintID, id):
        list = Database.getListFromOtherID(classMyObject, classConstraintID, id)
        for l in list :
            Database.getDetailsFromOtherClassParameters(l)
        return list

    @classmethod
    def getObjectFromOtherID(cls, classMyObject, classConstraintID, id):
        myObject = None
        if (classConstraintID in classSQLRequests[classMyObject]):
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject][classConstraintID]+str(id)+";")
            for row in cur.fetchall() :
                myObject = classMyObject.from_dict(row)
        return myObject

    @classmethod
    def getDetailsFromOtherClassParameters(cls, myObject):
        if myObject is not None:
            if (type(myObject) is Protagonist):
                if (myObject.type == "person"):
                    myObject.person = Database.getObjectFromOtherID(Person,Protagonist,myObject.id)
                elif (myObject.type == "person"):
                    myObject.company = Database.getObjectFromOtherID(Company,Protagonist,myObject.id)
            elif (type(myObject) is QuoteLink):
                myObject.quote_main = Database.getObjectFromID(Quote,myObject.quote_main_id)
                myObject.quote_support = Database.getObjectFromID(Quote,myObject.quote_support_id)
            elif (type(myObject) is Quote):
                dictSubClasses = Database.getOtherClassParameters(myObject)
                for objectName, subClassObject in dictSubClasses.items():
                    parameter = myObject.attribute_map[objectName]
                    if parameter == "quoteMains" or parameter == "quoteSupports":
                        setattr(myObject, objectName, Database.getListFromOtherID(subClassObject,parameter,myObject.id))
                    else:
                        setattr(myObject, objectName, Database.getListFromOtherID(subClassObject,type(myObject),myObject.id))
            else:
                dictSubClasses = Database.getOtherClassParameters(myObject)
                for objectName, subClassObject in dictSubClasses.items():
                    setattr(myObject, objectName, Database.getListFromOtherID(subClassObject,type(myObject),myObject.id))

        return myObject
