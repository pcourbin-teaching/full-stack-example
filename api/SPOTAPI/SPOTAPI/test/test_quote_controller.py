# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.quote import Quote  # noqa: E501
from SPOTAPI.test import BaseTestCase


class TestQuoteController(BaseTestCase):
    """QuoteController integration test stubs"""

    def test_quote_get(self):
        """Test case for quote_get

        Retrieve a collection of Quote objects
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quote',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quote_post(self):
        """Test case for quote_post

        Create Quote
        """
        quote = {}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quote',
            method='POST',
            headers=headers,
            data=json.dumps(quote),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_quote_id_mains_get(self):
        """Test case for quotes_quote_id_mains_get

        Get list of mains quotes supported by a specific quote
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quotes/{quote_id}/mains'.format(quote_id=1),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_quote_id_supports_get(self):
        """Test case for quotes_quote_id_supports_get

        Get list of supports quotes for a specific quote
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quotes/{quote_id}/supports'.format(quote_id=1),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_quote_iddelete(self):
        """Test case for quotes_quote_iddelete

        Delete Quote object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quotes/{quote_id}'.format(quote_id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_quote_idget(self):
        """Test case for quotes_quote_idget

        Retrieve a Quote object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quotes/{quote_id}'.format(quote_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_quote_idpatch(self):
        """Test case for quotes_quote_idpatch

        Update Quote object
        """
        quote = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/quotes/{quote_id}'.format(quote_id=1),
            method='PATCH',
            headers=headers,
            data=json.dumps(quote),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
