import connexion
import six

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.theme import Theme  # noqa: E501
from DebatIDOAPI import util


def theme_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Theme objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def theme_post(body):  # noqa: E501
    """Create Theme

     # noqa: E501

    :param body: 
    :type body: 

    :rtype: None
    """
    return 'do some magic!'


def themes_theme_iddelete(theme_id):  # noqa: E501
    """Delete Theme object

    Test # noqa: E501

    :param theme_id: The Id of a Theme
    :type theme_id: int

    :rtype: None
    """
    return 'do some magic!'


def themes_theme_idget(theme_id):  # noqa: E501
    """Retrieve a Theme object

    Test # noqa: E501

    :param theme_id: The Id of a Theme
    :type theme_id: int

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'
