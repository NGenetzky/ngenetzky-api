import connexion
from swagger_server.models.event import Event
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_event_by_id(eventId):
    """
    Find event by ID
    Returns a single event
    :param eventId: ID of event to return
    :type eventId: int

    :rtype: Event
    """
    return 'do some magic!'
