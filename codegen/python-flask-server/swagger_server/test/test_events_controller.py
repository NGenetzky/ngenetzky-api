# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.event import Event
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestEventsController(BaseTestCase):
    """ EventsController integration test stubs """

    def test_get_event_by_id(self):
        """
        Test case for get_event_by_id

        Find event by ID
        """
        response = self.client.open('/nathansen/ngenetzky-api/1.0.0/event/{eventId}'.format(eventId=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()