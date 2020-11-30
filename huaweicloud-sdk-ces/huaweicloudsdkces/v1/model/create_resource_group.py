# coding: utf-8

import pprint
import re

import six





class CreateResourceGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimensions': 'list[MetricsDimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, dimensions=None):
        """CreateResourceGroup - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._dimensions = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this CreateResourceGroup.

        资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html

        :return: The namespace of this CreateResourceGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CreateResourceGroup.

        资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html

        :param namespace: The namespace of this CreateResourceGroup.
        :type: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this CreateResourceGroup.

        一个或者多个资源维度。

        :return: The dimensions of this CreateResourceGroup.
        :rtype: list[MetricsDimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this CreateResourceGroup.

        一个或者多个资源维度。

        :param dimensions: The dimensions of this CreateResourceGroup.
        :type: list[MetricsDimension]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, CreateResourceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
