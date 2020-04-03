# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from DebatIDOAPI.models.error_model import ErrorModel  # noqa: E501
from DebatIDOAPI.models.quote_model import QuoteModel  # noqa: E501
from DebatIDOAPI.models.source_model import SourceModel  # noqa: E501
from DebatIDOAPI.test import BaseTestCase


class TestQuoteController(BaseTestCase):
    """QuoteController integration test stubs"""

    def test_quotes_id_quote_childs_get(self):
        """Test case for quotes_id_quote_childs_get

        Get list of childs of specific quote
        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open(
            '/quotes/{idQuote}/childs'.format(id_quote=1),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_id_quote_delete(self):
        """Test case for quotes_id_quote_delete

        Delete one specific quote
        """
        response = self.client.open(
            '/quotes/{idQuote}/'.format(id_quote=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_id_quote_get(self):
        """Test case for quotes_id_quote_get

        Get one specific quote
        """
        response = self.client.open(
            '/quotes/{idQuote}/'.format(id_quote=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_id_quote_parents_get(self):
        """Test case for quotes_id_quote_parents_get

        Get list of parents of specific quote
        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open(
            '/quotes/{idQuote}/parents'.format(id_quote=1),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_id_quote_sources_get(self):
        """Test case for quotes_id_quote_sources_get

        Get list of sources of specific quote
        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open(
            '/quotes/{idQuote}/sources'.format(id_quote=1),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
