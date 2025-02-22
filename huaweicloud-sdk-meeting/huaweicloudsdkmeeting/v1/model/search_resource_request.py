# coding: utf-8

import pprint
import re

import six





class SearchResourceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'corp_id': 'str',
        'start_expire_date': 'int',
        'end_expire_date': 'int',
        'type': 'str',
        'type_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'corp_id': 'corp_id',
        'start_expire_date': 'startExpireDate',
        'end_expire_date': 'endExpireDate',
        'type': 'type',
        'type_id': 'typeId',
        'status': 'status'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, corp_id=None, start_expire_date=None, end_expire_date=None, type=None, type_id=None, status=None):
        """SearchResourceRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._corp_id = None
        self._start_expire_date = None
        self._end_expire_date = None
        self._type = None
        self._type_id = None
        self._status = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        self.corp_id = corp_id
        if start_expire_date is not None:
            self.start_expire_date = start_expire_date
        if end_expire_date is not None:
            self.end_expire_date = end_expire_date
        if type is not None:
            self.type = type
        if type_id is not None:
            self.type_id = type_id
        if status is not None:
            self.status = status

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchResourceRequest.


        :return: The x_request_id of this SearchResourceRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchResourceRequest.


        :param x_request_id: The x_request_id of this SearchResourceRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchResourceRequest.


        :return: The accept_language of this SearchResourceRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchResourceRequest.


        :param accept_language: The accept_language of this SearchResourceRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchResourceRequest.


        :return: The offset of this SearchResourceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchResourceRequest.


        :param offset: The offset of this SearchResourceRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchResourceRequest.


        :return: The limit of this SearchResourceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchResourceRequest.


        :param limit: The limit of this SearchResourceRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchResourceRequest.


        :return: The search_key of this SearchResourceRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchResourceRequest.


        :param search_key: The search_key of this SearchResourceRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def corp_id(self):
        """Gets the corp_id of this SearchResourceRequest.


        :return: The corp_id of this SearchResourceRequest.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this SearchResourceRequest.


        :param corp_id: The corp_id of this SearchResourceRequest.
        :type: str
        """
        self._corp_id = corp_id

    @property
    def start_expire_date(self):
        """Gets the start_expire_date of this SearchResourceRequest.


        :return: The start_expire_date of this SearchResourceRequest.
        :rtype: int
        """
        return self._start_expire_date

    @start_expire_date.setter
    def start_expire_date(self, start_expire_date):
        """Sets the start_expire_date of this SearchResourceRequest.


        :param start_expire_date: The start_expire_date of this SearchResourceRequest.
        :type: int
        """
        self._start_expire_date = start_expire_date

    @property
    def end_expire_date(self):
        """Gets the end_expire_date of this SearchResourceRequest.


        :return: The end_expire_date of this SearchResourceRequest.
        :rtype: int
        """
        return self._end_expire_date

    @end_expire_date.setter
    def end_expire_date(self, end_expire_date):
        """Sets the end_expire_date of this SearchResourceRequest.


        :param end_expire_date: The end_expire_date of this SearchResourceRequest.
        :type: int
        """
        self._end_expire_date = end_expire_date

    @property
    def type(self):
        """Gets the type of this SearchResourceRequest.


        :return: The type of this SearchResourceRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchResourceRequest.


        :param type: The type of this SearchResourceRequest.
        :type: str
        """
        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this SearchResourceRequest.


        :return: The type_id of this SearchResourceRequest.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this SearchResourceRequest.


        :param type_id: The type_id of this SearchResourceRequest.
        :type: str
        """
        self._type_id = type_id

    @property
    def status(self):
        """Gets the status of this SearchResourceRequest.


        :return: The status of this SearchResourceRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchResourceRequest.


        :param status: The status of this SearchResourceRequest.
        :type: int
        """
        self._status = status

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
        if not isinstance(other, SearchResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
