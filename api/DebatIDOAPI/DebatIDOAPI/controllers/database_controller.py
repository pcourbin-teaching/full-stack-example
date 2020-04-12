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
from DebatIDOAPI.controllers.security_controller_ import TOKEN_DB

from typing import List, Dict  # noqa: F401

from flask import current_app
import inspect

import os
from sqlalchemy.engine.url import make_url
import mysql.connector

url = make_url(os.getenv('DATABASE_URL'))
#mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)

classNames = {
    "quote" : Quote,
    "reference" : Reference
}

classSQLRequests = {
    Quote : {
        "List" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id;",
        "ID" : {
            Quote : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id WHERE q.id = ",
        },
        "INSERT" : {
            Protagonist: "INSERT INTO quoteAuthor (quoteID, authorID) VALUES ({}, {})",
            Theme: "INSERT INTO quoteTheme (quoteID, themeID) VALUES ({}, {})",
            Reference: "INSERT INTO quoteReference (quoteID, referenceID) VALUES ({}, {})",
        },
        "DELETE" : "DELETE FROM quote q WHERE q.id = ",
        "quoteMains" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID JOIN quoteLink ql ON ql.quoteMainID = q.id WHERE ql.quoteSupportID = ",
        "quoteSupports" : "SELECT q.id, q.title, q.details, q.typeID, qt.title as typeTitle, q.dateUpdate FROM quote q JOIN quoteType qt ON q.typeID JOIN quoteLink ql ON ql.quoteSupportID = q.id WHERE ql.quoteMainID = ",
        "DBTable" : "quote",
    },
    QuoteLink : {
        "quoteMains" : "SELECT ql.quoteMainID, ql.quoteSupportID, ql.typeID, qlt.title as typeTitle, ql.dateUpdate FROM quoteLink ql JOIN quoteLinkType qlt ON ql.typeID = qlt.id WHERE ql.quoteSupportID = ",
        "quoteSupports" : "SELECT ql.quoteMainID, ql.quoteSupportID, ql.typeID, qlt.title as typeTitle, ql.dateUpdate FROM quoteLink ql JOIN quoteLinkType qlt ON ql.typeID = qlt.id WHERE ql.quoteMainID = ",
        "DBTable" : "quoteLink"
    },
    Reference : {
        "List" : "SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title as typeTitle, r.reliability, r.dateUpdate FROM reference r JOIN referenceType rt ON r.typeID = rt.id;",
        "ID" : {
            Reference : "SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title as typeTitle, r.reliability, r.dateUpdate FROM reference r JOIN referenceType rt ON r.typeID = rt.id WHERE r.id =",
            Quote : "SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title, r.reliability, r.dateUpdate FROM reference r JOIN quoteReference qr ON r.id = qr.referenceID JOIN referenceType rt ON r.typeID = rt.id WHERE qr.quoteID = ",
        },
        "INSERT" : {
        },
        "DELETE" : "DELETE FROM reference r WHERE r.id = ",
        "DBTable" : "reference",
    },
    Theme : {
        "List" : "SELECT t.id, t.title FROM theme t;",
        "ID" : {
            Theme : "SELECT t.id, t.title FROM theme t WHERE t.id = ",
            Quote : "SELECT t.id, t.title FROM theme t JOIN quoteTheme qt ON t.id = qt.themeID WHERE qt.quoteID = ",
        },
        "INSERT" : {
        },
        "DELETE" : "DELETE FROM theme t WHERE t.id = ",
        "DBTable" : "theme",
    },
    Protagonist : {
        "List" : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p;",
        "ID" : {
            Protagonist : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p WHERE p.id = ",
            Quote : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p JOIN quoteAuthor qa ON p.id = qa.authorID JOIN quote q ON q.id = qa.quoteID WHERE q.id =  ",
            Reference : "SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p JOIN referenceAuthor ra ON p.id = ra.authorID JOIN reference r ON r.id = ra.referenceID WHERE r.id = "
        },
        "INSERT" : {
        },
        "DELETE" : "DELETE FROM protagonist pr WHERE pr.id = ",
        "DBTable" : "protagonist",
    },
    Person : {
        "List" : "",
        "ID" : {
            Person : "SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM person pe WHERE pe.id = ",
            Protagonist : "SELECT pe.id, pe.surname, pe.role, pe.dateUpdate FROM protagonist pr JOIN person pe ON pr.id = pe.id WHERE pr.id = ",
        },
        "INSERT" : {
        },
        "DELETE" : "DELETE FROM person p WHERE p.id = ",
        "DBTable" : "person",
    },
    Company : {
        "List" : "",
        "ID" : {
            Company : "SELECT c.id, c.siret, c.dateUpdate FROM company c WHERE c.id = ",
            Protagonist : "SELECT c.id, c.siret, c.dateUpdate FROM protagonist pr JOIN company c ON pr.id = c.id WHERE pr.id = ",
        },
        "INSERT" : {
        },
        "DELETE" : "DELETE FROM company c WHERE c.id = ",
        "DBTable" : "company",
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
    def insertPatch(cls, insertInto):

        valueReturn = 0
        errorReturn = ""
        codeReturn = 401

        try:
            mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
            cur = mydb.cursor(dictionary=True)
            cur.execute(insertInto)
            mydb.commit()
            valueReturn = cur.lastrowid
        except mysql.connector.Error as error:
            mydb.rollback()
            errorReturn = error
        finally:
            if (mydb.is_connected()):
                mydb.close()

        if ((cur.lastrowid == 0 and insertInto.startswith("INSERT")) or (cur.rowcount == 0 and insertInto.startswith("UPDATE"))):
            codeReturn = 424
        else :
            codeReturn = 201
        return valueReturn, errorReturn, codeReturn

    @classmethod
    def insertPatchOrGet(cls, myNewObject, insertInto):

        valueReturn, errorReturn, codeReturn = Database.insertPatch(insertInto)

        if ((insertInto.startswith("UPDATE") or codeReturn != 201) and myNewObject.id is not None):
            valueReturn = myNewObject.id

        returnObject = Database.getObjectFromIDWithDetailsFromOtherClassParameters(type(myNewObject),valueReturn)
        return returnObject, codeReturn

    @classmethod
    def postNewObject(cls, myNewObject):

        returnObject = None
        codeReturn = 401

        user = TOKEN_DB.get(connexion.request.headers['API_KEY'], None)
        if (user['sub'] == "root"):
            if (myNewObject is not None and "DBTable" in classSQLRequests[type(myNewObject)]):
                parametersValue = list()
                parametersDB = list()

                for parameterPython, parameterDB in myNewObject.attribute_map.items():
                    attribute = getattr(myNewObject, parameterPython)
                    if (attribute is not None and type(attribute) is not list and type(attribute) is not Person and type(attribute) is not Company):
                        parametersDB.append(parameterDB)
                        parametersValue.append(attribute)

                mySql_insert_query_start = "INSERT INTO "+classSQLRequests[type(myNewObject)]["DBTable"]+" ("
                mySql_insert_query_end = ") VALUES ("
                mysql_insert_query = mySql_insert_query_start + str(parametersDB).replace("[","").replace("]","").replace("'","") + mySql_insert_query_end + str(parametersValue).strip('[]') + ");"

                returnObject, codeReturn = Database.insertPatchOrGet(myNewObject,mysql_insert_query)
                if (codeReturn == 201):
                    for parameterPython, parameterDB in myNewObject.attribute_map.items():
                        attribute = getattr(myNewObject, parameterPython)
                        if (attribute is not None and type(attribute) is list):
                            for l in attribute:
                                returnObjectL, codeReturnL = Database.postNewObject(l)
                                if (returnObjectL is not None):
                                    Database.insertPatch(classSQLRequests[type(myNewObject)]["INSERT"][type(l)].format(returnObject.id, returnObjectL.id))
                        elif (type(attribute) is Person or type(attribute) is Company):
                            attribute.id = returnObject.id
                            Database.postNewObject(attribute)

                    returnObject = Database.getObjectFromIDWithDetailsFromOtherClassParameters(type(myNewObject),returnObject.id)
        return returnObject, codeReturn


    @classmethod
    def patchObject(cls, myPatchedObject, myPatchedObjectID):

        returnObject = None
        codeReturn = 401

        user = TOKEN_DB.get(connexion.request.headers['API_KEY'], None)
        if (user['sub'] == "root"):
            returnObject = Database.getObjectFromIDWithDetailsFromOtherClassParameters(type(myPatchedObject),myPatchedObjectID)
            if (returnObject is not None and (myPatchedObject.id is None or myPatchedObject.id == myPatchedObjectID) and "DBTable" in classSQLRequests[type(myPatchedObject)]):
                mysql_patch_query_middle = ""
                for parameterPython, parameterDB in myPatchedObject.attribute_map.items():
                    attribute = getattr(myPatchedObject, parameterPython)
                    if (attribute is not None and type(attribute) is not list and type(attribute) is not Person and type(attribute) is not Company):
                        if (len(mysql_patch_query_middle) > 0):
                            mysql_patch_query_middle = mysql_patch_query_middle + ","
                        if (type(attribute) is str):
                            mysql_patch_query_middle = mysql_patch_query_middle + str(parameterDB) + " = " + "'" + str(attribute) + "'"
                        else:
                            mysql_patch_query_middle = mysql_patch_query_middle + str(parameterDB) + " = " + str(attribute)


                mySql_patch_query_start = "UPDATE "+classSQLRequests[type(myPatchedObject)]["DBTable"]+" SET "
                mySql_patch_query_end = " WHERE id = "+str(myPatchedObjectID)+";"
                mysql_patch_query = mySql_patch_query_start + mysql_patch_query_middle + mySql_patch_query_end

                returnObject, codeReturn = Database.insertPatchOrGet(myPatchedObject,mysql_patch_query)
                if (codeReturn != 401):
                    for parameterPython, parameterDB in myPatchedObject.attribute_map.items():
                        attribute = getattr(myPatchedObject, parameterPython)
                        if (attribute is not None and type(attribute) is list):
                            for l in attribute:
                                returnObjectL, codeReturnL = Database.postNewObject(l)
                                if (returnObjectL is not None):
                                    Database.insertPatch(classSQLRequests[type(myPatchedObject)]["INSERT"][type(l)].format(returnObject.id, returnObjectL.id))
                        elif (type(attribute) is Person or type(attribute) is Company):
                            attribute.id = returnObject.id
                            Database.patchObject(attribute, attribute.id)
                    returnObject = Database.getObjectFromIDWithDetailsFromOtherClassParameters(type(myPatchedObject),returnObject.id)
        return returnObject, codeReturn

    @classmethod
    def deleteObjectFromID(cls, classMyObject, id):
        valueReturn = 0
        if ("DELETE" in classSQLRequests[classMyObject]):
            mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["DELETE"]+str(id)+";")
            mydb.commit()
            mydb.close()
            valueReturn = cur.rowcount
        return valueReturn

    @classmethod
    def getObjectFromIDWithDetailsFromOtherClassParameters(cls, classMyObject, id):
        myObject = Database.getObjectFromID(classMyObject,id)
        Database.getDetailsFromOtherClassParameters(myObject)
        return myObject


    @classmethod
    def getList(cls, classMyObject):
        list = []
        if ("List" in classSQLRequests[classMyObject]):
            mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["List"])
            for row in cur.fetchall() :
                list.append(classMyObject.from_dict(row))
            mydb.close()
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
        if ("ID" in classSQLRequests[classMyObject] and classConstraintID in classSQLRequests[classMyObject]["ID"]):
            mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["ID"][classConstraintID]+str(id)+";")
            for row in cur.fetchall() :
                list.append(classMyObject.from_dict(row))
            mydb.close()
        return list

    @classmethod
    def getListFromOtherIDWithDetailsFromOtherClassParameters(cls, classMyObject, classConstraintID, id):
        list = Database.getListFromOtherID(classMyObject, classConstraintID, id)
        for l in list :
            Database.getDetailsFromOtherClassParameters(l)
        return list

    @classmethod
    def getObjectFromID(cls, classMyObject, id):
        return Database.getObjectFromOtherID(classMyObject, classMyObject, id)

    @classmethod
    def getObjectFromOtherID(cls, classMyObject, classConstraintID, id):
        myObject = None
        if ("ID" in classSQLRequests[classMyObject] and classConstraintID in classSQLRequests[classMyObject]["ID"]):
            mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
            cur = mydb.cursor(dictionary=True)
            cur.execute(classSQLRequests[classMyObject]["ID"][classConstraintID]+str(id)+";")
            for row in cur.fetchall() :
                myObject = classMyObject.from_dict(row)
            mydb.close()
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
                        #setattr(myObject, objectName, Database.getListFromOtherID(subClassObject,parameter,myObject.id))
                        #current_app.logger.debug("Not included")
                        pass
                    else:
                        #current_app.logger.debug("Attribut {} / {} : {}".format(objectName,subClassObject,Database.getListFromOtherID(subClassObject,type(myObject),myObject.id)))
                        setattr(myObject, objectName, Database.getListFromOtherID(subClassObject,type(myObject),myObject.id))

            else:
                dictSubClasses = Database.getOtherClassParameters(myObject)
                for objectName, subClassObject in dictSubClasses.items():
                    setattr(myObject, objectName, Database.getListFromOtherID(subClassObject,type(myObject),myObject.id))

        return myObject
