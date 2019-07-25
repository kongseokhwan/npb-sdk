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

from swagger_client.models.port_statistics import PortStatistics  # noqa: F401,E501


class ALLPortStatisticsRespList(object):
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
        'port_stats': 'list[PortStatistics]'
    }

    attribute_map = {
        'port_stats': 'port_stats'
    }

    def __init__(self, port_stats=None):  # noqa: E501
        """ALLPortStatisticsRespList - a model defined in Swagger"""  # noqa: E501

        self._port_stats = None
        self.discriminator = None

        if port_stats is not None:
            self.port_stats = port_stats

    @property
    def port_stats(self):
        """Gets the port_stats of this ALLPortStatisticsRespList.  # noqa: E501


        :return: The port_stats of this ALLPortStatisticsRespList.  # noqa: E501
        :rtype: list[PortStatistics]
        """
        return self._port_stats

    @port_stats.setter
    def port_stats(self, port_stats):
        """Sets the port_stats of this ALLPortStatisticsRespList.


        :param port_stats: The port_stats of this ALLPortStatisticsRespList.  # noqa: E501
        :type: list[PortStatistics]
        """

        self._port_stats = port_stats

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
        if issubclass(ALLPortStatisticsRespList, dict):
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
        if not isinstance(other, ALLPortStatisticsRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other