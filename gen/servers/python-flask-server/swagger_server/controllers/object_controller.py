import connexion
from swagger_server.models.arg_vector import ArgVector
from swagger_server.models.patch_request import PatchRequest
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def call_fn(objId, name, argv):
    """
    Call a function/method.
    
    :param objId: Identified object to act on.
    :type objId: int
    :param name: Function/Method Name.
    :type name: str
    :param argv: Parameters/Arguments
    :type argv: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        argv = ArgVector.from_dict(connexion.request.get_json())
    return 'do some magic!'


def get_reg(objId, index):
    """
    Get the value of a register
    Returns a single event
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
    Add a new event
    
    :param objId: Identified object to act on.
    :type objId: int
    :param body: Object representing event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchRequest.from_dict(connexion.request.get_json())
    return 'do some magic!'
