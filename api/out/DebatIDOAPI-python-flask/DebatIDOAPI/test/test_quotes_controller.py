# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from DebatIDOAPI.models.quote_model import QuoteModel  # noqa: E501
from DebatIDOAPI.test import BaseTestCase


class TestQuotesController(BaseTestCase):
    """QuotesController integration test stubs"""

    def test_quotes_get(self):
        """Test case for quotes_get

        Get all quotes
        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open(
            '/quotes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quotes_post(self):
        """Test case for quotes_post

        Add a new quote
        """
        body = QuoteModel()
        response = self.client.open(
            '/quotes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
