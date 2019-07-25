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


class PolicyStatisticsObject(object):
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
        'filter_name': 'str',
        'pps': 'str',
        'byte_count': 'str',
        'bps': 'str',
        'pkt_count': 'str',
        'aliave': 'str'
    }

    attribute_map = {
        'filter_name': 'filter_name',
        'pps': 'pps',
        'byte_count': 'byte_count',
        'bps': 'bps',
        'pkt_count': 'pkt_count',
        'aliave': 'aliave'
    }

    def __init__(self, filter_name=None, pps=None, byte_count=None, bps=None, pkt_count=None, aliave=None):  # noqa: E501
        """PolicyStatisticsObject - a model defined in Swagger"""  # noqa: E501

        self._filter_name = None
        self._pps = None
        self._byte_count = None
        self._bps = None
        self._pkt_count = None
        self._aliave = None
        self.discriminator = None

        if filter_name is not None:
            self.filter_name = filter_name
        if pps is not None:
            self.pps = pps
        if byte_count is not None:
            self.byte_count = byte_count
        if bps is not None:
            self.bps = bps
        if pkt_count is not None:
            self.pkt_count = pkt_count
        if aliave is not None:
            self.aliave = aliave

    @property
    def filter_name(self):
        """Gets the filter_name of this PolicyStatisticsObject.  # noqa: E501


        :return: The filter_name of this PolicyStatisticsObject.  # noqa: E501
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """Sets the filter_name of this PolicyStatisticsObject.


        :param filter_name: The filter_name of this PolicyStatisticsObject.  # noqa: E501
        :type: str
        """

        self._filter_name = filter_name

    @property
    def pps(self):
        """Gets the pps of this PolicyStatisticsObject.  # noqa: E501


        :return: The pps of this PolicyStatisticsObject.  # noqa: E501
        :rtype: str
        """
        return self._pps

    @pps.setter
    def pps(self, pps):
        """Sets the pps of this PolicyStatisticsObject.


        :param pps: The pps of this PolicyStatisticsObject.  # noqa: E501
        :type: str
        """

        self._pps = pps

    @property
    def byte_count(self):
        """Gets the byte_count of this PolicyStatisticsObject.  # noqa: E501


        :return: The byte_count of this PolicyStatisticsObject.  # noqa: E501
        :rtype: str
        """
        return self._byte_count

    @byte_count.setter
    def byte_count(self, byte_count):
        """Sets the byte_count of this PolicyStatisticsObject.


        :param byte_count: The byte_count of this PolicyStatisticsObject.  # noqa: E501
        :type: str
        """

        self._byte_count = byte_count

    @property
    def bps(self):
        """Gets the bps of this PolicyStatisticsObject.  # noqa: E501


        :return: The bps of this PolicyStatisticsObject.  # noqa: E501
        :rtype: str
        """
        return self._bps

    @bps.setter
    def bps(self, bps):
        """Sets the bps of this PolicyStatisticsObject.


        :param bps: The bps of this PolicyStatisticsObject.  # noqa: E501
        :type: str
        """

        self._bps = bps

    @property
    def pkt_count(self):
        """Gets the pkt_count of this PolicyStatisticsObject.  # noqa: E501


        :return: The pkt_count of this PolicyStatisticsObject.  # noqa: E501
        :rtype: str
        """
        return self._pkt_count

    @pkt_count.setter
    def pkt_count(self, pkt_count):
        """Sets the pkt_count of this PolicyStatisticsObject.


        :param pkt_count: The pkt_count of this PolicyStatisticsObject.  # noqa: E501
        :type: str
        """

        self._pkt_count = pkt_count

    @property
    def aliave(self):
        """Gets the aliave of this PolicyStatisticsObject.  # noqa: E501


        :return: The aliave of this PolicyStatisticsObject.  # noqa: E501
        :rtype: str
        """
        return self._aliave

    @aliave.setter
    def aliave(self, aliave):
        """Sets the aliave of this PolicyStatisticsObject.


        :param aliave: The aliave of this PolicyStatisticsObject.  # noqa: E501
        :type: str
        """

        self._aliave = aliave

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
        if issubclass(PolicyStatisticsObject, dict):
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
        if not isinstance(other, PolicyStatisticsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
