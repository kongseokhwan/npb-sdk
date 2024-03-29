# coding: utf-8

"""
    PRISM NBAPI

    This is a PRISM NBAPI API Client module.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@kulcloud.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.dpidinfo_object2 import DpidinfoObject2  # noqa: F401,E501


class GetDpidinfoObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dpid_info': 'list[DpidinfoObject2]',
        'type': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'dpid_info': 'dpid_info',
        'type': 'type',
        'group_name': 'group_name'
    }

    def __init__(self, dpid_info=None, type=None, group_name=None):  # noqa: E501
        """GetDpidinfoObject - a model defined in Swagger"""  # noqa: E501

        self._dpid_info = None
        self._type = None
        self._group_name = None
        self.discriminator = None

        if dpid_info is not None:
            self.dpid_info = dpid_info
        if type is not None:
            self.type = type
        if group_name is not None:
            self.group_name = group_name

    @property
    def dpid_info(self):
        """Gets the dpid_info of this GetDpidinfoObject.  # noqa: E501


        :return: The dpid_info of this GetDpidinfoObject.  # noqa: E501
        :rtype: list[DpidinfoObject2]
        """
        return self._dpid_info

    @dpid_info.setter
    def dpid_info(self, dpid_info):
        """Sets the dpid_info of this GetDpidinfoObject.


        :param dpid_info: The dpid_info of this GetDpidinfoObject.  # noqa: E501
        :type: list[DpidinfoObject2]
        """

        self._dpid_info = dpid_info

    @property
    def type(self):
        """Gets the type of this GetDpidinfoObject.  # noqa: E501


        :return: The type of this GetDpidinfoObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetDpidinfoObject.


        :param type: The type of this GetDpidinfoObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def group_name(self):
        """Gets the group_name of this GetDpidinfoObject.  # noqa: E501


        :return: The group_name of this GetDpidinfoObject.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this GetDpidinfoObject.


        :param group_name: The group_name of this GetDpidinfoObject.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
                result[attr] = value
        if issubclass(GetDpidinfoObject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetDpidinfoObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
