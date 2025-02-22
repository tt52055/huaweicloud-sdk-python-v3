# coding: utf-8

import pprint
import re

import six





class ListAsyncCommandsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'command_id': 'str',
        'command_name': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'instance_id': 'Instance-Id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'command_id': 'command_id',
        'command_name': 'command_name'
    }

    def __init__(self, device_id=None, instance_id=None, limit=None, marker=None, offset=None, start_time=None, end_time=None, status=None, command_id=None, command_name=None):
        """ListAsyncCommandsRequest - a model defined in huaweicloud sdk"""
        
        

        self._device_id = None
        self._instance_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._command_id = None
        self._command_name = None
        self.discriminator = None

        self.device_id = device_id
        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if command_id is not None:
            self.command_id = command_id
        if command_name is not None:
            self.command_name = command_name

    @property
    def device_id(self):
        """Gets the device_id of this ListAsyncCommandsRequest.


        :return: The device_id of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListAsyncCommandsRequest.


        :param device_id: The device_id of this ListAsyncCommandsRequest.
        :type: str
        """
        self._device_id = device_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAsyncCommandsRequest.


        :return: The instance_id of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAsyncCommandsRequest.


        :param instance_id: The instance_id of this ListAsyncCommandsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListAsyncCommandsRequest.


        :return: The limit of this ListAsyncCommandsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAsyncCommandsRequest.


        :param limit: The limit of this ListAsyncCommandsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAsyncCommandsRequest.


        :return: The marker of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAsyncCommandsRequest.


        :param marker: The marker of this ListAsyncCommandsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListAsyncCommandsRequest.


        :return: The offset of this ListAsyncCommandsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAsyncCommandsRequest.


        :param offset: The offset of this ListAsyncCommandsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def start_time(self):
        """Gets the start_time of this ListAsyncCommandsRequest.


        :return: The start_time of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAsyncCommandsRequest.


        :param start_time: The start_time of this ListAsyncCommandsRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAsyncCommandsRequest.


        :return: The end_time of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAsyncCommandsRequest.


        :param end_time: The end_time of this ListAsyncCommandsRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListAsyncCommandsRequest.


        :return: The status of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAsyncCommandsRequest.


        :param status: The status of this ListAsyncCommandsRequest.
        :type: str
        """
        self._status = status

    @property
    def command_id(self):
        """Gets the command_id of this ListAsyncCommandsRequest.


        :return: The command_id of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this ListAsyncCommandsRequest.


        :param command_id: The command_id of this ListAsyncCommandsRequest.
        :type: str
        """
        self._command_id = command_id

    @property
    def command_name(self):
        """Gets the command_name of this ListAsyncCommandsRequest.


        :return: The command_name of this ListAsyncCommandsRequest.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this ListAsyncCommandsRequest.


        :param command_name: The command_name of this ListAsyncCommandsRequest.
        :type: str
        """
        self._command_name = command_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAsyncCommandsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
