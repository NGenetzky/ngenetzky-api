import connexion
from swagger_server.models.event import Event
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_event(body):
    """
    Add a new event
    
    :param body: Object representing event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())
    return 'do some magic!'


def update_event(body):
    """
    Update an existing event
    
    :param body: Object representing event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())
    return 'do some magic!'
