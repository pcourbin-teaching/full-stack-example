# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from DebatIDOAPI.models.error_model import ErrorModel  # noqa: E501
from DebatIDOAPI.models.reference_model import ReferenceModel  # noqa: E501
from DebatIDOAPI.models.reference_new_model import ReferenceNewModel  # noqa: E501
from DebatIDOAPI.test import BaseTestCase


class TestReferenceController(BaseTestCase):
    """ReferenceController integration test stubs"""

    def test_quotes_id_quote_references_get(self):
        """Test case for quotes_id_quote_references_get

        Get list of references of specific quote
        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open(
            '/quotes/{idQuote}/references'.format(id_quote=1),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_get(self):
        """Test case for references_get

        Get all references
        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open(
            '/references',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_id_reference_delete(self):
        """Test case for references_id_reference_delete

        Delete one specific reference
        """
        response = self.client.open(
            '/references/{idReference}/'.format(id_reference=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_id_reference_get(self):
        """Test case for references_id_reference_get

        Get one specific reference
        """
        response = self.client.open(
            '/references/{idReference}/'.format(id_reference=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_references_post(self):
        """Test case for references_post

        Add a new reference
        """
        body = ReferenceNewModel()
        response = self.client.open(
            '/references',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
