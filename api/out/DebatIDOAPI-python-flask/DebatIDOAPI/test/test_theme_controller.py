# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from DebatIDOAPI.models.error import Error  # noqa: E501
from DebatIDOAPI.models.theme import Theme  # noqa: E501
from DebatIDOAPI.test import BaseTestCase


class TestThemeController(BaseTestCase):
    """ThemeController integration test stubs"""

    def test_theme_get(self):
        """Test case for theme_get

        Retrieve a collection of Theme objects
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/theme',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_theme_post(self):
        """Test case for theme_post

        Create Theme
        """
        body = {}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/theme',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_themes_theme_iddelete(self):
        """Test case for themes_theme_iddelete

        Delete Theme object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/themes/{theme_id}'.format(theme_id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_themes_theme_idget(self):
        """Test case for themes_theme_idget

        Retrieve a Theme object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/themes/{theme_id}'.format(theme_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_themes_theme_idpatch(self):
        """Test case for themes_theme_idpatch

        Update Theme object
        """
        theme = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/themes/{theme_id}'.format(theme_id=1),
            method='PATCH',
            headers=headers,
            data=json.dumps(theme),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
