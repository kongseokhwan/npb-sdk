# swagger_client.PortApi

All URIs are relative to *https://virtserver.swaggerhub.com/kongseokhwan/npb-sdk/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_portgroup**](PortApi.md#create_portgroup) | **POST** /tapping/port/group | Create NPB Port Group
[**delete_portgroup**](PortApi.md#delete_portgroup) | **DELETE** /tapping/port/{group_name} | Delete NPB Port Group
[**get_all_port_group**](PortApi.md#get_all_port_group) | **GET** /tapping/port/all | Get NPB All Port Group
[**get_port_group**](PortApi.md#get_port_group) | **GET** /tapping/port/{group_name} | Get NPB Port Group
[**update_port_group**](PortApi.md#update_port_group) | **PUT** /tapping/port/group/{group_name} | Update NPB Port Group


# **create_portgroup**
> SuccessMessage create_portgroup(portgroup_object)

Create NPB Port Group

Create NPB Port Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortApi()
portgroup_object = swagger_client.PortgroupObject() # PortgroupObject | Port Group Object

try:
    # Create NPB Port Group
    api_response = api_instance.create_portgroup(portgroup_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortApi->create_portgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portgroup_object** | [**PortgroupObject**](PortgroupObject.md)| Port Group Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portgroup**
> PortGroupName delete_portgroup(group_name)

Delete NPB Port Group

지정된 이름의 포트 그룹 삭제.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortApi()
group_name = 'group_name_example' # str | 삭제할 포트 그그룹 이름

try:
    # Delete NPB Port Group
    api_response = api_instance.delete_portgroup(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortApi->delete_portgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| 삭제할 포트 그그룹 이름 | 

### Return type

[**PortGroupName**](PortGroupName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_port_group**
> GetGroupsObject get_all_port_group()

Get NPB All Port Group

Get NPB All Port Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortApi()

try:
    # Get NPB All Port Group
    api_response = api_instance.get_all_port_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortApi->get_all_port_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetGroupsObject**](GetGroupsObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_group**
> GetGroupObject get_port_group(group_name)

Get NPB Port Group

Get NPB Port Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortApi()
group_name = 'group_name_example' # str | 삭제할 포트 그룸 이름

try:
    # Get NPB Port Group
    api_response = api_instance.get_port_group(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortApi->get_port_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| 삭제할 포트 그룸 이름 | 

### Return type

[**GetGroupObject**](GetGroupObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_port_group**
> SuccessMessage update_port_group(group_name, portgroup_object)

Update NPB Port Group

Update NPB Port Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortApi()
group_name = 'group_name_example' # str | group name
portgroup_object = swagger_client.PortgroupObject() # PortgroupObject | Port Group Object

try:
    # Update NPB Port Group
    api_response = api_instance.update_port_group(group_name, portgroup_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortApi->update_port_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| group name | 
 **portgroup_object** | [**PortgroupObject**](PortgroupObject.md)| Port Group Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

