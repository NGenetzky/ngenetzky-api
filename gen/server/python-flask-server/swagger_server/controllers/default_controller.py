import connexion
from swagger_server.models.universal_resource import UniversalResource
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def uri_post(uri):
    """
    uri_post
    
    :param uri: 
    :type uri: dict | bytes

    :rtype: UniversalResource
    """
    if connexion.request.is_json:
        uri = UniversalResource.from_dict(connexion.request.get_json())
    return 'do some magic!'
