import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.quote import Quote  # noqa: E501
from DebatIDOAPI.models.reference import Reference  # noqa: E501
from DebatIDOAPI.models.theme import Theme  # noqa: E501
from DebatIDOAPI.models.protagonist import Protagonist  # noqa: E501
from DebatIDOAPI import util

from DebatIDOAPI.controllers.database_controller import Database
from flask import current_app
import inspect

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

    list = Database.getList(Quote)
    for l in list :
        Database.getDetailsFromOtherClassParameters(l)

    return list


def quote_post(quote):  # noqa: E501
    """Create Quote

     # noqa: E501

    :param quote:
    :type quote: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        quote = Quote.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
    return Database.deleteObjectFromID(Quote,quote_id)


def quotes_quote_idget(quote_id):  # noqa: E501
    """Retrieve a Quote object

    Test # noqa: E501

    :param quote_id: The Id of a Quote
    :type quote_id: int

    :rtype: None
    """
    myObject = Database.getObjectFromID(Quote,quote_id)
    Database.getDetailsFromOtherClassParameters(myObject)
    return myObject


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
