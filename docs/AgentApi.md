# revengai.AgentApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get**](AgentApi.md#check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities/status | Check the status of a capabilities analysis workflow
[**check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get**](AgentApi.md#check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get) | **GET** /v2/analyses/{analysis_id}/agent/remediation/status | Check the status of a remediation analysis workflow
[**check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get**](AgentApi.md#check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis/status | Check the status of a report analysis workflow
[**check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get**](AgentApi.md#check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get) | **GET** /v2/analyses/{analysis_id}/agent/triage/status | Check the status of a triage analysis workflow
[**create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post**](AgentApi.md#create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post) | **POST** /v2/analyses/{analysis_id}/agent/capabilities | Queues a capabilities analysis workflow process
[**create_remediation_task_v2_analyses_analysis_id_agent_remediation_post**](AgentApi.md#create_remediation_task_v2_analyses_analysis_id_agent_remediation_post) | **POST** /v2/analyses/{analysis_id}/agent/remediation | Queues a remediation analysis workflow process
[**create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post**](AgentApi.md#create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post) | **POST** /v2/analyses/{analysis_id}/agent/report-analysis | Queues a combined report analysis workflow process
[**create_triage_task_v2_analyses_analysis_id_agent_triage_post**](AgentApi.md#create_triage_task_v2_analyses_analysis_id_agent_triage_post) | **POST** /v2/analyses/{analysis_id}/agent/triage | Queues a triage analysis workflow process
[**get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get**](AgentApi.md#get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities | Get Capabilities Result
[**get_remediation_result_v2_analyses_analysis_id_agent_remediation_get**](AgentApi.md#get_remediation_result_v2_analyses_analysis_id_agent_remediation_get) | **GET** /v2/analyses/{analysis_id}/agent/remediation | Get Remediation Result
[**get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get**](AgentApi.md#get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis | Get Report Analysis Result
[**get_triage_result_v2_analyses_analysis_id_agent_triage_get**](AgentApi.md#get_triage_result_v2_analyses_analysis_id_agent_triage_get) | **GET** /v2/analyses/{analysis_id}/agent/triage | Get Triage Result
[**v3_cancel_rename_unnamed_functions**](AgentApi.md#v3_cancel_rename_unnamed_functions) | **POST** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions/cancel | Cancel the rename-unnamed-functions agent.
[**v3_get_rename_unnamed_functions_result**](AgentApi.md#v3_get_rename_unnamed_functions_result) | **GET** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions | Get rename-unnamed-functions agent result.
[**v3_get_rename_unnamed_functions_status**](AgentApi.md#v3_get_rename_unnamed_functions_status) | **GET** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions/status | Get rename-unnamed-functions agent status.
[**v3_trigger_rename_unnamed_functions**](AgentApi.md#v3_trigger_rename_unnamed_functions) | **POST** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions | Run the rename-unnamed-functions agent.


# **check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get**
> TaskStatusResponse check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get(analysis_id)

Check the status of a capabilities analysis workflow

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.task_status_response import TaskStatusResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Check the status of a capabilities analysis workflow
        api_response = api_instance.check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get(analysis_id)
        print("The response of AgentApi->check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get**
> TaskStatusResponse check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get(analysis_id)

Check the status of a remediation analysis workflow

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.task_status_response import TaskStatusResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Check the status of a remediation analysis workflow
        api_response = api_instance.check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get(analysis_id)
        print("The response of AgentApi->check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get**
> TaskStatusResponse check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get(analysis_id)

Check the status of a report analysis workflow

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.task_status_response import TaskStatusResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Check the status of a report analysis workflow
        api_response = api_instance.check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get(analysis_id)
        print("The response of AgentApi->check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get**
> TaskStatusResponse check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get(analysis_id)

Check the status of a triage analysis workflow

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.task_status_response import TaskStatusResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Check the status of a triage analysis workflow
        api_response = api_instance.check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get(analysis_id)
        print("The response of AgentApi->check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post**
> BaseResponseQueuedWorkflowTaskResponse create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post(analysis_id)

Queues a capabilities analysis workflow process

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_queued_workflow_task_response import BaseResponseQueuedWorkflowTaskResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Queues a capabilities analysis workflow process
        api_response = api_instance.create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post(analysis_id)
        print("The response of AgentApi->create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseQueuedWorkflowTaskResponse**](BaseResponseQueuedWorkflowTaskResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_remediation_task_v2_analyses_analysis_id_agent_remediation_post**
> BaseResponseQueuedWorkflowTaskResponse create_remediation_task_v2_analyses_analysis_id_agent_remediation_post(analysis_id)

Queues a remediation analysis workflow process

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_queued_workflow_task_response import BaseResponseQueuedWorkflowTaskResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Queues a remediation analysis workflow process
        api_response = api_instance.create_remediation_task_v2_analyses_analysis_id_agent_remediation_post(analysis_id)
        print("The response of AgentApi->create_remediation_task_v2_analyses_analysis_id_agent_remediation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_remediation_task_v2_analyses_analysis_id_agent_remediation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseQueuedWorkflowTaskResponse**](BaseResponseQueuedWorkflowTaskResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post**
> QueuedWorkflowTaskResponse create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post(analysis_id)

Queues a combined report analysis workflow process

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.queued_workflow_task_response import QueuedWorkflowTaskResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Queues a combined report analysis workflow process
        api_response = api_instance.create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post(analysis_id)
        print("The response of AgentApi->create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**QueuedWorkflowTaskResponse**](QueuedWorkflowTaskResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |
**409** | Task already completed or queued |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_triage_task_v2_analyses_analysis_id_agent_triage_post**
> BaseResponseQueuedWorkflowTaskResponse create_triage_task_v2_analyses_analysis_id_agent_triage_post(analysis_id)

Queues a triage analysis workflow process

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_queued_workflow_task_response import BaseResponseQueuedWorkflowTaskResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Queues a triage analysis workflow process
        api_response = api_instance.create_triage_task_v2_analyses_analysis_id_agent_triage_post(analysis_id)
        print("The response of AgentApi->create_triage_task_v2_analyses_analysis_id_agent_triage_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_triage_task_v2_analyses_analysis_id_agent_triage_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseQueuedWorkflowTaskResponse**](BaseResponseQueuedWorkflowTaskResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get**
> BaseResponseCapabilitiesAgentResponse get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get(analysis_id)

Get Capabilities Result

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_capabilities_agent_response import BaseResponseCapabilitiesAgentResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Capabilities Result
        api_response = api_instance.get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get(analysis_id)
        print("The response of AgentApi->get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseCapabilitiesAgentResponse**](BaseResponseCapabilitiesAgentResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remediation_result_v2_analyses_analysis_id_agent_remediation_get**
> BaseResponseRemediationAgentResponse get_remediation_result_v2_analyses_analysis_id_agent_remediation_get(analysis_id)

Get Remediation Result

Returns:
- A list of generated YARA rules
- A list of generated Snort rules
- A list of generated STIX rules

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_remediation_agent_response import BaseResponseRemediationAgentResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Remediation Result
        api_response = api_instance.get_remediation_result_v2_analyses_analysis_id_agent_remediation_get(analysis_id)
        print("The response of AgentApi->get_remediation_result_v2_analyses_analysis_id_agent_remediation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_remediation_result_v2_analyses_analysis_id_agent_remediation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseRemediationAgentResponse**](BaseResponseRemediationAgentResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get**
> BaseResponseReportAnalysisResponse get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get(analysis_id)

Get Report Analysis Result

Returns:
- A summary of the analysis
- The software type of the binary
- An attack flow summary
- List of IOCs
- List of MITRE executable techniques
- A YARA rule

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_report_analysis_response import BaseResponseReportAnalysisResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Report Analysis Result
        api_response = api_instance.get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get(analysis_id)
        print("The response of AgentApi->get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseReportAnalysisResponse**](BaseResponseReportAnalysisResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_triage_result_v2_analyses_analysis_id_agent_triage_get**
> BaseResponseTriageReportResponse get_triage_result_v2_analyses_analysis_id_agent_triage_get(analysis_id)

Get Triage Result

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_triage_report_response import BaseResponseTriageReportResponse
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Triage Result
        api_response = api_instance.get_triage_result_v2_analyses_analysis_id_agent_triage_get(analysis_id)
        print("The response of AgentApi->get_triage_result_v2_analyses_analysis_id_agent_triage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_triage_result_v2_analyses_analysis_id_agent_triage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseTriageReportResponse**](BaseResponseTriageReportResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cancel_rename_unnamed_functions**
> v3_cancel_rename_unnamed_functions(analysis_id)

Cancel the rename-unnamed-functions agent.

Requests cancellation of the currently running rename-unnamed-functions run for the analysis. Returns 404 if no run is in progress.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NO_ACTIVE_RUN`](/errors/NO_ACTIVE_RUN) — No Active Run

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Cancel the rename-unnamed-functions agent.
        api_instance.v3_cancel_rename_unnamed_functions(analysis_id)
    except Exception as e:
        print("Exception when calling AgentApi->v3_cancel_rename_unnamed_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_rename_unnamed_functions_result**
> RenameUnnamedFunctionsResult v3_get_rename_unnamed_functions_result(analysis_id)

Get rename-unnamed-functions agent result.

Returns the summary of the most recent completed rename-unnamed-functions run. Returns 409 while a run is still in progress and 404 when the agent has never produced a result for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.rename_unnamed_functions_result import RenameUnnamedFunctionsResult
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get rename-unnamed-functions agent result.
        api_response = api_instance.v3_get_rename_unnamed_functions_result(analysis_id)
        print("The response of AgentApi->v3_get_rename_unnamed_functions_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_rename_unnamed_functions_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**RenameUnnamedFunctionsResult**](RenameUnnamedFunctionsResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_rename_unnamed_functions_status**
> StatusBody v3_get_rename_unnamed_functions_status(analysis_id)

Get rename-unnamed-functions agent status.

Returns the status of the most recent rename-unnamed-functions run for the analysis. `UNINITIALISED` means the agent has never been triggered, so it is safe to start one.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.status_body import StatusBody
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get rename-unnamed-functions agent status.
        api_response = api_instance.v3_get_rename_unnamed_functions_status(analysis_id)
        print("The response of AgentApi->v3_get_rename_unnamed_functions_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_rename_unnamed_functions_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**StatusBody**](StatusBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_trigger_rename_unnamed_functions**
> StatusBody v3_trigger_rename_unnamed_functions(analysis_id, trigger_rename_unnamed_functions_input_body)

Run the rename-unnamed-functions agent.

Starts an agent that renames the analysis' unnamed functions from their AI decompilations. Each function costs an AI decompilation, so a whole-analysis run can be expensive — use `limit` to bound it. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.status_body import StatusBody
from revengai.models.trigger_rename_unnamed_functions_input_body import TriggerRenameUnnamedFunctionsInputBody
from revengai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.reveng.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = revengai.Configuration(
    host = "https://api.reveng.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AgentApi(api_client)
    analysis_id = 56 # int | Analysis ID
    trigger_rename_unnamed_functions_input_body = revengai.TriggerRenameUnnamedFunctionsInputBody() # TriggerRenameUnnamedFunctionsInputBody | 

    try:
        # Run the rename-unnamed-functions agent.
        api_response = api_instance.v3_trigger_rename_unnamed_functions(analysis_id, trigger_rename_unnamed_functions_input_body)
        print("The response of AgentApi->v3_trigger_rename_unnamed_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_trigger_rename_unnamed_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **trigger_rename_unnamed_functions_input_body** | [**TriggerRenameUnnamedFunctionsInputBody**](TriggerRenameUnnamedFunctionsInputBody.md)|  | 

### Return type

[**StatusBody**](StatusBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

