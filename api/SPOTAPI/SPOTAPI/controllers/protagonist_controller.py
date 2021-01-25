import connexion
import six

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.protagonist import Protagonist  # noqa: E501
from SPOTAPI import util

from SPOTAPI.controllers.database_controller import Database

def protagonist_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Protagonist objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return Database.getListWithDetailsFromOtherClassParameters(Protagonist)


def protagonist_post(protagonist):  # noqa: E501
    """Create Protagonist

     # noqa: E501

    :param protagonist: 
    :type protagonist: dict | bytes

    :rtype: None
    """
    valueReturn = 0
    codeReturn = 401

    if connexion.request.is_json:
        protagonist = Protagonist.from_dict(connexion.request.get_json())  # noqa: E501
        valueReturn, codeReturn = Database.postNewObject(protagonist)

    return valueReturn, codeReturn


def protagonists_protagonist_iddelete(protagonist_id):  # noqa: E501
    """Delete Protagonist object

    Test # noqa: E501

    :param protagonist_id: The Id of a Protagonist
    :type protagonist_id: int

    :rtype: None
    """
    return Database.deleteObjectFromID(Protagonist,protagonist_id)


def protagonists_protagonist_idget(protagonist_id):  # noqa: E501
    """Retrieve a Protagonist object

    Test # noqa: E501

    :param protagonist_id: The Id of a Protagonist
    :type protagonist_id: int

    :rtype: None
    """
    return Database.getObjectFromIDWithDetailsFromOtherClassParameters(Protagonist,protagonist_id)


def protagonists_protagonist_idpatch(protagonist_id, protagonist):  # noqa: E501
    """Update Protagonist object

    Test # noqa: E501

    :param protagonist_id: The Id of a Protagonist
    :type protagonist_id: int
    :param protagonist: 
    :type protagonist: dict | bytes

    :rtype: None
    """
    valueReturn = 0
    codeReturn = 401

    if connexion.request.is_json:
        protagonist = Protagonist.from_dict(connexion.request.get_json())  # noqa: E501
        valueReturn, codeReturn = Database.patchObject(protagonist,protagonist_id)

    return valueReturn, codeReturn
