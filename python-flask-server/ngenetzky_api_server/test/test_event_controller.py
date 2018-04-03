# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ngenetzky_api_server.models.api_response import ApiResponse  # noqa: E501
from ngenetzky_api_server.models.event import Event  # noqa: E501
from ngenetzky_api_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_event_event_id_get(self):
        """Test case for event_event_id_get

        Find event by ID
        """
        response = self.client.open(
            '/v0/event/{eventId}'.format(eventId=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_event_post(self):
        """Test case for event_post

        Add a new event
        """
        body = Event()
        response = self.client.open(
            '/v0/event',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
