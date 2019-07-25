# swagger_client.RatelimitApi

All URIs are relative to *https://virtserver.swaggerhub.com/kongseokhwan/npb-sdk/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate_limit**](RatelimitApi.md#create_rate_limit) | **POST** /tapping/rate/limit | Create NPB Rate Limit
[**delete_rate_limit**](RatelimitApi.md#delete_rate_limit) | **DELETE** /tapping/rate/limit/{limit_name} | Delete NPB Rate Limit
[**get_all_rate_limit**](RatelimitApi.md#get_all_rate_limit) | **GET** /tapping/rate/limit/all | Get NPB Rate Limit All
[**get_rate_limit**](RatelimitApi.md#get_rate_limit) | **GET** /tapping/rate/limit/{limit_name} | Get NPB Rate Limit
[**update_rate_limit**](RatelimitApi.md#update_rate_limit) | **PUT** /tapping/rate/limit/{limit_name} | Update NPB Rate Limit


# **create_rate_limit**
> SuccessMessage create_rate_limit(rate_limit_object)

Create NPB Rate Limit

Create NPB Rate Limit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RatelimitApi()
rate_limit_object = swagger_client.RateLimitObject() # RateLimitObject | Port Group Object

try:
    # Create NPB Rate Limit
    api_response = api_instance.create_rate_limit(rate_limit_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatelimitApi->create_rate_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limit_object** | [**RateLimitObject**](RateLimitObject.md)| Port Group Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rate_limit**
> RateLimitName delete_rate_limit(limit_name)

Delete NPB Rate Limit

Delete NPB Rate Limit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RatelimitApi()
limit_name = 'limit_name_example' # str | Rate Limit Name

try:
    # Delete NPB Rate Limit
    api_response = api_instance.delete_rate_limit(limit_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatelimitApi->delete_rate_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_name** | **str**| Rate Limit Name | 

### Return type

[**RateLimitName**](RateLimitName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rate_limit**
> RateLimitRespList get_all_rate_limit()

Get NPB Rate Limit All

Get NPB Rate Limit All

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RatelimitApi()

try:
    # Get NPB Rate Limit All
    api_response = api_instance.get_all_rate_limit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatelimitApi->get_all_rate_limit: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RateLimitRespList**](RateLimitRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_limit**
> RateLimitResp get_rate_limit(limit_name)

Get NPB Rate Limit

Get NPB Rate Limit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RatelimitApi()
limit_name = 'limit_name_example' # str | Rate Limit Name

try:
    # Get NPB Rate Limit
    api_response = api_instance.get_rate_limit(limit_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatelimitApi->get_rate_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_name** | **str**| Rate Limit Name | 

### Return type

[**RateLimitResp**](RateLimitResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rate_limit**
> SuccessMessage update_rate_limit(limit_name, rate_limit_object)

Update NPB Rate Limit

Update NPB Rate Limit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RatelimitApi()
limit_name = 'limit_name_example' # str | limit name
rate_limit_object = swagger_client.RateLimitObject() # RateLimitObject | Rate Limit Object

try:
    # Update NPB Rate Limit
    api_response = api_instance.update_rate_limit(limit_name, rate_limit_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatelimitApi->update_rate_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_name** | **str**| limit name | 
 **rate_limit_object** | [**RateLimitObject**](RateLimitObject.md)| Rate Limit Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

