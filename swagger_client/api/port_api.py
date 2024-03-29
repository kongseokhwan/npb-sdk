# coding: utf-8

"""
    PRISM NBAPI

    This is a PRISM NBAPI API Client module.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@kulcloud.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PortApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_portgroup(self, portgroup_object, **kwargs):  # noqa: E501
        """Create NPB Port Group  # noqa: E501

        Create NPB Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portgroup(portgroup_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortgroupObject portgroup_object: Port Group Object (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_portgroup_with_http_info(portgroup_object, **kwargs)  # noqa: E501
        else:
            (data) = self.create_portgroup_with_http_info(portgroup_object, **kwargs)  # noqa: E501
            return data

    def create_portgroup_with_http_info(self, portgroup_object, **kwargs):  # noqa: E501
        """Create NPB Port Group  # noqa: E501

        Create NPB Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portgroup_with_http_info(portgroup_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortgroupObject portgroup_object: Port Group Object (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['portgroup_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_portgroup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'portgroup_object' is set
        if ('portgroup_object' not in params or
                params['portgroup_object'] is None):
            raise ValueError("Missing the required parameter `portgroup_object` when calling `create_portgroup`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'portgroup_object' in params:
            body_params = params['portgroup_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tapping/port/group', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_portgroup(self, group_name, **kwargs):  # noqa: E501
        """Delete NPB Port Group  # noqa: E501

        지정된 이름의 포트 그룹 삭제.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_portgroup(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: 삭제할 포트 그그룹 이름 (required)
        :return: PortGroupName
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_portgroup_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_portgroup_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def delete_portgroup_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Delete NPB Port Group  # noqa: E501

        지정된 이름의 포트 그룹 삭제.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_portgroup_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: 삭제할 포트 그그룹 이름 (required)
        :return: PortGroupName
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_portgroup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `delete_portgroup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tapping/port/{group_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortGroupName',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_port_group(self, **kwargs):  # noqa: E501
        """Get NPB All Port Group  # noqa: E501

        Get NPB All Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_port_group(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetGroupsObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_port_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_port_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_port_group_with_http_info(self, **kwargs):  # noqa: E501
        """Get NPB All Port Group  # noqa: E501

        Get NPB All Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_port_group_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetGroupsObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_port_group" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tapping/port/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetGroupsObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_port_group(self, group_name, **kwargs):  # noqa: E501
        """Get NPB Port Group  # noqa: E501

        Get NPB Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_port_group(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: 삭제할 포트 그룸 이름 (required)
        :return: GetGroupObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_port_group_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_port_group_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def get_port_group_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Get NPB Port Group  # noqa: E501

        Get NPB Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_port_group_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: 삭제할 포트 그룸 이름 (required)
        :return: GetGroupObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_port_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `get_port_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tapping/port/{group_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetGroupObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_port_group(self, group_name, portgroup_object, **kwargs):  # noqa: E501
        """Update NPB Port Group  # noqa: E501

        Update NPB Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_port_group(group_name, portgroup_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: group name (required)
        :param PortgroupObject portgroup_object: Port Group Object (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_port_group_with_http_info(group_name, portgroup_object, **kwargs)  # noqa: E501
        else:
            (data) = self.update_port_group_with_http_info(group_name, portgroup_object, **kwargs)  # noqa: E501
            return data

    def update_port_group_with_http_info(self, group_name, portgroup_object, **kwargs):  # noqa: E501
        """Update NPB Port Group  # noqa: E501

        Update NPB Port Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_port_group_with_http_info(group_name, portgroup_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: group name (required)
        :param PortgroupObject portgroup_object: Port Group Object (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'portgroup_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_port_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `update_port_group`")  # noqa: E501
        # verify the required parameter 'portgroup_object' is set
        if ('portgroup_object' not in params or
                params['portgroup_object'] is None):
            raise ValueError("Missing the required parameter `portgroup_object` when calling `update_port_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'portgroup_object' in params:
            body_params = params['portgroup_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tapping/port/group/{group_name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
