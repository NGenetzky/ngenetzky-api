# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.universal_resource import UniversalResource
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_uri_post(self):
        """
        Test case for uri_post

        
        """
        uri = UniversalResource()
        response = self.client.open('/v0/uri/',
                                    method='POST',
                                    data=json.dumps(uri),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
