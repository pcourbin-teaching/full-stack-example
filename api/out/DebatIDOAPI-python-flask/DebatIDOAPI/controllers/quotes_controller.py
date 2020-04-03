import connexion
import six

from DebatIDOAPI.models.error_model import ErrorModel  # noqa: E501
from DebatIDOAPI.models.quote_model import QuoteModel  # noqa: E501
from DebatIDOAPI.models.quote_new_model import QuoteNewModel  # noqa: E501
from DebatIDOAPI.models.reference_model import ReferenceModel  # noqa: E501
from DebatIDOAPI import util


def quotes_get(offset=None, limit=None):  # noqa: E501
    """Get all quotes

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_id_quote_childs_get(id_quote, offset=None, limit=None):  # noqa: E501
    """Get list of childs of specific quote

    This operation supports pagination # noqa: E501

    :param id_quote: The Id of a Quote
    :type id_quote: int
    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_id_quote_delete(id_quote):  # noqa: E501
    """Delete one specific quote

    Test # noqa: E501

    :param id_quote: The Id of a Quote
    :type id_quote: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_id_quote_get(id_quote):  # noqa: E501
    """Get one specific quote

    Test # noqa: E501

    :param id_quote: The Id of a Quote
    :type id_quote: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_id_quote_parents_get(id_quote, offset=None, limit=None):  # noqa: E501
    """Get list of parents of specific quote

    This operation supports pagination # noqa: E501

    :param id_quote: The Id of a Quote
    :type id_quote: int
    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_id_quote_references_get(id_quote, offset=None, limit=None):  # noqa: E501
    """Get list of references of specific quote

    This operation supports pagination # noqa: E501

    :param id_quote: The Id of a Quote
    :type id_quote: int
    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def quotes_post(body):  # noqa: E501
    """Add a new quote

     # noqa: E501

    :param body: A JSON object containing quote data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = QuoteNewModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
