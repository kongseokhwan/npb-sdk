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
from swagger_client.api.filter_api import FilterApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFilterApi(unittest.TestCase):
    """FilterApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.filter_api.FilterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_filter(self):
        """Test case for create_filter

        Create NPB Filter  # noqa: E501
        """
        pass

    def test_delete_filter(self):
        """Test case for delete_filter

        Delete NPB Filter  # noqa: E501
        """
        pass

    def test_get_all_filter(self):
        """Test case for get_all_filter

        Get NPB Filter All  # noqa: E501
        """
        pass

    def test_get_filter(self):
        """Test case for get_filter

        Get NPB Filter  # noqa: E501
        """
        pass

    def test_update_filter(self):
        """Test case for update_filter

        Update NPB Filter  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
