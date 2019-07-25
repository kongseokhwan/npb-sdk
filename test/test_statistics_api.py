# coding: utf-8

"""
    PRISM NBAPI

    This is a PRISM NBAPI API Client module.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@kulcloud.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.statistics_api import StatisticsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.statistics_api.StatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_policy_statistics(self):
        """Test case for get_all_policy_statistics

        Get NPB Statistics of All Policy  # noqa: E501
        """
        pass

    def test_get_all_port_statistics(self):
        """Test case for get_all_port_statistics

        Get NPB Statistics of All Port  # noqa: E501
        """
        pass

    def test_get_enable_all_policy_statistics(self):
        """Test case for get_enable_all_policy_statistics

        Enable NPB Statistics of All Policy  # noqa: E501
        """
        pass

    def test_get_policy_statistics(self):
        """Test case for get_policy_statistics

        Get NPB Statistics of Policy  # noqa: E501
        """
        pass

    def test_get_policy_statistics_duration_nonreal(self):
        """Test case for get_policy_statistics_duration_nonreal

        Get NPB Non realtime Statistics of Policy  # noqa: E501
        """
        pass

    def test_get_policy_statistics_nonreal(self):
        """Test case for get_policy_statistics_nonreal

        Get NPB Non realtime Statistics of Policy  # noqa: E501
        """
        pass

    def test_get_port_statistics(self):
        """Test case for get_port_statistics

        Get NPB Statistics of Port  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()