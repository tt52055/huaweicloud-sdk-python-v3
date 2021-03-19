# coding: utf-8

import pprint
import re

import six





class CreateDnsNameRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dns_type': 'str'
    }

    attribute_map = {
        'dns_type': 'dns_type'
    }

    def __init__(self, dns_type=None):
        """CreateDnsNameRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._dns_type = None
        self.discriminator = None

        self.dns_type = dns_type

    @property
    def dns_type(self):
        """Gets the dns_type of this CreateDnsNameRequestBody.

        域名类型，当前只支持private

        :return: The dns_type of this CreateDnsNameRequestBody.
        :rtype: str
        """
        return self._dns_type

    @dns_type.setter
    def dns_type(self, dns_type):
        """Sets the dns_type of this CreateDnsNameRequestBody.

        域名类型，当前只支持private

        :param dns_type: The dns_type of this CreateDnsNameRequestBody.
        :type: str
        """
        self._dns_type = dns_type

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
        if not isinstance(other, CreateDnsNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other