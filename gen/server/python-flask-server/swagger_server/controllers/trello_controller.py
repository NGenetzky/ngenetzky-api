import connexion
from swagger_server.models.trello_query import TrelloQuery
from swagger_server.models.universal_resource import UniversalResource
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def trello_model_id_put(model, id):
    """
    Updates the models currently in db.
    
    :param model: 
    :type model: str
    :param id: 
    :type id: str

    :rtype: UniversalResource
    """
    return 'do some magic!'


def trello_post(key=None, token=None, query=None):
    """
    trello_post
    
    :param key: 
    :type key: str
    :param token: 
    :type token: str
    :param query: 
    :type query: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        query = TrelloQuery.from_dict(connexion.request.get_json())
    return 'do some magic!'


def trello_put(key=None, token=None):
    """
    trello_put
    
    :param key: 
    :type key: str
    :param token: 
    :type token: str

    :rtype: int
    """
    return 'do some magic!'
