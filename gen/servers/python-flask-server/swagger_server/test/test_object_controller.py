# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.api_response import ApiResponse
from swagger_server.models.patch_request import PatchRequest
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestObjectController(BaseTestCase):
    """ ObjectController integration test stubs """

    def test_call_fn(self):
        """
        Test case for call_fn

        Call a function/method.
        """
        args = 'args_example'
        response = self.client.open('/v0/call/{objId}/{name}'.format(objId=56, name='name_example'),
                                    method='POST',
                                    data=json.dumps(args),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_reg(self):
        """
        Test case for get_reg

        Get the value of a register
        """
        response = self.client.open('/v0/state/{objId}/reg/{index}'.format(objId=56, index=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_state(self):
        """
        Test case for get_state

        Get the state of the object.
        """
        response = self.client.open('/v0/state/{objId}'.format(objId=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_patch_state(self):
        """
        Test case for patch_state

        Partially modify the state of an object
        """
        body = PatchRequest()
        response = self.client.open('/v0/state/{objId}'.format(objId=56),
                                    method='PATCH',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
