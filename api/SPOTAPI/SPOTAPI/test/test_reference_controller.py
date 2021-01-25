# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.reference import Reference  # noqa: E501
from SPOTAPI.test import BaseTestCase


class TestReferenceController(BaseTestCase):
    """ReferenceController integration test stubs"""

    def test_reference_get(self):
        """Test case for reference_get

        Retrieve a collection of Reference objects
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/reference',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reference_post(self):
        """Test case for reference_post

        Create Reference
        """
        reference = {}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/reference',
            method='POST',
            headers=headers,
            data=json.dumps(reference),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_reference_iddelete(self):
        """Test case for references_reference_iddelete

        Delete Reference object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/references/{reference_id}'.format(reference_id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_reference_idget(self):
        """Test case for references_reference_idget

        Retrieve a Reference object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/references/{reference_id}'.format(reference_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_reference_idpatch(self):
        """Test case for references_reference_idpatch

        Update Reference object
        """
        reference = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/references/{reference_id}'.format(reference_id=1),
            method='PATCH',
            headers=headers,
            data=json.dumps(reference),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
