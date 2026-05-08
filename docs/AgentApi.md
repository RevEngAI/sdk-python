# revengai.AgentApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get**](AgentApi.md#check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities/status | Check the status of a capabilities analysis workflow
[**check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get**](AgentApi.md#check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis/status | Check the status of a report analysis workflow
[**check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get**](AgentApi.md#check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get) | **GET** /v2/analyses/{analysis_id}/agent/triage/status | Check the status of a triage analysis workflow
[**create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post**](AgentApi.md#create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post) | **POST** /v2/analyses/{analysis_id}/agent/capabilities | Queues a capabilities analysis workflow process
[**create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post**](AgentApi.md#create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post) | **POST** /v2/analyses/{analysis_id}/agent/report-analysis | Queues a combined report analysis workflow process
[**create_triage_task_v2_analyses_analysis_id_agent_triage_post**](AgentApi.md#create_triage_task_v2_analyses_analysis_id_agent_triage_post) | **POST** /v2/analyses/{analysis_id}/agent/triage | Queues a triage analysis workflow process
[**get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get**](AgentApi.md#get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities | Get Capabilities Result
[**get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get**](AgentApi.md#get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis | Get Report Analysis Result
[**get_triage_result_v2_analyses_analysis_id_agent_triage_get**](AgentApi.md#get_triage_result_v2_analyses_analysis_id_agent_triage_get) | **GET** /v2/analyses/{analysis_id}/agent/triage | Get Triage Result


# **check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get**
> TaskStatusResponse check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get(analysis_id)

Check the status of a capabilities analysis workflow

### Example

* Api Key Authentication (APIKey):

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

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

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

