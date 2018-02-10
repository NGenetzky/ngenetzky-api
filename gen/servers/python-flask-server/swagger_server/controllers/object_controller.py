import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.patch_request import PatchRequest
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from ..uobj import create_reg

def call_fn(objId, name, args=None):
    """
    Call a function/method.
    
    :param objId: Identified object to act on.
    :type objId: int
    :param name: Function/Method Name.
    :type name: str
    :param args: Parameters/Arguments
    :type args: str

    :rtype: ApiResponse
    """
    o = create_reg()
    ar = ApiResponse(o.id, o.uuid)
    return ar


def get_reg(objId, index):
    """
    Get the value of a register
    
    :param objId: Identified object to act on.
    :type objId: int
    :param index: Index of the register.
    :type index: int

    :rtype: int
    """
    return 'do some magic!'


def get_state(objId):
    """
    Get the state of the object.
    
    :param objId: Identified object to act on.
    :type objId: int

    :rtype: object
    """
    return 'do some magic!'


def patch_state(objId, body):
    """
    Partially modify the state of an object
    
    :param objId: Identified object to act on.
    :type objId: int
    :param body: Object representing event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchRequest.from_dict(connexion.request.get_json())
    return 'do some magic!'
