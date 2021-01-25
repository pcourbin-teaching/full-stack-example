# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.protagonist import Protagonist  # noqa: E501
from SPOTAPI.test import BaseTestCase


class TestProtagonistController(BaseTestCase):
    """ProtagonistController integration test stubs"""

    def test_protagonist_get(self):
        """Test case for protagonist_get

        Retrieve a collection of Protagonist objects
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/protagonist',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_protagonist_post(self):
        """Test case for protagonist_post

        Create Protagonist
        """
        protagonist = {}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/protagonist',
            method='POST',
            headers=headers,
            data=json.dumps(protagonist),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_protagonists_protagonist_iddelete(self):
        """Test case for protagonists_protagonist_iddelete

        Delete Protagonist object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/protagonists/{protagonist_id}'.format(protagonist_id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_protagonists_protagonist_idget(self):
        """Test case for protagonists_protagonist_idget

        Retrieve a Protagonist object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/protagonists/{protagonist_id}'.format(protagonist_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_protagonists_protagonist_idpatch(self):
        """Test case for protagonists_protagonist_idpatch

        Update Protagonist object
        """
        protagonist = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/protagonists/{protagonist_id}'.format(protagonist_id=1),
            method='PATCH',
            headers=headers,
            data=json.dumps(protagonist),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
