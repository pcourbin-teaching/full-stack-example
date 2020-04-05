import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.quote import Quote  # noqa: E501
from DebatIDOAPI import util

from flask import current_app
import inspect

from DebatIDOAPI.controllers.database_controller import Database

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
    quoteList = Database.getListQuotes()

    for q in quoteList :
        q.themes = Database.getThemesFromQuoteID(q.id)
        q.references = Database.getReferencesFromQuoteID(q.id)

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
