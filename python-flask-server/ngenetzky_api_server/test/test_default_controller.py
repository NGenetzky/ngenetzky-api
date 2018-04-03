# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ngenetzky_api_server.models.api_response import ApiResponse  # noqa: E501
from ngenetzky_api_server.models.universal_object import UniversalObject  # noqa: E501
from ngenetzky_api_server.models.uuid1 import Uuid1  # noqa: E501
from ngenetzky_api_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_data_type_post(self):
        """Test case for data_type_post

        Add new data
        """
        data = None
        response = self.client.open(
            '/v0/data/{type}/'.format(type=8.14),
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_uuid1_post(self):
        """Test case for uuid1_post

        Create new or add existing UUID1.
        """
        obj = Uuid1()
        response = self.client.open(
            '/v0/uuid1/',
            method='POST',
            data=json.dumps(obj),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
