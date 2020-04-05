import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.quote import Quote  # noqa: E501
from DebatIDOAPI.models.theme import Theme  # noqa: E501
from DebatIDOAPI.models.reference import Reference  # noqa: E501
from DebatIDOAPI.models.protagonist import Protagonist  # noqa: E501
from DebatIDOAPI.models.person import Person  # noqa: E501
from DebatIDOAPI.models.company import Company  # noqa: E501
from DebatIDOAPI import util

from flask import current_app
import inspect

import os
from sqlalchemy.engine.url import make_url
import mysql.connector

url = make_url(os.getenv('DATABASE_URL'))
mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)

class Database:
    @classmethod
    def getListQuotes(cls):
        listQuotes = []
        curQuote = mydb.cursor(dictionary=True)
        curQuote.execute("SELECT q.id as id, q.title as title, q.details as details, q.typeID as typeID, qt.title as typeTitle, q.dateUpdate as dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id;")
        for rowQuote in curQuote.fetchall() :
            listQuotes.append(Quote.from_dict(rowQuote))
        return listQuotes

    @classmethod
    def getReferencesFromQuoteID(cls, id):
        list = []
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT r.id, r.title, r.details, r.url, r.date, r.typeID, rt.title, r.reliability, r.dateUpdate FROM reference r JOIN quoteReference qr ON r.id = qr.referenceID JOIN referenceType rt ON r.typeID = rt.id WHERE qr.quoteID = "+str(id)+";")
        for row in cur.fetchall() :
            r = Reference.from_dict(row)
            r.authors = Database.getAuthorFromReferenceID(r.id)
            list.append(r)
        return list

    @classmethod
    def getThemesFromQuoteID(cls, id):
        list = []
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT t.id as id, t.title as title FROM theme t JOIN quoteTheme qt ON t.id = qt.themeID WHERE qt.quoteID = "+str(id)+";")
        for row in cur.fetchall() :
            list.append(Theme.from_dict(row))
        return list

    @classmethod
    def getAuthorFromReferenceID(cls, id):
        list = []
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT p.id, p.type, p.name, p.link, p.photo, p.dateUpdate FROM protagonist p JOIN referenceAuthor ra ON p.id = ra.authorID JOIN reference r ON r.id = ra.referenceID WHERE r.id = "+str(id)+";")
        for row in cur.fetchall() :
            protagonist = Protagonist.from_dict(row)
            if (protagonist.type == "person"):
                protagonist.person = Database.getPersonFromReferenceID(protagonist.id)
            elif (protagonist.type == "person"):
                protagonist.company = Database.getCompanyFromReferenceID(protagonist.id)
            list.append(protagonist)
        return list

    @classmethod
    def getPersonFromReferenceID(cls, id):
        person = None
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT pe.id, pe.protagonistID, pe.surname, pe.role, pe.dateUpdate FROM protagonist pr JOIN person pe ON pr.id = pe.protagonistID WHERE pr.id = "+str(id)+";")
        for row in cur.fetchall() :
            person = Person.from_dict(row)
        return person

    @classmethod
    def getCompanyFromReferenceID(cls, id):
        company = None
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT pe.id, pe.protagonistID, pe.siret, pe.dateUpdate FROM protagonist pr JOIN company c ON pr.id = c.protagonistID WHERE pr.id = "+str(id)+";")
        for row in cur.fetchall() :
            company = Company.from_dict(row)
        return company
