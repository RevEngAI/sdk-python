# revengai.AgentApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get**](AgentApi.md#check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities/status | Check the status of a capabilities analysis workflow
[**check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get**](AgentApi.md#check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get) | **GET** /v2/analyses/{analysis_id}/agent/protocols/status | Check the status of a protocols discovery workflow
[**check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get**](AgentApi.md#check_remediation_task_status_v2_analyses_analysis_id_agent_remediation_status_get) | **GET** /v2/analyses/{analysis_id}/agent/remediation/status | Check the status of a remediation analysis workflow
[**check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get**](AgentApi.md#check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis/status | Check the status of a report analysis workflow
[**check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get**](AgentApi.md#check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get) | **GET** /v2/analyses/{analysis_id}/agent/secrets/status | Check the status of a secrets discovery workflow
[**check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get**](AgentApi.md#check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get) | **GET** /v2/analyses/{analysis_id}/agent/triage/status | Check the status of a triage analysis workflow
[**create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post**](AgentApi.md#create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post) | **POST** /v2/analyses/{analysis_id}/agent/capabilities | Queues a capabilities analysis workflow process
[**create_protocols_task_v2_analyses_analysis_id_agent_protocols_post**](AgentApi.md#create_protocols_task_v2_analyses_analysis_id_agent_protocols_post) | **POST** /v2/analyses/{analysis_id}/agent/protocols | Queues a protocols discovery workflow process
[**create_remediation_task_v2_analyses_analysis_id_agent_remediation_post**](AgentApi.md#create_remediation_task_v2_analyses_analysis_id_agent_remediation_post) | **POST** /v2/analyses/{analysis_id}/agent/remediation | Queues a remediation analysis workflow process
[**create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post**](AgentApi.md#create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post) | **POST** /v2/analyses/{analysis_id}/agent/report-analysis | Queues a combined report analysis workflow process
[**create_secrets_task_v2_analyses_analysis_id_agent_secrets_post**](AgentApi.md#create_secrets_task_v2_analyses_analysis_id_agent_secrets_post) | **POST** /v2/analyses/{analysis_id}/agent/secrets | Queues a secrets discovery workflow process
[**create_triage_task_v2_analyses_analysis_id_agent_triage_post**](AgentApi.md#create_triage_task_v2_analyses_analysis_id_agent_triage_post) | **POST** /v2/analyses/{analysis_id}/agent/triage | Queues a triage analysis workflow process
[**get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get**](AgentApi.md#get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities | Get Capabilities Result
[**get_protocols_result_v2_analyses_analysis_id_agent_protocols_get**](AgentApi.md#get_protocols_result_v2_analyses_analysis_id_agent_protocols_get) | **GET** /v2/analyses/{analysis_id}/agent/protocols | Get Protocols Result
[**get_remediation_result_v2_analyses_analysis_id_agent_remediation_get**](AgentApi.md#get_remediation_result_v2_analyses_analysis_id_agent_remediation_get) | **GET** /v2/analyses/{analysis_id}/agent/remediation | Get Remediation Result
[**get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get**](AgentApi.md#get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis | Get Report Analysis Result
[**get_secrets_result_v2_analyses_analysis_id_agent_secrets_get**](AgentApi.md#get_secrets_result_v2_analyses_analysis_id_agent_secrets_get) | **GET** /v2/analyses/{analysis_id}/agent/secrets | Get Secrets Result
[**get_triage_result_v2_analyses_analysis_id_agent_triage_get**](AgentApi.md#get_triage_result_v2_analyses_analysis_id_agent_triage_get) | **GET** /v2/analyses/{analysis_id}/agent/triage | Get Triage Result
[**v3_cancel_rename_unnamed_functions**](AgentApi.md#v3_cancel_rename_unnamed_functions) | **POST** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions/cancel | Cancel the rename-unnamed-functions agent.
[**v3_cancel_security_scan_operation**](AgentApi.md#v3_cancel_security_scan_operation) | **POST** /v3/operations/security-scan/{analysis_id}:cancel | Cancel a security-scan operation.
[**v3_get_binary_agent_feedback**](AgentApi.md#v3_get_binary_agent_feedback) | **GET** /v3/analyses/{analysis_id}/agents/{agent}/feedback | Get the caller&#39;s feedback on an agent&#39;s output.
[**v3_get_capabilities_operation**](AgentApi.md#v3_get_capabilities_operation) | **GET** /v3/operations/capabilities/{analysis_id} | Get a capabilities operation.
[**v3_get_crypto_explain_operation**](AgentApi.md#v3_get_crypto_explain_operation) | **GET** /v3/operations/crypto-explain/{function_id} | Get a crypto-explain operation.
[**v3_get_crypto_scan_operation**](AgentApi.md#v3_get_crypto_scan_operation) | **GET** /v3/operations/crypto-scan/{analysis_id} | Get a crypto-scan operation.
[**v3_get_execution_explain_operation**](AgentApi.md#v3_get_execution_explain_operation) | **GET** /v3/operations/execution-explain/{function_id} | Get an execution-explain operation.
[**v3_get_execution_scan_operation**](AgentApi.md#v3_get_execution_scan_operation) | **GET** /v3/operations/execution-scan/{analysis_id} | Get an execution-scan operation.
[**v3_get_filesystem_analyse_operation**](AgentApi.md#v3_get_filesystem_analyse_operation) | **GET** /v3/operations/filesystem-analyse/{function_id} | Get a filesystem-analyse operation.
[**v3_get_filesystem_scan_operation**](AgentApi.md#v3_get_filesystem_scan_operation) | **GET** /v3/operations/filesystem-scan/{analysis_id} | Get a filesystem-scan operation.
[**v3_get_networking_explain_operation**](AgentApi.md#v3_get_networking_explain_operation) | **GET** /v3/operations/networking-explain/{function_id} | Get a networking-explain operation.
[**v3_get_networking_scan_operation**](AgentApi.md#v3_get_networking_scan_operation) | **GET** /v3/operations/networking-scan/{analysis_id} | Get a networking-scan operation.
[**v3_get_protocols_operation**](AgentApi.md#v3_get_protocols_operation) | **GET** /v3/operations/protocols/{analysis_id} | Get a protocols operation.
[**v3_get_remediation_operation**](AgentApi.md#v3_get_remediation_operation) | **GET** /v3/operations/remediation/{analysis_id} | Get a remediation operation.
[**v3_get_rename_unnamed_functions_result**](AgentApi.md#v3_get_rename_unnamed_functions_result) | **GET** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions | Get rename-unnamed-functions agent result.
[**v3_get_rename_unnamed_functions_status**](AgentApi.md#v3_get_rename_unnamed_functions_status) | **GET** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions/status | Get rename-unnamed-functions agent status.
[**v3_get_report_analysis_operation**](AgentApi.md#v3_get_report_analysis_operation) | **GET** /v3/operations/report-analysis/{analysis_id} | Get a report-analysis operation.
[**v3_get_secrets_operation**](AgentApi.md#v3_get_secrets_operation) | **GET** /v3/operations/secrets/{analysis_id} | Get a secrets operation.
[**v3_get_security_scan_operation**](AgentApi.md#v3_get_security_scan_operation) | **GET** /v3/operations/security-scan/{analysis_id} | Get a security-scan operation.
[**v3_get_triage_operation**](AgentApi.md#v3_get_triage_operation) | **GET** /v3/operations/triage/{analysis_id} | Get a triage operation.
[**v3_run_capabilities**](AgentApi.md#v3_run_capabilities) | **POST** /v3/analyses/{analysis_id}/capabilities:run | Run the capabilities agent.
[**v3_run_crypto_explain**](AgentApi.md#v3_run_crypto_explain) | **POST** /v3/functions/{function_id}/crypto-explain:run | Run the crypto-explain agent.
[**v3_run_crypto_scan**](AgentApi.md#v3_run_crypto_scan) | **POST** /v3/analyses/{analysis_id}/crypto-scan:run | Run the crypto-scan agent.
[**v3_run_execution_explain**](AgentApi.md#v3_run_execution_explain) | **POST** /v3/functions/{function_id}/execution-explain:run | Run the execution-explain agent.
[**v3_run_execution_scan**](AgentApi.md#v3_run_execution_scan) | **POST** /v3/analyses/{analysis_id}/execution-scan:run | Run the execution-scan agent.
[**v3_run_filesystem_analyse**](AgentApi.md#v3_run_filesystem_analyse) | **POST** /v3/functions/{function_id}/filesystem-analyse:run | Run the filesystem-analyse agent.
[**v3_run_filesystem_scan**](AgentApi.md#v3_run_filesystem_scan) | **POST** /v3/analyses/{analysis_id}/filesystem-scan:run | Run the filesystem-scan agent.
[**v3_run_networking_explain**](AgentApi.md#v3_run_networking_explain) | **POST** /v3/functions/{function_id}/networking-explain:run | Run the networking-explain agent.
[**v3_run_networking_scan**](AgentApi.md#v3_run_networking_scan) | **POST** /v3/analyses/{analysis_id}/networking-scan:run | Run the networking-scan agent.
[**v3_run_protocols**](AgentApi.md#v3_run_protocols) | **POST** /v3/analyses/{analysis_id}/protocols:run | Run the protocols agent.
[**v3_run_remediation**](AgentApi.md#v3_run_remediation) | **POST** /v3/analyses/{analysis_id}/remediation:run | Run the remediation agent.
[**v3_run_report_analysis**](AgentApi.md#v3_run_report_analysis) | **POST** /v3/analyses/{analysis_id}/report-analysis:run | Run the report-analysis agent.
[**v3_run_secrets**](AgentApi.md#v3_run_secrets) | **POST** /v3/analyses/{analysis_id}/secrets:run | Run the secrets agent.
[**v3_run_security_scan**](AgentApi.md#v3_run_security_scan) | **POST** /v3/analyses/{analysis_id}/security-scan:run | Run the security-scan agent.
[**v3_run_triage**](AgentApi.md#v3_run_triage) | **POST** /v3/analyses/{analysis_id}/triage:run | Run the triage agent.
[**v3_trigger_rename_unnamed_functions**](AgentApi.md#v3_trigger_rename_unnamed_functions) | **POST** /v3/analyses/{analysis_id}/agents/rename-unnamed-functions | Run the rename-unnamed-functions agent.
[**v3_upsert_binary_agent_feedback**](AgentApi.md#v3_upsert_binary_agent_feedback) | **PUT** /v3/analyses/{analysis_id}/agents/{agent}/feedback | Record feedback on an agent&#39;s output.


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

# **check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get**
> TaskStatusResponse check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get(analysis_id)

Check the status of a protocols discovery workflow

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
        # Check the status of a protocols discovery workflow
        api_response = api_instance.check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get(analysis_id)
        print("The response of AgentApi->check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->check_protocols_task_status_v2_analyses_analysis_id_agent_protocols_status_get: %s\n" % e)
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

# **check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get**
> TaskStatusResponse check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get(analysis_id)

Check the status of a secrets discovery workflow

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
        # Check the status of a secrets discovery workflow
        api_response = api_instance.check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get(analysis_id)
        print("The response of AgentApi->check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->check_secrets_task_status_v2_analyses_analysis_id_agent_secrets_status_get: %s\n" % e)
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

# **create_protocols_task_v2_analyses_analysis_id_agent_protocols_post**
> BaseResponseQueuedWorkflowTaskResponse create_protocols_task_v2_analyses_analysis_id_agent_protocols_post(analysis_id)

Queues a protocols discovery workflow process

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
        # Queues a protocols discovery workflow process
        api_response = api_instance.create_protocols_task_v2_analyses_analysis_id_agent_protocols_post(analysis_id)
        print("The response of AgentApi->create_protocols_task_v2_analyses_analysis_id_agent_protocols_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_protocols_task_v2_analyses_analysis_id_agent_protocols_post: %s\n" % e)
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

# **create_secrets_task_v2_analyses_analysis_id_agent_secrets_post**
> BaseResponseQueuedWorkflowTaskResponse create_secrets_task_v2_analyses_analysis_id_agent_secrets_post(analysis_id)

Queues a secrets discovery workflow process

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
        # Queues a secrets discovery workflow process
        api_response = api_instance.create_secrets_task_v2_analyses_analysis_id_agent_secrets_post(analysis_id)
        print("The response of AgentApi->create_secrets_task_v2_analyses_analysis_id_agent_secrets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_secrets_task_v2_analyses_analysis_id_agent_secrets_post: %s\n" % e)
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

# **get_protocols_result_v2_analyses_analysis_id_agent_protocols_get**
> BaseResponseProtocolsAgentResponse get_protocols_result_v2_analyses_analysis_id_agent_protocols_get(analysis_id)

Get Protocols Result

Returns the protocols report, including metadata, findings, and evidence.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_protocols_agent_response import BaseResponseProtocolsAgentResponse
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
        # Get Protocols Result
        api_response = api_instance.get_protocols_result_v2_analyses_analysis_id_agent_protocols_get(analysis_id)
        print("The response of AgentApi->get_protocols_result_v2_analyses_analysis_id_agent_protocols_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_protocols_result_v2_analyses_analysis_id_agent_protocols_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseProtocolsAgentResponse**](BaseResponseProtocolsAgentResponse.md)

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

# **get_secrets_result_v2_analyses_analysis_id_agent_secrets_get**
> BaseResponseSecretsAgentResponse get_secrets_result_v2_analyses_analysis_id_agent_secrets_get(analysis_id)

Get Secrets Result

Returns the secrets report, including metadata, findings, and evidence.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_secrets_agent_response import BaseResponseSecretsAgentResponse
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
        # Get Secrets Result
        api_response = api_instance.get_secrets_result_v2_analyses_analysis_id_agent_secrets_get(analysis_id)
        print("The response of AgentApi->get_secrets_result_v2_analyses_analysis_id_agent_secrets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_secrets_result_v2_analyses_analysis_id_agent_secrets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseSecretsAgentResponse**](BaseResponseSecretsAgentResponse.md)

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

# **v3_cancel_security_scan_operation**
> v3_cancel_security_scan_operation(analysis_id)

Cancel a security-scan operation.

Requests cancellation of the currently running security-scan run for the analysis. Returns 404 if no run is in progress.

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
        # Cancel a security-scan operation.
        api_instance.v3_cancel_security_scan_operation(analysis_id)
    except Exception as e:
        print("Exception when calling AgentApi->v3_cancel_security_scan_operation: %s\n" % e)
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

# **v3_get_binary_agent_feedback**
> FeedbackOutputBody v3_get_binary_agent_feedback(analysis_id, agent)

Get the caller's feedback on an agent's output.

Returns the sentiment the caller recorded for one agent on this analysis, or a null sentiment when they have not recorded any.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.feedback_output_body import FeedbackOutputBody
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
    agent = 'agent_example' # str | Which agent's output the feedback is about

    try:
        # Get the caller's feedback on an agent's output.
        api_response = api_instance.v3_get_binary_agent_feedback(analysis_id, agent)
        print("The response of AgentApi->v3_get_binary_agent_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_binary_agent_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **agent** | **str**| Which agent&#39;s output the feedback is about | 

### Return type

[**FeedbackOutputBody**](FeedbackOutputBody.md)

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

# **v3_get_capabilities_operation**
> OperationMetadataCapabilitiesResult v3_get_capabilities_operation(analysis_id)

Get a capabilities operation.

Polls a capabilities run. `metadata.status` tracks the run and `metadata.log_history` carries its progress messages; `response` is set once the run has completed.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_capabilities_result import OperationMetadataCapabilitiesResult
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
        # Get a capabilities operation.
        api_response = api_instance.v3_get_capabilities_operation(analysis_id)
        print("The response of AgentApi->v3_get_capabilities_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_capabilities_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataCapabilitiesResult**](OperationMetadataCapabilitiesResult.md)

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

# **v3_get_crypto_explain_operation**
> OperationCryptoExplainMetadataCryptoExplainResult v3_get_crypto_explain_operation(function_id)

Get a crypto-explain operation.

Returns the current state of the crypto-explain run for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_crypto_explain_metadata_crypto_explain_result import OperationCryptoExplainMetadataCryptoExplainResult
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
    function_id = 56 # int | Function ID

    try:
        # Get a crypto-explain operation.
        api_response = api_instance.v3_get_crypto_explain_operation(function_id)
        print("The response of AgentApi->v3_get_crypto_explain_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_crypto_explain_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**OperationCryptoExplainMetadataCryptoExplainResult**](OperationCryptoExplainMetadataCryptoExplainResult.md)

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

# **v3_get_crypto_scan_operation**
> OperationCryptoScanMetadataCryptoScanResult v3_get_crypto_scan_operation(analysis_id)

Get a crypto-scan operation.

Returns the current state of the crypto-scan run for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_crypto_scan_metadata_crypto_scan_result import OperationCryptoScanMetadataCryptoScanResult
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
        # Get a crypto-scan operation.
        api_response = api_instance.v3_get_crypto_scan_operation(analysis_id)
        print("The response of AgentApi->v3_get_crypto_scan_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_crypto_scan_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationCryptoScanMetadataCryptoScanResult**](OperationCryptoScanMetadataCryptoScanResult.md)

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

# **v3_get_execution_explain_operation**
> OperationExecutionExplainMetadataExecutionExplainResult v3_get_execution_explain_operation(function_id)

Get an execution-explain operation.

Returns the current state of the execution-explain run for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_execution_explain_metadata_execution_explain_result import OperationExecutionExplainMetadataExecutionExplainResult
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
    function_id = 56 # int | Function ID

    try:
        # Get an execution-explain operation.
        api_response = api_instance.v3_get_execution_explain_operation(function_id)
        print("The response of AgentApi->v3_get_execution_explain_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_execution_explain_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**OperationExecutionExplainMetadataExecutionExplainResult**](OperationExecutionExplainMetadataExecutionExplainResult.md)

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

# **v3_get_execution_scan_operation**
> OperationExecutionScanMetadataExecutionScanResult v3_get_execution_scan_operation(analysis_id)

Get an execution-scan operation.

Returns the current state of the execution-scan run for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_execution_scan_metadata_execution_scan_result import OperationExecutionScanMetadataExecutionScanResult
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
        # Get an execution-scan operation.
        api_response = api_instance.v3_get_execution_scan_operation(analysis_id)
        print("The response of AgentApi->v3_get_execution_scan_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_execution_scan_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationExecutionScanMetadataExecutionScanResult**](OperationExecutionScanMetadataExecutionScanResult.md)

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

# **v3_get_filesystem_analyse_operation**
> OperationFilesystemAnalyseMetadataFilesystemAnalyseResult v3_get_filesystem_analyse_operation(function_id)

Get a filesystem-analyse operation.

Returns the current state of the filesystem-analyse run for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_filesystem_analyse_metadata_filesystem_analyse_result import OperationFilesystemAnalyseMetadataFilesystemAnalyseResult
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
    function_id = 56 # int | Function ID

    try:
        # Get a filesystem-analyse operation.
        api_response = api_instance.v3_get_filesystem_analyse_operation(function_id)
        print("The response of AgentApi->v3_get_filesystem_analyse_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_filesystem_analyse_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**OperationFilesystemAnalyseMetadataFilesystemAnalyseResult**](OperationFilesystemAnalyseMetadataFilesystemAnalyseResult.md)

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

# **v3_get_filesystem_scan_operation**
> OperationFilesystemScanMetadataFilesystemScanResult v3_get_filesystem_scan_operation(analysis_id)

Get a filesystem-scan operation.

Returns the current state of the filesystem-scan run for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_filesystem_scan_metadata_filesystem_scan_result import OperationFilesystemScanMetadataFilesystemScanResult
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
        # Get a filesystem-scan operation.
        api_response = api_instance.v3_get_filesystem_scan_operation(analysis_id)
        print("The response of AgentApi->v3_get_filesystem_scan_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_filesystem_scan_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationFilesystemScanMetadataFilesystemScanResult**](OperationFilesystemScanMetadataFilesystemScanResult.md)

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

# **v3_get_networking_explain_operation**
> OperationNetworkingExplainMetadataNetworkingExplainResult v3_get_networking_explain_operation(function_id)

Get a networking-explain operation.

Returns the current state of the networking-explain run for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_networking_explain_metadata_networking_explain_result import OperationNetworkingExplainMetadataNetworkingExplainResult
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
    function_id = 56 # int | Function ID

    try:
        # Get a networking-explain operation.
        api_response = api_instance.v3_get_networking_explain_operation(function_id)
        print("The response of AgentApi->v3_get_networking_explain_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_networking_explain_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**OperationNetworkingExplainMetadataNetworkingExplainResult**](OperationNetworkingExplainMetadataNetworkingExplainResult.md)

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

# **v3_get_networking_scan_operation**
> OperationNetworkingScanMetadataNetworkingScanResult v3_get_networking_scan_operation(analysis_id)

Get a networking-scan operation.

Returns the current state of the networking-scan run for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_networking_scan_metadata_networking_scan_result import OperationNetworkingScanMetadataNetworkingScanResult
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
        # Get a networking-scan operation.
        api_response = api_instance.v3_get_networking_scan_operation(analysis_id)
        print("The response of AgentApi->v3_get_networking_scan_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_networking_scan_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationNetworkingScanMetadataNetworkingScanResult**](OperationNetworkingScanMetadataNetworkingScanResult.md)

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

# **v3_get_protocols_operation**
> OperationMetadataReportResult v3_get_protocols_operation(analysis_id)

Get a protocols operation.

Polls a protocols run. `metadata.status` tracks the run and `metadata.log_history` carries its progress messages; `response.report` is set once the run has completed and carries the findings document as the agent produced it.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_report_result import OperationMetadataReportResult
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
        # Get a protocols operation.
        api_response = api_instance.v3_get_protocols_operation(analysis_id)
        print("The response of AgentApi->v3_get_protocols_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_protocols_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataReportResult**](OperationMetadataReportResult.md)

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

# **v3_get_remediation_operation**
> OperationMetadataRemediationResult v3_get_remediation_operation(analysis_id)

Get a remediation operation.

Polls a remediation run. `metadata.status` tracks the run and `metadata.log_history` carries its progress messages; `response` is set once the run has completed.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_remediation_result import OperationMetadataRemediationResult
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
        # Get a remediation operation.
        api_response = api_instance.v3_get_remediation_operation(analysis_id)
        print("The response of AgentApi->v3_get_remediation_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_remediation_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataRemediationResult**](OperationMetadataRemediationResult.md)

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

# **v3_get_report_analysis_operation**
> OperationMetadataThreatReportResult v3_get_report_analysis_operation(analysis_id)

Get a report-analysis operation.

Polls a report-analysis run. `metadata.status` tracks the run and `metadata.log_history` carries its progress messages; `response` is set once the run has completed.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_threat_report_result import OperationMetadataThreatReportResult
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
        # Get a report-analysis operation.
        api_response = api_instance.v3_get_report_analysis_operation(analysis_id)
        print("The response of AgentApi->v3_get_report_analysis_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_report_analysis_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataThreatReportResult**](OperationMetadataThreatReportResult.md)

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

# **v3_get_secrets_operation**
> OperationMetadataReportResult v3_get_secrets_operation(analysis_id)

Get a secrets operation.

Polls a secrets run. `metadata.status` tracks the run and `metadata.log_history` carries its progress messages; `response.report` is set once the run has completed and carries the findings document as the agent produced it.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_report_result import OperationMetadataReportResult
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
        # Get a secrets operation.
        api_response = api_instance.v3_get_secrets_operation(analysis_id)
        print("The response of AgentApi->v3_get_secrets_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_secrets_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataReportResult**](OperationMetadataReportResult.md)

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

# **v3_get_security_scan_operation**
> OperationSecurityScanMetadataSecurityScanResult v3_get_security_scan_operation(analysis_id)

Get a security-scan operation.

Returns the current state of the security-scan run for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_security_scan_metadata_security_scan_result import OperationSecurityScanMetadataSecurityScanResult
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
        # Get a security-scan operation.
        api_response = api_instance.v3_get_security_scan_operation(analysis_id)
        print("The response of AgentApi->v3_get_security_scan_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_security_scan_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationSecurityScanMetadataSecurityScanResult**](OperationSecurityScanMetadataSecurityScanResult.md)

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

# **v3_get_triage_operation**
> OperationMetadataTriageResult v3_get_triage_operation(analysis_id)

Get a triage operation.

Polls a triage run. `metadata.status` tracks the run and `metadata.log_history` carries its progress messages; `response` is set once the run has completed.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_triage_result import OperationMetadataTriageResult
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
        # Get a triage operation.
        api_response = api_instance.v3_get_triage_operation(analysis_id)
        print("The response of AgentApi->v3_get_triage_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_get_triage_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataTriageResult**](OperationMetadataTriageResult.md)

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

# **v3_run_capabilities**
> OperationMetadataCapabilitiesResult v3_run_capabilities(analysis_id)

Run the capabilities agent.

Starts the capabilities agent, which attributes behavioural capabilities to individual functions, and returns the operation to poll for its outcome. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_capabilities_result import OperationMetadataCapabilitiesResult
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
        # Run the capabilities agent.
        api_response = api_instance.v3_run_capabilities(analysis_id)
        print("The response of AgentApi->v3_run_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataCapabilitiesResult**](OperationMetadataCapabilitiesResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_crypto_explain**
> OperationCryptoExplainMetadataCryptoExplainResult v3_run_crypto_explain(function_id)

Run the crypto-explain agent.

Starts an agent that explains the cryptography the function implements, and returns the operation to poll for its outcome. Requires credits. Returns 409 while a run is already in progress for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_crypto_explain_metadata_crypto_explain_result import OperationCryptoExplainMetadataCryptoExplainResult
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
    function_id = 56 # int | Function ID

    try:
        # Run the crypto-explain agent.
        api_response = api_instance.v3_run_crypto_explain(function_id)
        print("The response of AgentApi->v3_run_crypto_explain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_crypto_explain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**OperationCryptoExplainMetadataCryptoExplainResult**](OperationCryptoExplainMetadataCryptoExplainResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_crypto_scan**
> OperationCryptoScanMetadataCryptoScanResult v3_run_crypto_scan(analysis_id, trigger_crypto_scan_input_body)

Run the crypto-scan agent.

Starts an agent that name-matches the analysis' functions and their callees against known crypto-library APIs, and returns the operation to poll for its outcome. Purely name-based — never triggers AI decompilation, so it costs no credits and runs in seconds. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_crypto_scan_metadata_crypto_scan_result import OperationCryptoScanMetadataCryptoScanResult
from revengai.models.trigger_crypto_scan_input_body import TriggerCryptoScanInputBody
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
    trigger_crypto_scan_input_body = revengai.TriggerCryptoScanInputBody() # TriggerCryptoScanInputBody | 

    try:
        # Run the crypto-scan agent.
        api_response = api_instance.v3_run_crypto_scan(analysis_id, trigger_crypto_scan_input_body)
        print("The response of AgentApi->v3_run_crypto_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_crypto_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **trigger_crypto_scan_input_body** | [**TriggerCryptoScanInputBody**](TriggerCryptoScanInputBody.md)|  | 

### Return type

[**OperationCryptoScanMetadataCryptoScanResult**](OperationCryptoScanMetadataCryptoScanResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v3_run_execution_explain**
> OperationExecutionExplainMetadataExecutionExplainResult v3_run_execution_explain(function_id, trigger_execution_explain_input_body)

Run the execution-explain agent.

Starts an agent that explains the code execution the function performs, and returns the operation to poll for its outcome. Requires credits. Returns 409 while a run is already in progress for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_execution_explain_metadata_execution_explain_result import OperationExecutionExplainMetadataExecutionExplainResult
from revengai.models.trigger_execution_explain_input_body import TriggerExecutionExplainInputBody
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
    function_id = 56 # int | Function ID
    trigger_execution_explain_input_body = revengai.TriggerExecutionExplainInputBody() # TriggerExecutionExplainInputBody | 

    try:
        # Run the execution-explain agent.
        api_response = api_instance.v3_run_execution_explain(function_id, trigger_execution_explain_input_body)
        print("The response of AgentApi->v3_run_execution_explain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_execution_explain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **trigger_execution_explain_input_body** | [**TriggerExecutionExplainInputBody**](TriggerExecutionExplainInputBody.md)|  | 

### Return type

[**OperationExecutionExplainMetadataExecutionExplainResult**](OperationExecutionExplainMetadataExecutionExplainResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_execution_scan**
> OperationExecutionScanMetadataExecutionScanResult v3_run_execution_scan(analysis_id, trigger_execution_scan_input_body)

Run the execution-scan agent.

Starts an agent that name-matches the analysis' functions and their callees against known code-execution APIs, and returns the operation to poll for its outcome. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_execution_scan_metadata_execution_scan_result import OperationExecutionScanMetadataExecutionScanResult
from revengai.models.trigger_execution_scan_input_body import TriggerExecutionScanInputBody
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
    trigger_execution_scan_input_body = revengai.TriggerExecutionScanInputBody() # TriggerExecutionScanInputBody | 

    try:
        # Run the execution-scan agent.
        api_response = api_instance.v3_run_execution_scan(analysis_id, trigger_execution_scan_input_body)
        print("The response of AgentApi->v3_run_execution_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_execution_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **trigger_execution_scan_input_body** | [**TriggerExecutionScanInputBody**](TriggerExecutionScanInputBody.md)|  | 

### Return type

[**OperationExecutionScanMetadataExecutionScanResult**](OperationExecutionScanMetadataExecutionScanResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v3_run_filesystem_analyse**
> OperationFilesystemAnalyseMetadataFilesystemAnalyseResult v3_run_filesystem_analyse(function_id, trigger_filesystem_analyse_input_body)

Run the filesystem-analyse agent.

Starts an agent that explains the filesystem/system access the function performs, and returns the operation to poll for its outcome. Requires credits. Returns 409 while a run is already in progress for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_filesystem_analyse_metadata_filesystem_analyse_result import OperationFilesystemAnalyseMetadataFilesystemAnalyseResult
from revengai.models.trigger_filesystem_analyse_input_body import TriggerFilesystemAnalyseInputBody
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
    function_id = 56 # int | Function ID
    trigger_filesystem_analyse_input_body = revengai.TriggerFilesystemAnalyseInputBody() # TriggerFilesystemAnalyseInputBody | 

    try:
        # Run the filesystem-analyse agent.
        api_response = api_instance.v3_run_filesystem_analyse(function_id, trigger_filesystem_analyse_input_body)
        print("The response of AgentApi->v3_run_filesystem_analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_filesystem_analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **trigger_filesystem_analyse_input_body** | [**TriggerFilesystemAnalyseInputBody**](TriggerFilesystemAnalyseInputBody.md)|  | 

### Return type

[**OperationFilesystemAnalyseMetadataFilesystemAnalyseResult**](OperationFilesystemAnalyseMetadataFilesystemAnalyseResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_filesystem_scan**
> OperationFilesystemScanMetadataFilesystemScanResult v3_run_filesystem_scan(analysis_id, trigger_filesystem_scan_input_body)

Run the filesystem-scan agent.

Starts an agent that name-matches the analysis' functions and their callees against known filesystem/system APIs, and returns the operation to poll for its outcome.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_filesystem_scan_metadata_filesystem_scan_result import OperationFilesystemScanMetadataFilesystemScanResult
from revengai.models.trigger_filesystem_scan_input_body import TriggerFilesystemScanInputBody
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
    trigger_filesystem_scan_input_body = revengai.TriggerFilesystemScanInputBody() # TriggerFilesystemScanInputBody | 

    try:
        # Run the filesystem-scan agent.
        api_response = api_instance.v3_run_filesystem_scan(analysis_id, trigger_filesystem_scan_input_body)
        print("The response of AgentApi->v3_run_filesystem_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_filesystem_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **trigger_filesystem_scan_input_body** | [**TriggerFilesystemScanInputBody**](TriggerFilesystemScanInputBody.md)|  | 

### Return type

[**OperationFilesystemScanMetadataFilesystemScanResult**](OperationFilesystemScanMetadataFilesystemScanResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v3_run_networking_explain**
> OperationNetworkingExplainMetadataNetworkingExplainResult v3_run_networking_explain(function_id, trigger_networking_explain_input_body)

Run the networking-explain agent.

Starts an agent that explains the network communication a function performs, and returns the operation to poll for its outcome. Requires credits. Returns 409 while a run is already in progress for this function.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_networking_explain_metadata_networking_explain_result import OperationNetworkingExplainMetadataNetworkingExplainResult
from revengai.models.trigger_networking_explain_input_body import TriggerNetworkingExplainInputBody
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
    function_id = 56 # int | Function ID
    trigger_networking_explain_input_body = revengai.TriggerNetworkingExplainInputBody() # TriggerNetworkingExplainInputBody | 

    try:
        # Run the networking-explain agent.
        api_response = api_instance.v3_run_networking_explain(function_id, trigger_networking_explain_input_body)
        print("The response of AgentApi->v3_run_networking_explain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_networking_explain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **trigger_networking_explain_input_body** | [**TriggerNetworkingExplainInputBody**](TriggerNetworkingExplainInputBody.md)|  | 

### Return type

[**OperationNetworkingExplainMetadataNetworkingExplainResult**](OperationNetworkingExplainMetadataNetworkingExplainResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_networking_scan**
> OperationNetworkingScanMetadataNetworkingScanResult v3_run_networking_scan(analysis_id, trigger_networking_scan_input_body)

Run the networking-scan agent.

Starts an agent that name-matches the analysis' functions and their callees against known networking APIs, and returns the operation to poll for its outcome.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_networking_scan_metadata_networking_scan_result import OperationNetworkingScanMetadataNetworkingScanResult
from revengai.models.trigger_networking_scan_input_body import TriggerNetworkingScanInputBody
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
    trigger_networking_scan_input_body = revengai.TriggerNetworkingScanInputBody() # TriggerNetworkingScanInputBody | 

    try:
        # Run the networking-scan agent.
        api_response = api_instance.v3_run_networking_scan(analysis_id, trigger_networking_scan_input_body)
        print("The response of AgentApi->v3_run_networking_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_networking_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **trigger_networking_scan_input_body** | [**TriggerNetworkingScanInputBody**](TriggerNetworkingScanInputBody.md)|  | 

### Return type

[**OperationNetworkingScanMetadataNetworkingScanResult**](OperationNetworkingScanMetadataNetworkingScanResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v3_run_protocols**
> OperationMetadataReportResult v3_run_protocols(analysis_id)

Run the protocols agent.

Starts the protocols agent, which identifies the network and data protocols the binary implements, and returns the operation to poll for its outcome. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_report_result import OperationMetadataReportResult
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
        # Run the protocols agent.
        api_response = api_instance.v3_run_protocols(analysis_id)
        print("The response of AgentApi->v3_run_protocols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_protocols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataReportResult**](OperationMetadataReportResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_remediation**
> OperationMetadataRemediationResult v3_run_remediation(analysis_id)

Run the remediation agent.

Starts the remediation agent, which generates YARA, Snort and STIX detection rules for the binary, and returns the operation to poll for its outcome. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_remediation_result import OperationMetadataRemediationResult
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
        # Run the remediation agent.
        api_response = api_instance.v3_run_remediation(analysis_id)
        print("The response of AgentApi->v3_run_remediation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_remediation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataRemediationResult**](OperationMetadataRemediationResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_report_analysis**
> OperationMetadataThreatReportResult v3_run_report_analysis(analysis_id)

Run the report-analysis agent.

Starts the report-analysis agent, which produces a combined threat report — summary, software type, attack flow, indicators of compromise, MITRE ATT&CK techniques and a YARA rule — and returns the operation to poll for its outcome. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_threat_report_result import OperationMetadataThreatReportResult
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
        # Run the report-analysis agent.
        api_response = api_instance.v3_run_report_analysis(analysis_id)
        print("The response of AgentApi->v3_run_report_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_report_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataThreatReportResult**](OperationMetadataThreatReportResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_secrets**
> OperationMetadataReportResult v3_run_secrets(analysis_id)

Run the secrets agent.

Starts the secrets agent, which finds credentials and other hardcoded secrets in the binary, and returns the operation to poll for its outcome. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_report_result import OperationMetadataReportResult
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
        # Run the secrets agent.
        api_response = api_instance.v3_run_secrets(analysis_id)
        print("The response of AgentApi->v3_run_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataReportResult**](OperationMetadataReportResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_security_scan**
> OperationSecurityScanMetadataSecurityScanResult v3_run_security_scan(analysis_id, trigger_security_scan_input_body)

Run the security-scan agent.

Starts an agent that decompiles the analysis' functions and runs a security scan over the decompiled source, and returns the operation to poll for its outcome. Each function costs an AI decompilation, so a whole-analysis run can be expensive — use `max_functions_to_scan` to bound it. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_security_scan_metadata_security_scan_result import OperationSecurityScanMetadataSecurityScanResult
from revengai.models.trigger_security_scan_input_body import TriggerSecurityScanInputBody
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
    trigger_security_scan_input_body = revengai.TriggerSecurityScanInputBody() # TriggerSecurityScanInputBody | 

    try:
        # Run the security-scan agent.
        api_response = api_instance.v3_run_security_scan(analysis_id, trigger_security_scan_input_body)
        print("The response of AgentApi->v3_run_security_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_security_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **trigger_security_scan_input_body** | [**TriggerSecurityScanInputBody**](TriggerSecurityScanInputBody.md)|  | 

### Return type

[**OperationSecurityScanMetadataSecurityScanResult**](OperationSecurityScanMetadataSecurityScanResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_run_triage**
> OperationMetadataTriageResult v3_run_triage(analysis_id)

Run the triage agent.

Starts the triage agent, which scores the binary and each of its functions for maliciousness, and returns the operation to poll for its outcome. Unlike the other binary agents this one is not gated on subscription tier. Returns 409 while a run is already in progress for this analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_metadata_triage_result import OperationMetadataTriageResult
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
        # Run the triage agent.
        api_response = api_instance.v3_run_triage(analysis_id)
        print("The response of AgentApi->v3_run_triage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->v3_run_triage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationMetadataTriageResult**](OperationMetadataTriageResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
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
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits

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
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_upsert_binary_agent_feedback**
> v3_upsert_binary_agent_feedback(analysis_id, agent, submit_feedback_input_body)

Record feedback on an agent's output.

Records how useful the caller found one agent's output for this analysis. Replaces any sentiment they recorded previously.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.submit_feedback_input_body import SubmitFeedbackInputBody
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
    agent = 'agent_example' # str | Which agent's output the feedback is about
    submit_feedback_input_body = revengai.SubmitFeedbackInputBody() # SubmitFeedbackInputBody | 

    try:
        # Record feedback on an agent's output.
        api_instance.v3_upsert_binary_agent_feedback(analysis_id, agent, submit_feedback_input_body)
    except Exception as e:
        print("Exception when calling AgentApi->v3_upsert_binary_agent_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **agent** | **str**| Which agent&#39;s output the feedback is about | 
 **submit_feedback_input_body** | [**SubmitFeedbackInputBody**](SubmitFeedbackInputBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

