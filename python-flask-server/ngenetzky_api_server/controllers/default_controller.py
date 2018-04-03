import connexion
import six

from ngenetzky_api_server.models.api_response import ApiResponse  # noqa: E501
from ngenetzky_api_server.models.universal_object import UniversalObject  # noqa: E501
from ngenetzky_api_server.models.uuid1 import Uuid1  # noqa: E501
from ngenetzky_api_server import util


def data_type_post(type, data):  # noqa: E501
    """Add new data

     # noqa: E501

    :param type: 
    :type type: 
    :param data: 
    :type data: 

    :rtype: UniversalObject
    """
    return 'do some magic!'


def uuid1_post(obj=None):  # noqa: E501
    """Create new or add existing UUID1.

     # noqa: E501

    :param obj: 
    :type obj: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        obj = Uuid1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
