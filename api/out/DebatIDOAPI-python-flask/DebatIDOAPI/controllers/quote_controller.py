import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.quote import Quote  # noqa: E501
from DebatIDOAPI import util

from flask import current_app
import inspect

import os
from sqlalchemy.engine.url import make_url
import mysql.connector

url = make_url(os.getenv('DATABASE_URL'))
mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def quote_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Quote objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    current_app.logger.debug("{} -- API_KEY : {}".format(inspect.stack()[0][3],connexion.request.headers['API_KEY']))
    quoteList = []
    curQuote = mydb.cursor(dictionary=True)
    curQuote.execute("SELECT q.id as quoteID, q.title as title, q.details as details, q.typeID as typeID, qt.title as typeTitle, q.dateUpdate as dateUpdate FROM quote q JOIN quoteType qt ON q.typeID = qt.id;")
    for rowQuote in curQuote.fetchall() :
        curTheme = mydb.cursor(dictionary=True)
        curTheme.execute("SELECT t.id as id, t.title as title FROM theme t JOIN quoteTheme qt ON t.id = qt.themeID WHERE qt.quoteID = "+str(rowQuote['quoteID'])+";")
        themeList = []
        for rowTheme in curTheme.fetchall() :
            themeList.append(rowTheme)
        rowQuote['themes'] = themeList

        quoteList.append(rowQuote)
    #for j in mycursor:
    #   quote_list.append(Quote(j))

    return quoteList


def quote_post(body):  # noqa: E501
    """Create Quote

     # noqa: E501

    :param body:
    :type body:

    :rtype: None
    """
    current_app.logger.debug("{} -- API_KEY : {}".format(inspect.stack()[0][3],connexion.request.headers['API_KEY']))
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
        for value in body._student_ids:
            mycursor.execute("INSERT INTO teacher_student VALUES ("+str(teacher_id)+","+str(value)+")")
    return 'Your API KEY : '+connexion.request.headers['API_KEY']


def quotes_quote_id_supports_get(quote_id, offset=None, limit=None):  # noqa: E501
    """Get list of supports quotes of specific quote

    This operation supports pagination # noqa: E501

    :param quote_id: The Id of a Quote
    :type quote_id: int
    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_quote_iddelete(quote_id):  # noqa: E501
    """Delete Quote object

    Test # noqa: E501

    :param quote_id: The Id of a Quote
    :type quote_id: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_quote_idget(quote_id):  # noqa: E501
    """Retrieve a Quote object

    Test # noqa: E501

    :param quote_id: The Id of a Quote
    :type quote_id: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_quote_idpatch(quote_id, quote):  # noqa: E501
    """Update Quote object

    Test # noqa: E501

    :param quote_id: The Id of a Quote
    :type quote_id: int
    :param quote:
    :type quote: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        quote = Quote.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
