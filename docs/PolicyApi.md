# swagger_client.PolicyApi

All URIs are relative to *https://virtserver.swaggerhub.com/kongseokhwan/npb-sdk/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PolicyApi.md#create_policy) | **POST** /tapping/policy | Create NPB Policy
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /tapping/policy/{policy_name} | Delete NPB Policy
[**get_all_policy**](PolicyApi.md#get_all_policy) | **GET** /tapping/policy/all | Get NPB Policy All
[**get_policy**](PolicyApi.md#get_policy) | **GET** /tapping/policy/{policy_name} | Get NPB Policy
[**update_policy**](PolicyApi.md#update_policy) | **PUT** /tapping/policy/{policy_name} | Update NPB Policy


# **create_policy**
> SuccessMessage create_policy(policy_object)

Create NPB Policy

Create NPB Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_object = swagger_client.PolicyObject() # PolicyObject | Policy Object

try:
    # Create NPB Policy
    api_response = api_instance.create_policy(policy_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_object** | [**PolicyObject**](PolicyObject.md)| Policy Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> PolicyName delete_policy(policy_name)

Delete NPB Policy

Delete NPB Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_name = 'policy_name_example' # str | Policy Name

try:
    # Delete NPB Policy
    api_response = api_instance.delete_policy(policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy Name | 

### Return type

[**PolicyName**](PolicyName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policy**
> PolicyRespList get_all_policy()

Get NPB Policy All

Get NPB Policy All

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()

try:
    # Get NPB Policy All
    api_response = api_instance.get_all_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PolicyRespList**](PolicyRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> PolicyResp get_policy(policy_name)

Get NPB Policy

Get NPB Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_name = 'policy_name_example' # str | Policy Name

try:
    # Get NPB Policy
    api_response = api_instance.get_policy(policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy Name | 

### Return type

[**PolicyResp**](PolicyResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> SuccessMessage update_policy(policy_name, policy_object)

Update NPB Policy

Update NPB Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
policy_name = 'policy_name_example' # str | policy name
policy_object = swagger_client.PolicyObject() # PolicyObject | Policy Object

try:
    # Update NPB Policy
    api_response = api_instance.update_policy(policy_name, policy_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| policy name | 
 **policy_object** | [**PolicyObject**](PolicyObject.md)| Policy Object | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

