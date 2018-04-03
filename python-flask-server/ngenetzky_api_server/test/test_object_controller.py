# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ngenetzky_api_server.models.api_response import ApiResponse  # noqa: E501
from ngenetzky_api_server.test import BaseTestCase


class TestObjectController(BaseTestCase):
    """ObjectController integration test stubs"""

    def test_call_obj_id_name_post(self):
        """Test case for call_obj_id_name_post

        Call a function/method.
        """
        args = 'args_example'
        response = self.client.open(
            '/v0/call/{objId}/{name}'.format(objId=56, name='name_example'),
            method='POST',
            data=json.dumps(args),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variable_obj_id_name_get(self):
        """Test case for variable_obj_id_name_get

        Returns variable
        """
        response = self.client.open(
            '/v0/variable/{objId}/{name}'.format(objId=56, name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_variable_obj_id_name_put(self):
        """Test case for variable_obj_id_name_put

        Set variable
        """
        response = self.client.open(
            '/v0/variable/{objId}/{name}'.format(objId=56, name='name_example'),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
