# swagger_client.FilterApi

All URIs are relative to *https://virtserver.swaggerhub.com/kongseokhwan/npb-sdk/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter**](FilterApi.md#create_filter) | **POST** /tapping/filter/service | Create NPB Filter
[**delete_filter**](FilterApi.md#delete_filter) | **DELETE** /tapping/filter/service/{filter_name} | Delete NPB Filter
[**get_all_filter**](FilterApi.md#get_all_filter) | **GET** /tapping/filter/service/all | Get NPB Filter All
[**get_filter**](FilterApi.md#get_filter) | **GET** /tapping/filter/service/{filter_name} | Get NPB Filter
[**update_filter**](FilterApi.md#update_filter) | **PUT** /tapping/filter/service/{filter_name} | Update NPB Filter


# **create_filter**
> SuccessMessage create_filter(filter_object)

Create NPB Filter

Create NPB Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilterApi()
filter_object = swagger_client.FilterObject() # FilterObject | Filter Object

try:
    # Create NPB Filter
    api_response = api_instance.create_filter(filter_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_object** | [**FilterObject**](FilterObject.md)| Filter Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> FilterName delete_filter(filter_name)

Delete NPB Filter

Delete NPB Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilterApi()
filter_name = 'filter_name_example' # str | Filter Name

try:
    # Delete NPB Filter
    api_response = api_instance.delete_filter(filter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filter Name | 

### Return type

[**FilterName**](FilterName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_filter**
> FilterRespList get_all_filter()

Get NPB Filter All

Get NPB Filter All

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilterApi()

try:
    # Get NPB Filter All
    api_response = api_instance.get_all_filter()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->get_all_filter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilterRespList**](FilterRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter**
> FilterResp get_filter(filter_name)

Get NPB Filter

Get NPB Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilterApi()
filter_name = 'filter_name_example' # str | Filter Name

try:
    # Get NPB Filter
    api_response = api_instance.get_filter(filter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->get_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filter Name | 

### Return type

[**FilterResp**](FilterResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filter**
> SuccessMessage update_filter(filter_name, filter_object)

Update NPB Filter

Update NPB Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilterApi()
filter_name = 'filter_name_example' # str | filter name
filter_object = swagger_client.FilterObject() # FilterObject | Filter Object

try:
    # Update NPB Filter
    api_response = api_instance.update_filter(filter_name, filter_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->update_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| filter name | 
 **filter_object** | [**FilterObject**](FilterObject.md)| Filter Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

