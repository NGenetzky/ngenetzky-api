# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SavedState(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, uuid: str=None, last_update: datetime=None, hash: int=None):
        """
        SavedState - a model defined in Swagger

        :param uuid: The uuid of this SavedState.
        :type uuid: str
        :param last_update: The last_update of this SavedState.
        :type last_update: datetime
        :param hash: The hash of this SavedState.
        :type hash: int
        """
        self.swagger_types = {
            'uuid': str,
            'last_update': datetime,
            'hash': int
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'last_update': 'lastUpdate',
            'hash': 'hash'
        }

        self._uuid = uuid
        self._last_update = last_update
        self._hash = hash

    @classmethod
    def from_dict(cls, dikt) -> 'SavedState':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SavedState of this SavedState.
        :rtype: SavedState
        """
        return deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """
        Gets the uuid of this SavedState.

        :return: The uuid of this SavedState.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """
        Sets the uuid of this SavedState.

        :param uuid: The uuid of this SavedState.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def last_update(self) -> datetime:
        """
        Gets the last_update of this SavedState.

        :return: The last_update of this SavedState.
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update: datetime):
        """
        Sets the last_update of this SavedState.

        :param last_update: The last_update of this SavedState.
        :type last_update: datetime
        """

        self._last_update = last_update

    @property
    def hash(self) -> int:
        """
        Gets the hash of this SavedState.
        Hash computed from the state.

        :return: The hash of this SavedState.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash: int):
        """
        Sets the hash of this SavedState.
        Hash computed from the state.

        :param hash: The hash of this SavedState.
        :type hash: int
        """

        self._hash = hash

