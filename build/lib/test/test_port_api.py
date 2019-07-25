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
from swagger_client.api.port_api import PortApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPortApi(unittest.TestCase):
    """PortApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.port_api.PortApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_portgroup(self):
        """Test case for create_portgroup

        Create NPB Port Group  # noqa: E501
        """
        pass

    def test_delete_portgroup(self):
        """Test case for delete_portgroup

        Delete NPB Port Group  # noqa: E501
        """
        pass

    def test_get_all_port_group(self):
        """Test case for get_all_port_group

        Get NPB All Port Group  # noqa: E501
        """
        pass

    def test_get_port_group(self):
        """Test case for get_port_group

        Get NPB Port Group  # noqa: E501
        """
        pass

    def test_update_port_group(self):
        """Test case for update_port_group

        Update NPB Port Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
