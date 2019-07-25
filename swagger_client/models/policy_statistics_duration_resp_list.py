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

from swagger_client.models.filter_stats_list import FilterStatsList  # noqa: F401,E501


class PolicyStatisticsDurationRespList(object):
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
        'policy_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'policy_stats': 'FilterStatsList'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'policy_stats': 'policy_stats'
    }

    def __init__(self, policy_name=None, start_time=None, end_time=None, policy_stats=None):  # noqa: E501
        """PolicyStatisticsDurationRespList - a model defined in Swagger"""  # noqa: E501

        self._policy_name = None
        self._start_time = None
        self._end_time = None
        self._policy_stats = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if policy_stats is not None:
            self.policy_stats = policy_stats

    @property
    def policy_name(self):
        """Gets the policy_name of this PolicyStatisticsDurationRespList.  # noqa: E501


        :return: The policy_name of this PolicyStatisticsDurationRespList.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PolicyStatisticsDurationRespList.


        :param policy_name: The policy_name of this PolicyStatisticsDurationRespList.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def start_time(self):
        """Gets the start_time of this PolicyStatisticsDurationRespList.  # noqa: E501


        :return: The start_time of this PolicyStatisticsDurationRespList.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PolicyStatisticsDurationRespList.


        :param start_time: The start_time of this PolicyStatisticsDurationRespList.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PolicyStatisticsDurationRespList.  # noqa: E501


        :return: The end_time of this PolicyStatisticsDurationRespList.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PolicyStatisticsDurationRespList.


        :param end_time: The end_time of this PolicyStatisticsDurationRespList.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def policy_stats(self):
        """Gets the policy_stats of this PolicyStatisticsDurationRespList.  # noqa: E501


        :return: The policy_stats of this PolicyStatisticsDurationRespList.  # noqa: E501
        :rtype: FilterStatsList
        """
        return self._policy_stats

    @policy_stats.setter
    def policy_stats(self, policy_stats):
        """Sets the policy_stats of this PolicyStatisticsDurationRespList.


        :param policy_stats: The policy_stats of this PolicyStatisticsDurationRespList.  # noqa: E501
        :type: FilterStatsList
        """

        self._policy_stats = policy_stats

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
        if issubclass(PolicyStatisticsDurationRespList, dict):
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
        if not isinstance(other, PolicyStatisticsDurationRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
