from typing import List

from flask import current_app
import inspect

from connexion.exceptions import OAuthProblem

TOKEN_DB = {
    'G#hqqq8NlW&tz5Hjk#%qcr7^iV*P%2pZWd*!mafPpu5!ANjJwM': {
        'uid': 100,
        'sub' : "root"
    },
    'vC$!Y0CEnMjyT07E&$66lYkyN^G4Zd$C8#0sV1wVzeqn%I@8LY': {
        'uid': 200,
        'sub' : "front"
    }
}

def info_from_ApiKeyAuth(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: dict | None
    """
    current_app.logger.debug("{} -- {}".format(api_key, TOKEN_DB))

    info = TOKEN_DB.get(api_key, None)

    current_app.logger.debug("{} -- {} -- {}".format(info, api_key, TOKEN_DB))

    if not info:
        raise OAuthProblem('Invalid token')

    return info
