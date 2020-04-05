import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.theme import Theme  # noqa: E501
from DebatIDOAPI import util

from DebatIDOAPI.controllers.database_controller import Database
from flask import current_app
import inspect

def theme_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Theme objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """

    list = Database.getList(Theme)
    for l in list :
        Database.getDetailsFromOtherClassParameters(l)

    return list


def theme_post(theme):  # noqa: E501
    """Create Theme

     # noqa: E501

    :param theme:
    :type theme: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        theme = Theme.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def themes_theme_iddelete(theme_id):  # noqa: E501
    """Delete Theme object

    Test # noqa: E501

    :param theme_id: The Id of a Theme
    :type theme_id: int

    :rtype: None
    """
    return Database.deleteObjectFromID(Theme,theme_id)


def themes_theme_idget(theme_id):  # noqa: E501
    """Retrieve a Theme object

    Test # noqa: E501

    :param theme_id: The Id of a Theme
    :type theme_id: int

    :rtype: None
    """
    myObject = Database.getObjectFromID(Theme,theme_id)
    Database.getDetailsFromOtherClassParameters(myObject)
    return myObject


def themes_theme_idpatch(theme_id, theme):  # noqa: E501
    """Update Theme object

    Test # noqa: E501

    :param theme_id: The Id of a Theme
    :type theme_id: int
    :param theme:
    :type theme: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        theme = Theme.from_dict(connexion.request.get_json())  # noqa: E501

    Database.patchObjectFromID(theme, theme_id)
    return 'do some magic!'
