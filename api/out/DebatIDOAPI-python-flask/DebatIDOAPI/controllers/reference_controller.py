import connexion
import six

from DebatIDOAPI.models.error_model import ErrorModel  # noqa: E501
from DebatIDOAPI.models.reference_model import ReferenceModel  # noqa: E501
from DebatIDOAPI.models.reference_new_model import ReferenceNewModel  # noqa: E501
from DebatIDOAPI import util


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


def references_get(offset=None, limit=None):  # noqa: E501
    """Get all references

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def references_id_reference_delete(id_reference):  # noqa: E501
    """Delete one specific reference

    Test # noqa: E501

    :param id_reference: The Id of a Quote
    :type id_reference: int

    :rtype: None
    """
    return 'do some magic!'


def references_id_reference_get(id_reference):  # noqa: E501
    """Get one specific reference

    Test # noqa: E501

    :param id_reference: The Id of a Quote
    :type id_reference: int

    :rtype: None
    """
    return 'do some magic!'


def references_post(body):  # noqa: E501
    """Add a new reference

     # noqa: E501

    :param body: A JSON object containing reference data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ReferenceNewModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
