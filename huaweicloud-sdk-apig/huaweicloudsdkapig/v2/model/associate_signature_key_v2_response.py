# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class AssociateSignatureKeyV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bindings': 'list[SignBindingApiResp]'
    }

    attribute_map = {
        'bindings': 'bindings'
    }

    def __init__(self, bindings=None):
        """AssociateSignatureKeyV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bindings = None
        self.discriminator = None

        if bindings is not None:
            self.bindings = bindings

    @property
    def bindings(self):
        """Gets the bindings of this AssociateSignatureKeyV2Response.

        API与签名密钥的绑定关系列表

        :return: The bindings of this AssociateSignatureKeyV2Response.
        :rtype: list[SignBindingApiResp]
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        """Sets the bindings of this AssociateSignatureKeyV2Response.

        API与签名密钥的绑定关系列表

        :param bindings: The bindings of this AssociateSignatureKeyV2Response.
        :type: list[SignBindingApiResp]
        """
        self._bindings = bindings

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
        if not isinstance(other, AssociateSignatureKeyV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other