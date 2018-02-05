# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.event import Event
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestEventController(BaseTestCase):
    """ EventController integration test stubs """

    def test_add_event(self):
        """
        Test case for add_event

        Add a new event
        """
        body = Event()
        response = self.client.open('/v0/event',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_event_by_id(self):
        """
        Test case for get_event_by_id

        Find event by ID
        """
        response = self.client.open('/v0/event/{eventId}'.format(eventId=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_event(self):
        """
        Test case for update_event

        Update an existing event
        """
        body = Event()
        response = self.client.open('/v0/event',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
