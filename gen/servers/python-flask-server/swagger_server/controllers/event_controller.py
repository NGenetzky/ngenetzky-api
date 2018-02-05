import connexion
from swagger_server.models.event import Event
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server import data


def add_event(body):
    """
    Add a new event
    
    :param body: Object representing event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())

    db = data.Db()
    json = body.to_dict()
    try:
        json['published_at'] = json['published_at'].isoformat()
    except:
        pass
    db.post('event', json)
    return str(json)


def get_event_by_id(eventId):
    """
    Find event by ID
    Returns a single event
    :param eventId: ID of event to return
    :type eventId: int

    :rtype: Event
    """
    db = data.Db()
    return db.get('event', eventId)


def update_event(body):
    """
    Update an existing event
    
    :param body: Object representing event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())
    db = data.Db()
    json = body.to_dict()
    try:
        json['published_at'] = json['published_at'].isoformat()
    except:
        pass
    db.put('event', json['id'], json)
    return str(json)
