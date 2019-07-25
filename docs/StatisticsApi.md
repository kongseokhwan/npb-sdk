# swagger_client.StatisticsApi

All URIs are relative to *https://virtserver.swaggerhub.com/kongseokhwan/npb-sdk/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_policy_statistics**](StatisticsApi.md#get_all_policy_statistics) | **GET** /tapping/{dpid}/stat/realtime/policy/all | Get NPB Statistics of All Policy
[**get_all_port_statistics**](StatisticsApi.md#get_all_port_statistics) | **GET** /tapping/{dpid}/stat/port/all | Get NPB Statistics of All Port
[**get_enable_all_policy_statistics**](StatisticsApi.md#get_enable_all_policy_statistics) | **GET** /tapping/{dpid}/stat/nonrealtime/{state}/policy/all | Enable NPB Statistics of All Policy
[**get_policy_statistics**](StatisticsApi.md#get_policy_statistics) | **GET** /tapping/{dpid}/stat/realtime/policy/{policy_name} | Get NPB Statistics of Policy
[**get_policy_statistics_duration_nonreal**](StatisticsApi.md#get_policy_statistics_duration_nonreal) | **GET** /tapping/{dpid}/stat/nonrealtime/{start_time}/{end_time}/policy/{policy_name} | Get NPB Non realtime Statistics of Policy
[**get_policy_statistics_nonreal**](StatisticsApi.md#get_policy_statistics_nonreal) | **GET** /tapping/{dpid}/stat/nonrealtime/{time}/policy/{policy_name} | Get NPB Non realtime Statistics of Policy
[**get_port_statistics**](StatisticsApi.md#get_port_statistics) | **GET** /tapping/{dpid}/stat/port/{port_num} | Get NPB Statistics of Port


# **get_all_policy_statistics**
> ALLPolicyStatisticsRespList get_all_policy_statistics(dpid)

Get NPB Statistics of All Policy

Get NPB Statistics of All Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | dpid name

try:
    # Get NPB Statistics of All Policy
    api_response = api_instance.get_all_policy_statistics(dpid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_all_policy_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| dpid name | 

### Return type

[**ALLPolicyStatisticsRespList**](ALLPolicyStatisticsRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_port_statistics**
> ALLPortStatisticsRespList get_all_port_statistics(dpid)

Get NPB Statistics of All Port

Get NPB Statistics of All Port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | dpid name

try:
    # Get NPB Statistics of All Port
    api_response = api_instance.get_all_port_statistics(dpid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_all_port_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| dpid name | 

### Return type

[**ALLPortStatisticsRespList**](ALLPortStatisticsRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enable_all_policy_statistics**
> EnablePolicyStatistics get_enable_all_policy_statistics(dpid, state)

Enable NPB Statistics of All Policy

Enable NPB Statistics of All Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | dpid name
state = 'state_example' # str | state

try:
    # Enable NPB Statistics of All Policy
    api_response = api_instance.get_enable_all_policy_statistics(dpid, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_enable_all_policy_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| dpid name | 
 **state** | **str**| state | 

### Return type

[**EnablePolicyStatistics**](EnablePolicyStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_statistics**
> PolicyStatisticsList get_policy_statistics(dpid, policy_name)

Get NPB Statistics of Policy

Get NPB Statistics of Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | Policy Name
policy_name = 'policy_name_example' # str | Policy Name

try:
    # Get NPB Statistics of Policy
    api_response = api_instance.get_policy_statistics(dpid, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_policy_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| Policy Name | 
 **policy_name** | **str**| Policy Name | 

### Return type

[**PolicyStatisticsList**](PolicyStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_statistics_duration_nonreal**
> PolicyStatisticsDurationRespList get_policy_statistics_duration_nonreal(dpid, start_time, end_time, policy_name)

Get NPB Non realtime Statistics of Policy

Get NPB Non realtime Statistics of Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | dpid name
start_time = 'start_time_example' # str | start_time
end_time = 'end_time_example' # str | end_time
policy_name = 'policy_name_example' # str | policy name

try:
    # Get NPB Non realtime Statistics of Policy
    api_response = api_instance.get_policy_statistics_duration_nonreal(dpid, start_time, end_time, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_policy_statistics_duration_nonreal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| dpid name | 
 **start_time** | **str**| start_time | 
 **end_time** | **str**| end_time | 
 **policy_name** | **str**| policy name | 

### Return type

[**PolicyStatisticsDurationRespList**](PolicyStatisticsDurationRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_statistics_nonreal**
> PolicyStatisticsNonrealRespList get_policy_statistics_nonreal(dpid, time, policy_name)

Get NPB Non realtime Statistics of Policy

Get NPB Non realtime Statistics of Policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | dpid name
time = 'time_example' # str | time
policy_name = 'policy_name_example' # str | policy name

try:
    # Get NPB Non realtime Statistics of Policy
    api_response = api_instance.get_policy_statistics_nonreal(dpid, time, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_policy_statistics_nonreal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| dpid name | 
 **time** | **str**| time | 
 **policy_name** | **str**| policy name | 

### Return type

[**PolicyStatisticsNonrealRespList**](PolicyStatisticsNonrealRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_statistics**
> PortStatisticsRespList get_port_statistics(dpid, port_num)

Get NPB Statistics of Port

Get NPB Statistics of Port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
dpid = 'dpid_example' # str | dpid name
port_num = 'port_num_example' # str | port number

try:
    # Get NPB Statistics of Port
    api_response = api_instance.get_port_statistics(dpid, port_num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_port_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpid** | **str**| dpid name | 
 **port_num** | **str**| port number | 

### Return type

[**PortStatisticsRespList**](PortStatisticsRespList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

