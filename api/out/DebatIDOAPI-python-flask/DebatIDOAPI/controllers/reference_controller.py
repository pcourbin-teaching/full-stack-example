import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.reference import Reference  # noqa: E501
from DebatIDOAPI import util


def reference_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Reference objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def reference_post(body):  # noqa: E501
    """Create Reference

     # noqa: E501

    :param body: 
    :type body: 

    :rtype: None
    """
    return 'do some magic!'


def references_reference_iddelete(reference_id):  # noqa: E501
    """Delete Reference object

    Test # noqa: E501

    :param reference_id: The Id of a Reference
    :type reference_id: int

    :rtype: None
    """
    return 'do some magic!'


def references_reference_idget(reference_id):  # noqa: E501
    """Retrieve a Reference object

    Test # noqa: E501

    :param reference_id: The Id of a Reference
    :type reference_id: int

    :rtype: None
    """
    return 'do some magic!'


def references_reference_idpatch(reference_id, reference):  # noqa: E501
    """Update Reference object

    Test # noqa: E501

    :param reference_id: The Id of a Reference
    :type reference_id: int
    :param reference: 
    :type reference: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        reference = Reference.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
