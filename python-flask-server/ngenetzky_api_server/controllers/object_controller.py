import connexion
import six

from ngenetzky_api_server.models.api_response import ApiResponse  # noqa: E501
from ngenetzky_api_server import util


def call_obj_id_name_post(objId, name, args=None):  # noqa: E501
    """Call a function/method.

     # noqa: E501

    :param objId: Identified object to act on.
    :type objId: int
    :param name: Function/Method Name.
    :type name: str
    :param args: Parameters/Arguments
    :type args: str

    :rtype: ApiResponse
    """
    return 'do some magic!'


def variable_obj_id_name_get(objId, name):  # noqa: E501
    """Returns variable

     # noqa: E501

    :param objId: Identified object to act on.
    :type objId: int
    :param name: Variable Name.
    :type name: str

    :rtype: str
    """
    return 'do some magic!'


def variable_obj_id_name_put(objId, name):  # noqa: E501
    """Set variable

     # noqa: E501

    :param objId: Identified object to act on.
    :type objId: int
    :param name: Variable Name.
    :type name: str

    :rtype: None
    """
    return 'do some magic!'
