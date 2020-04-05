import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.protagonist import Protagonist  # noqa: E501
from DebatIDOAPI import util

from flask import current_app
import inspect

from DebatIDOAPI.controllers.database_controller import Database

def protagonist_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Protagonist objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def protagonist_post(body):  # noqa: E501
    """Create Protagonist

     # noqa: E501

    :param body:
    :type body:

    :rtype: None
    """
    return 'do some magic!'


def protagonists_protagonist_iddelete(protagonist_id):  # noqa: E501
    """Delete Protagonist object

    Test # noqa: E501

    :param protagonist_id: The Id of a Protagonist
    :type protagonist_id: int

    :rtype: None
    """
    return 'do some magic!'


def protagonists_protagonist_idget(protagonist_id):  # noqa: E501
    """Retrieve a Protagonist object

    Test # noqa: E501

    :param protagonist_id: The Id of a Protagonist
    :type protagonist_id: int

    :rtype: None
    """
    protagonist = Database.getProtagonistFromID(protagonist_id)

    return protagonist


def protagonists_protagonist_idpatch(protagonist_id, protagonist):  # noqa: E501
    """Update Protagonist object

    Test # noqa: E501

    :param protagonist_id: The Id of a Protagonist
    :type protagonist_id: int
    :param protagonist:
    :type protagonist: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        protagonist = Protagonist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
