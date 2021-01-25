import connexion
import six

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.theme import Theme  # noqa: E501
from SPOTAPI import util

from SPOTAPI.controllers.database_controller import Database

def theme_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Theme objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return Database.getListWithDetailsFromOtherClassParameters(Theme)


def theme_post(theme):  # noqa: E501
    """Create Theme

     # noqa: E501

    :param theme: 
    :type theme: dict | bytes

    :rtype: None
    """
    valueReturn = 0
    codeReturn = 401

    if connexion.request.is_json:
        theme = Theme.from_dict(connexion.request.get_json())  # noqa: E501
        valueReturn, codeReturn = Database.postNewObject(theme)

    return valueReturn, codeReturn


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
    return Database.getObjectFromIDWithDetailsFromOtherClassParameters(Theme,theme_id)


def themes_theme_idpatch(theme_id, theme):  # noqa: E501
    """Update Theme object

    Test # noqa: E501

    :param theme_id: The Id of a Theme
    :type theme_id: int
    :param theme: 
    :type theme: dict | bytes

    :rtype: None
    """
    valueReturn = 0
    codeReturn = 401

    if connexion.request.is_json:
        theme = Theme.from_dict(connexion.request.get_json())  # noqa: E501
        valueReturn, codeReturn = Database.patchObject(theme, theme_id)

    return valueReturn, codeReturn
