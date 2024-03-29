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

from swagger_client.models.filter_stats_object import FilterStatsObject  # noqa: F401,E501


class FilterStatsList(object):
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
        'filter_stats': 'list[FilterStatsObject]'
    }

    attribute_map = {
        'filter_stats': 'filter_stats'
    }

    def __init__(self, filter_stats=None):  # noqa: E501
        """FilterStatsList - a model defined in Swagger"""  # noqa: E501

        self._filter_stats = None
        self.discriminator = None

        if filter_stats is not None:
            self.filter_stats = filter_stats

    @property
    def filter_stats(self):
        """Gets the filter_stats of this FilterStatsList.  # noqa: E501


        :return: The filter_stats of this FilterStatsList.  # noqa: E501
        :rtype: list[FilterStatsObject]
        """
        return self._filter_stats

    @filter_stats.setter
    def filter_stats(self, filter_stats):
        """Sets the filter_stats of this FilterStatsList.


        :param filter_stats: The filter_stats of this FilterStatsList.  # noqa: E501
        :type: list[FilterStatsObject]
        """

        self._filter_stats = filter_stats

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
        if issubclass(FilterStatsList, dict):
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
        if not isinstance(other, FilterStatsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
