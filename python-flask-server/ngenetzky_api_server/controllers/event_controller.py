import connexion
import six

from ngenetzky_api_server.models.api_response import ApiResponse  # noqa: E501
from ngenetzky_api_server.models.event import Event  # noqa: E501
from ngenetzky_api_server import util


def event_event_id_get(eventId):  # noqa: E501
    """Find event by ID

    Returns a single event # noqa: E501

    :param eventId: ID of event to return
    :type eventId: int

    :rtype: Event
    """
    return 'do some magic!'


def event_post(body):  # noqa: E501
    """Add a new event

     # noqa: E501

    :param body: Object representing event
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
