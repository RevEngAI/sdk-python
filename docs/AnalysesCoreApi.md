# revengai.AnalysesCoreApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_string_to_analysis**](AnalysesCoreApi.md#add_user_string_to_analysis) | **POST** /v3/analyses/{analysis_id}/user-provided-strings | Add a user-provided string to an analysis.
[**create_analysis**](AnalysesCoreApi.md#create_analysis) | **POST** /v2/analyses | Create Analysis
[**delete_analysis**](AnalysesCoreApi.md#delete_analysis) | **DELETE** /v2/analyses/{analysis_id} | Delete Analysis
[**get_analysis_basic_info**](AnalysesCoreApi.md#get_analysis_basic_info) | **GET** /v2/analyses/{analysis_id}/basic | Gets basic analysis information
[**get_analysis_basic_info_0**](AnalysesCoreApi.md#get_analysis_basic_info_0) | **GET** /v3/analyses/{analysis_id}/basic | Get basic analysis information
[**get_analysis_bytes**](AnalysesCoreApi.md#get_analysis_bytes) | **GET** /v3/analyses/{analysis_id}/bytes | Get the bytes of a binary
[**get_analysis_function_map**](AnalysesCoreApi.md#get_analysis_function_map) | **GET** /v2/analyses/{analysis_id}/func_maps | Get Analysis Function Map
[**get_analysis_function_matches**](AnalysesCoreApi.md#get_analysis_function_matches) | **GET** /v3/analyses/{analysis_id}/functions/matches | Get function-matching results for an analysis
[**get_analysis_function_matching_status**](AnalysesCoreApi.md#get_analysis_function_matching_status) | **GET** /v3/analyses/{analysis_id}/functions/matches/status | Get function-matching status for an analysis
[**get_analysis_logs**](AnalysesCoreApi.md#get_analysis_logs) | **GET** /v2/analyses/{analysis_id}/logs | Gets the logs of an analysis
[**get_analysis_params**](AnalysesCoreApi.md#get_analysis_params) | **GET** /v2/analyses/{analysis_id}/params | Gets analysis param information
[**get_analysis_status**](AnalysesCoreApi.md#get_analysis_status) | **GET** /v2/analyses/{analysis_id}/status | Gets the status of an analysis
[**get_dynamic_execution_report**](AnalysesCoreApi.md#get_dynamic_execution_report) | **GET** /v2/analyses/{analysis_id}/dynamic-execution/report | Get dynamic execution report
[**get_dynamic_execution_status**](AnalysesCoreApi.md#get_dynamic_execution_status) | **GET** /v2/analyses/{analysis_id}/dynamic-execution/status | Get dynamic execution status
[**insert_analysis_log**](AnalysesCoreApi.md#insert_analysis_log) | **POST** /v2/analyses/{analysis_id}/logs | Insert a log entry for an analysis
[**list_analyses**](AnalysesCoreApi.md#list_analyses) | **GET** /v2/analyses/list | Gets the most recent analyses
[**lookup_binary_id**](AnalysesCoreApi.md#lookup_binary_id) | **GET** /v2/analyses/lookup/{binary_id} | Gets the analysis ID from binary ID
[**put_analysis_strings**](AnalysesCoreApi.md#put_analysis_strings) | **PUT** /v2/analyses/{analysis_id}/strings | Add strings to the analysis
[**requeue_analysis**](AnalysesCoreApi.md#requeue_analysis) | **POST** /v2/analyses/{analysis_id}/requeue | Requeue Analysis
[**start_analysis_function_matching**](AnalysesCoreApi.md#start_analysis_function_matching) | **POST** /v3/analyses/{analysis_id}/functions/matches | Start function matching for an analysis
[**update_analysis**](AnalysesCoreApi.md#update_analysis) | **PATCH** /v2/analyses/{analysis_id} | Update Analysis
[**update_analysis_tags**](AnalysesCoreApi.md#update_analysis_tags) | **PATCH** /v2/analyses/{analysis_id}/tags | Update Analysis Tags
[**upload_file**](AnalysesCoreApi.md#upload_file) | **POST** /v2/upload | Upload File
[**v3_create_analysis**](AnalysesCoreApi.md#v3_create_analysis) | **POST** /v3/analyses | Create an analysis
[**v3_delete_analysis**](AnalysesCoreApi.md#v3_delete_analysis) | **DELETE** /v3/analyses/{analysis_id} | Delete an analysis.
[**v3_download_binary_export**](AnalysesCoreApi.md#v3_download_binary_export) | **GET** /v3/analyses/{analysis_id}/binary-export | Download a binary export
[**v3_get_analysis**](AnalysesCoreApi.md#v3_get_analysis) | **GET** /v3/analyses/{analysis_id} | Get an analysis.
[**v3_get_analysis_auto_unstrip_status**](AnalysesCoreApi.md#v3_get_analysis_auto_unstrip_status) | **GET** /v3/analyses/{analysis_id}/auto-unstrip/status | Get the auto-unstrip status for an analysis.
[**v3_get_analysis_functions_progress**](AnalysesCoreApi.md#v3_get_analysis_functions_progress) | **GET** /v3/analyses/{analysis_id}/progress/functions | Get function embedding progress for an analysis.
[**v3_get_analysis_logs**](AnalysesCoreApi.md#v3_get_analysis_logs) | **GET** /v3/analyses/{analysis_id}/logs | Get the Analysis log
[**v3_get_analysis_operation**](AnalysesCoreApi.md#v3_get_analysis_operation) | **GET** /v3/operations/analyses/{analysis_id} | Get an Analysis-creation operation
[**v3_get_analysis_strings**](AnalysesCoreApi.md#v3_get_analysis_strings) | **GET** /v3/analyses/{analysis_id}/functions/strings | List strings for an analysis.
[**v3_get_analysis_strings_status**](AnalysesCoreApi.md#v3_get_analysis_strings_status) | **GET** /v3/analyses/{analysis_id}/functions/strings/status | Get the string-extraction status for an analysis.
[**v3_get_binary_export_operation**](AnalysesCoreApi.md#v3_get_binary_export_operation) | **GET** /v3/operations/binary-export/{task_id} | Get a binary export operation
[**v3_list_analyses**](AnalysesCoreApi.md#v3_list_analyses) | **GET** /v3/analyses | List analyses
[**v3_list_example_analyses**](AnalysesCoreApi.md#v3_list_example_analyses) | **GET** /v3/analyses/examples | List example analyses
[**v3_lookup_analysis_by_binary_id**](AnalysesCoreApi.md#v3_lookup_analysis_by_binary_id) | **GET** /v3/analyses/lookup/{binary_id} | Look up the most recent analysis for a binary.
[**v3_queue_binary_export**](AnalysesCoreApi.md#v3_queue_binary_export) | **POST** /v3/analyses/{analysis_id}/binary-export | Queue a binary export
[**v3_update_analysis**](AnalysesCoreApi.md#v3_update_analysis) | **PATCH** /v3/analyses/{analysis_id} | Update an analysis.
[**v3_upgrade_analysis_model**](AnalysesCoreApi.md#v3_upgrade_analysis_model) | **POST** /v3/analyses/{analysis_id}/upgrade-model | Re-analyse on the latest model


# **add_user_string_to_analysis**
> object add_user_string_to_analysis(analysis_id, add_user_string_input_body)

Add a user-provided string to an analysis.

Attaches a user-provided string to an analysis at the given virtual address. The string is stored with source `USER` and complements strings discovered automatically during analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.add_user_string_input_body import AddUserStringInputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    add_user_string_input_body = revengai.AddUserStringInputBody() # AddUserStringInputBody | 

    try:
        # Add a user-provided string to an analysis.
        api_response = api_instance.add_user_string_to_analysis(analysis_id, add_user_string_input_body)
        print("The response of AnalysesCoreApi->add_user_string_to_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->add_user_string_to_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **add_user_string_input_body** | [**AddUserStringInputBody**](AddUserStringInputBody.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis**
> BaseResponseAnalysisCreateResponse create_analysis(analysis_create_request, x_rev_eng_application=x_rev_eng_application)

Create Analysis

Begins an analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_create_request import AnalysisCreateRequest
from revengai.models.base_response_analysis_create_response import BaseResponseAnalysisCreateResponse
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_create_request = revengai.AnalysisCreateRequest() # AnalysisCreateRequest | 
    x_rev_eng_application = 'x_rev_eng_application_example' # str |  (optional)

    try:
        # Create Analysis
        api_response = api_instance.create_analysis(analysis_create_request, x_rev_eng_application=x_rev_eng_application)
        print("The response of AnalysesCoreApi->create_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->create_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_create_request** | [**AnalysisCreateRequest**](AnalysisCreateRequest.md)|  | 
 **x_rev_eng_application** | **str**|  | [optional] 

### Return type

[**BaseResponseAnalysisCreateResponse**](BaseResponseAnalysisCreateResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Unprocessable Entity |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_analysis**
> BaseResponseDict delete_analysis(analysis_id)

Delete Analysis

Deletes an analysis based on the provided analysis ID.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_dict import BaseResponseDict
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Delete Analysis
        api_response = api_instance.delete_analysis(analysis_id)
        print("The response of AnalysesCoreApi->delete_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->delete_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseDict**](BaseResponseDict.md)

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
**404** | Not Found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_basic_info**
> BaseResponseBasic get_analysis_basic_info(analysis_id)

Gets basic analysis information

Returns basic analysis information for an analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_basic import BaseResponseBasic
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Gets basic analysis information
        api_response = api_instance.get_analysis_basic_info(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_basic_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_basic_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseBasic**](BaseResponseBasic.md)

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

# **get_analysis_basic_info_0**
> AnalysisBasicInfoOutputBody get_analysis_basic_info_0(analysis_id)

Get basic analysis information

Returns basic metadata for the given analysis including binary details, model, owner, and function count.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_basic_info_output_body import AnalysisBasicInfoOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get basic analysis information
        api_response = api_instance.get_analysis_basic_info_0(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_basic_info_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_basic_info_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**AnalysisBasicInfoOutputBody**](AnalysisBasicInfoOutputBody.md)

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

# **get_analysis_bytes**
> get_analysis_bytes(analysis_id, page=page)

Get the bytes of a binary

Returns a 64kb byte page from the binary.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    page = 56 # int | 64kb page of binary data (optional)

    try:
        # Get the bytes of a binary
        api_instance.get_analysis_bytes(analysis_id, page=page)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_bytes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **page** | **int**| 64kb page of binary data | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_function_map**
> BaseResponseAnalysisFunctionMapping get_analysis_function_map(analysis_id)

Get Analysis Function Map

Returns three maps: a map of function ids to function addresses, it's inverse and a map of function addresses to function names.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_analysis_function_mapping import BaseResponseAnalysisFunctionMapping
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Analysis Function Map
        api_response = api_instance.get_analysis_function_map(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_function_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_function_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseAnalysisFunctionMapping**](BaseResponseAnalysisFunctionMapping.md)

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

# **get_analysis_function_matches**
> GetMatchesOutputBody get_analysis_function_matches(analysis_id, match_id=match_id)

Get function-matching results for an analysis

Returns the matches blob when the matching workflow has completed. While the workflow is in progress this endpoint returns the current status with no matches; use /matches/status to poll progress.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_matches_output_body import GetMatchesOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    match_id = 'match_id_example' # str | Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. (optional)

    try:
        # Get function-matching results for an analysis
        api_response = api_instance.get_analysis_function_matches(analysis_id, match_id=match_id)
        print("The response of AnalysesCoreApi->get_analysis_function_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_function_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **match_id** | **str**| Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. | [optional] 

### Return type

[**GetMatchesOutputBody**](GetMatchesOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_function_matching_status**
> GetMatchesStatusOutputBody get_analysis_function_matching_status(analysis_id, match_id=match_id)

Get function-matching status for an analysis

Returns the matching workflow's current status. Does not include the matches blob — use GET /matches for that.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_matches_status_output_body import GetMatchesStatusOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    match_id = 'match_id_example' # str | Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. (optional)

    try:
        # Get function-matching status for an analysis
        api_response = api_instance.get_analysis_function_matching_status(analysis_id, match_id=match_id)
        print("The response of AnalysesCoreApi->get_analysis_function_matching_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_function_matching_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **match_id** | **str**| Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. | [optional] 

### Return type

[**GetMatchesStatusOutputBody**](GetMatchesStatusOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_logs**
> BaseResponseLogs get_analysis_logs(analysis_id)

Gets the logs of an analysis

Given an analysis ID gets the current logs of an analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_logs import BaseResponseLogs
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Gets the logs of an analysis
        api_response = api_instance.get_analysis_logs(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseLogs**](BaseResponseLogs.md)

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

# **get_analysis_params**
> BaseResponseParams get_analysis_params(analysis_id)

Gets analysis param information

Gets the params that the analysis was run with

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_params import BaseResponseParams
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Gets analysis param information
        api_response = api_instance.get_analysis_params(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseParams**](BaseResponseParams.md)

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

# **get_analysis_status**
> BaseResponseStatus get_analysis_status(analysis_id)

Gets the status of an analysis

Given an analysis ID gets the current status of the analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_status import BaseResponseStatus
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Gets the status of an analysis
        api_response = api_instance.get_analysis_status(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseStatus**](BaseResponseStatus.md)

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

# **get_dynamic_execution_report**
> AnalysisReport get_dynamic_execution_report(analysis_id)

Get dynamic execution report

Returns the dynamic execution report JSON for the analysis. Requires the task to be in COMPLETED status.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`DYNAMIC_EXECUTION_INCOMPLETE`](/errors/DYNAMIC_EXECUTION_INCOMPLETE) — Dynamic Execution Incomplete

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_report import AnalysisReport
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get dynamic execution report
        api_response = api_instance.get_dynamic_execution_report(analysis_id)
        print("The response of AnalysesCoreApi->get_dynamic_execution_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_dynamic_execution_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**AnalysisReport**](AnalysisReport.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_execution_status**
> DynamicExecutionStatusResponse get_dynamic_execution_status(analysis_id)

Get dynamic execution status

Returns the status of the most recent dynamic execution task for the analysis. Returns UNINITIALISED if no task has been started.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.dynamic_execution_status_response import DynamicExecutionStatusResponse
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get dynamic execution status
        api_response = api_instance.get_dynamic_execution_status(analysis_id)
        print("The response of AnalysesCoreApi->get_dynamic_execution_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_dynamic_execution_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**DynamicExecutionStatusResponse**](DynamicExecutionStatusResponse.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_analysis_log**
> BaseResponse insert_analysis_log(analysis_id, insert_analysis_log_request)

Insert a log entry for an analysis

Inserts a log record for an analysis. Only the analysis owner can insert logs.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response import BaseResponse
from revengai.models.insert_analysis_log_request import InsertAnalysisLogRequest
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    insert_analysis_log_request = revengai.InsertAnalysisLogRequest() # InsertAnalysisLogRequest | 

    try:
        # Insert a log entry for an analysis
        api_response = api_instance.insert_analysis_log(analysis_id, insert_analysis_log_request)
        print("The response of AnalysesCoreApi->insert_analysis_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->insert_analysis_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **insert_analysis_log_request** | [**InsertAnalysisLogRequest**](InsertAnalysisLogRequest.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analyses**
> BaseResponseRecent list_analyses(search_term=search_term, workspace=workspace, status=status, model_name=model_name, dynamic_execution_status=dynamic_execution_status, usernames=usernames, sha256_hash=sha256_hash, limit=limit, offset=offset, order_by=order_by, order=order)

Gets the most recent analyses

Gets the most recent analyses provided a scope, this is then paginated, if pages and limit doesnt fit, it increases the limit

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.app_api_rest_v2_analyses_enums_order_by import AppApiRestV2AnalysesEnumsOrderBy
from revengai.models.base_response_recent import BaseResponseRecent
from revengai.models.dynamic_execution_status import DynamicExecutionStatus
from revengai.models.model_name import ModelName
from revengai.models.order import Order
from revengai.models.status_input import StatusInput
from revengai.models.workspace import Workspace
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    search_term = '' # str |  (optional) (default to '')
    workspace = ["personal"] # List[Workspace] | The workspace to be viewed (optional) (default to ["personal"])
    status = ["All"] # List[StatusInput] | The status of the analysis (optional) (default to ["All"])
    model_name = [revengai.ModelName()] # List[ModelName] | Show analysis belonging to the model (optional)
    dynamic_execution_status = revengai.DynamicExecutionStatus() # DynamicExecutionStatus | Show analysis that have a dynamic execution with the given status (optional)
    usernames = [] # List[Optional[str]] | Show analysis belonging to the user (optional) (default to [])
    sha256_hash = 'sha256_hash_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    order_by = revengai.AppApiRestV2AnalysesEnumsOrderBy() # AppApiRestV2AnalysesEnumsOrderBy |  (optional)
    order = revengai.Order() # Order |  (optional)

    try:
        # Gets the most recent analyses
        api_response = api_instance.list_analyses(search_term=search_term, workspace=workspace, status=status, model_name=model_name, dynamic_execution_status=dynamic_execution_status, usernames=usernames, sha256_hash=sha256_hash, limit=limit, offset=offset, order_by=order_by, order=order)
        print("The response of AnalysesCoreApi->list_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->list_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] [default to &#39;&#39;]
 **workspace** | [**List[Workspace]**](Workspace.md)| The workspace to be viewed | [optional] [default to [&quot;personal&quot;]]
 **status** | [**List[StatusInput]**](StatusInput.md)| The status of the analysis | [optional] [default to [&quot;All&quot;]]
 **model_name** | [**List[ModelName]**](ModelName.md)| Show analysis belonging to the model | [optional] 
 **dynamic_execution_status** | [**DynamicExecutionStatus**](.md)| Show analysis that have a dynamic execution with the given status | [optional] 
 **usernames** | [**List[Optional[str]]**](str.md)| Show analysis belonging to the user | [optional] [default to []]
 **sha256_hash** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | [**AppApiRestV2AnalysesEnumsOrderBy**](.md)|  | [optional] 
 **order** | [**Order**](.md)|  | [optional] 

### Return type

[**BaseResponseRecent**](BaseResponseRecent.md)

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

# **lookup_binary_id**
> object lookup_binary_id(binary_id)

Gets the analysis ID from binary ID

Given an binary ID gets the ID of an analysis

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
    api_instance = revengai.AnalysesCoreApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the analysis ID from binary ID
        api_response = api_instance.lookup_binary_id(binary_id)
        print("The response of AnalysesCoreApi->lookup_binary_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->lookup_binary_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

**object**

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

# **put_analysis_strings**
> BaseResponse put_analysis_strings(analysis_id, put_analysis_strings_request)

Add strings to the analysis

Add strings to the analysis. Rejects if any string already exists at the given vaddr.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response import BaseResponse
from revengai.models.put_analysis_strings_request import PutAnalysisStringsRequest
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    put_analysis_strings_request = revengai.PutAnalysisStringsRequest() # PutAnalysisStringsRequest | 

    try:
        # Add strings to the analysis
        api_response = api_instance.put_analysis_strings(analysis_id, put_analysis_strings_request)
        print("The response of AnalysesCoreApi->put_analysis_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->put_analysis_strings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **put_analysis_strings_request** | [**PutAnalysisStringsRequest**](PutAnalysisStringsRequest.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requeue_analysis**
> BaseResponseCreated requeue_analysis(analysis_id, re_analysis_form, x_rev_eng_application=x_rev_eng_application)

Requeue Analysis

Re-queues an already uploaded analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_created import BaseResponseCreated
from revengai.models.re_analysis_form import ReAnalysisForm
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    re_analysis_form = revengai.ReAnalysisForm() # ReAnalysisForm | 
    x_rev_eng_application = 'x_rev_eng_application_example' # str |  (optional)

    try:
        # Requeue Analysis
        api_response = api_instance.requeue_analysis(analysis_id, re_analysis_form, x_rev_eng_application=x_rev_eng_application)
        print("The response of AnalysesCoreApi->requeue_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->requeue_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **re_analysis_form** | [**ReAnalysisForm**](ReAnalysisForm.md)|  | 
 **x_rev_eng_application** | **str**|  | [optional] 

### Return type

[**BaseResponseCreated**](BaseResponseCreated.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_analysis_function_matching**
> StartMatchingOutputBody start_analysis_function_matching(analysis_id, start_matching_for_analysis_input_body)

Start function matching for an analysis

Dispatches the function-matching workflow against every function in the analysis. Returns immediately. Poll the status endpoint for progress; fetch results from the matches endpoint when status=COMPLETED.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.start_matching_for_analysis_input_body import StartMatchingForAnalysisInputBody
from revengai.models.start_matching_output_body import StartMatchingOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    start_matching_for_analysis_input_body = revengai.StartMatchingForAnalysisInputBody() # StartMatchingForAnalysisInputBody | 

    try:
        # Start function matching for an analysis
        api_response = api_instance.start_analysis_function_matching(analysis_id, start_matching_for_analysis_input_body)
        print("The response of AnalysesCoreApi->start_analysis_function_matching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->start_analysis_function_matching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **start_matching_for_analysis_input_body** | [**StartMatchingForAnalysisInputBody**](StartMatchingForAnalysisInputBody.md)|  | 

### Return type

[**StartMatchingOutputBody**](StartMatchingOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis**
> BaseResponseAnalysisDetailResponse update_analysis(analysis_id, analysis_update_request)

Update Analysis

Updates analysis attributes (binary_name, analysis_scope). User must be the owner.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_update_request import AnalysisUpdateRequest
from revengai.models.base_response_analysis_detail_response import BaseResponseAnalysisDetailResponse
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    analysis_update_request = revengai.AnalysisUpdateRequest() # AnalysisUpdateRequest | 

    try:
        # Update Analysis
        api_response = api_instance.update_analysis(analysis_id, analysis_update_request)
        print("The response of AnalysesCoreApi->update_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->update_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **analysis_update_request** | [**AnalysisUpdateRequest**](AnalysisUpdateRequest.md)|  | 

### Return type

[**BaseResponseAnalysisDetailResponse**](BaseResponseAnalysisDetailResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis_tags**
> BaseResponseAnalysisUpdateTagsResponse update_analysis_tags(analysis_id, analysis_update_tags_request)

Update Analysis Tags

Updates analysis tags. User must be the owner.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_update_tags_request import AnalysisUpdateTagsRequest
from revengai.models.base_response_analysis_update_tags_response import BaseResponseAnalysisUpdateTagsResponse
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    analysis_update_tags_request = revengai.AnalysisUpdateTagsRequest() # AnalysisUpdateTagsRequest | 

    try:
        # Update Analysis Tags
        api_response = api_instance.update_analysis_tags(analysis_id, analysis_update_tags_request)
        print("The response of AnalysesCoreApi->update_analysis_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->update_analysis_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **analysis_update_tags_request** | [**AnalysisUpdateTagsRequest**](AnalysisUpdateTagsRequest.md)|  | 

### Return type

[**BaseResponseAnalysisUpdateTagsResponse**](BaseResponseAnalysisUpdateTagsResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> BaseResponseUploadResponse upload_file(upload_file_type, file, packed_password=packed_password, force_overwrite=force_overwrite)

Upload File

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_upload_response import BaseResponseUploadResponse
from revengai.models.upload_file_type import UploadFileType
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    upload_file_type = revengai.UploadFileType() # UploadFileType | 
    file = None # bytearray | 
    packed_password = 'packed_password_example' # str |  (optional)
    force_overwrite = False # bool |  (optional) (default to False)

    try:
        # Upload File
        api_response = api_instance.upload_file(upload_file_type, file, packed_password=packed_password, force_overwrite=force_overwrite)
        print("The response of AnalysesCoreApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_file_type** | [**UploadFileType**](UploadFileType.md)|  | 
 **file** | **bytearray**|  | 
 **packed_password** | **str**|  | [optional] 
 **force_overwrite** | **bool**|  | [optional] [default to False]

### Return type

[**BaseResponseUploadResponse**](BaseResponseUploadResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_analysis**
> OperationCreateMetadataCreateResult v3_create_analysis(create_request, x_rev_eng_application=x_rev_eng_application)

Create an analysis

Queues a new Analysis for an uploaded Binary and returns the created Operation.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `413` [`REQUEST_ENTITY_TOO_LARGE`](/errors/REQUEST_ENTITY_TOO_LARGE) — Request Entity Too Large

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.create_request import CreateRequest
from revengai.models.operation_create_metadata_create_result import OperationCreateMetadataCreateResult
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    create_request = revengai.CreateRequest() # CreateRequest | 
    x_rev_eng_application = 'x_rev_eng_application_example' # str | Identifies the calling RevEng application. Recorded on the Analysis log. (optional)

    try:
        # Create an analysis
        api_response = api_instance.v3_create_analysis(create_request, x_rev_eng_application=x_rev_eng_application)
        print("The response of AnalysesCoreApi->v3_create_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_create_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**CreateRequest**](CreateRequest.md)|  | 
 **x_rev_eng_application** | **str**| Identifies the calling RevEng application. Recorded on the Analysis log. | [optional] 

### Return type

[**OperationCreateMetadataCreateResult**](OperationCreateMetadataCreateResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**413** | Request Entity Too Large |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_delete_analysis**
> v3_delete_analysis(analysis_id)

Delete an analysis.

Deactivates the analysis. Only the owner may call it.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Delete an analysis.
        api_instance.v3_delete_analysis(analysis_id)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_delete_analysis: %s\n" % e)
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

# **v3_download_binary_export**
> v3_download_binary_export(analysis_id, task_id=task_id)

Download a binary export

Streams the exported binary. Returns 404 if the task is not complete or its result has expired -- export again in either case.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    task_id = 'task_id_example' # str | Task ID returned by queueing the export (optional)

    try:
        # Download a binary export
        api_instance.v3_download_binary_export(analysis_id, task_id=task_id)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_download_binary_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **task_id** | **str**| Task ID returned by queueing the export | [optional] 

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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_analysis**
> AnalysisDetailOutputBody v3_get_analysis(analysis_id)

Get an analysis.

Returns the analysis' resource-level detail: binary attributes, ownership, and the configuration it was submitted with.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_detail_output_body import AnalysisDetailOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get an analysis.
        api_response = api_instance.v3_get_analysis(analysis_id)
        print("The response of AnalysesCoreApi->v3_get_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**AnalysisDetailOutputBody**](AnalysisDetailOutputBody.md)

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

# **v3_get_analysis_auto_unstrip_status**
> AutoUnstripStatusOutputBody v3_get_analysis_auto_unstrip_status(analysis_id)

Get the auto-unstrip status for an analysis.

Returns the status of the auto-unstrip task for the binary backing the analysis. One of `UNINITIALISED`, `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.auto_unstrip_status_output_body import AutoUnstripStatusOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get the auto-unstrip status for an analysis.
        api_response = api_instance.v3_get_analysis_auto_unstrip_status(analysis_id)
        print("The response of AnalysesCoreApi->v3_get_analysis_auto_unstrip_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis_auto_unstrip_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**AutoUnstripStatusOutputBody**](AutoUnstripStatusOutputBody.md)

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

# **v3_get_analysis_functions_progress**
> FunctionsProgressOutputBody v3_get_analysis_functions_progress(analysis_id)

Get function embedding progress for an analysis.

Returns how many functions the analysis has and how many carry an embedding, with the percentage complete. Embeddings are counted from the unified store, so an analysis whose model predates the current multi-arch one reports zero.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.functions_progress_output_body import FunctionsProgressOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get function embedding progress for an analysis.
        api_response = api_instance.v3_get_analysis_functions_progress(analysis_id)
        print("The response of AnalysesCoreApi->v3_get_analysis_functions_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis_functions_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**FunctionsProgressOutputBody**](FunctionsProgressOutputBody.md)

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

# **v3_get_analysis_logs**
> GetAnalysisLogsOutputBody v3_get_analysis_logs(analysis_id)

Get the Analysis log

Returns every log line recorded for the Analysis, oldest first, merged from every source that has written one.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_analysis_logs_output_body import GetAnalysisLogsOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get the Analysis log
        api_response = api_instance.v3_get_analysis_logs(analysis_id)
        print("The response of AnalysesCoreApi->v3_get_analysis_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**GetAnalysisLogsOutputBody**](GetAnalysisLogsOutputBody.md)

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

# **v3_get_analysis_operation**
> OperationCreateMetadataCreateResult v3_get_analysis_operation(analysis_id)

Get an Analysis-creation operation

Polls the status of an Analysis-creation operation.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_create_metadata_create_result import OperationCreateMetadataCreateResult
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get an Analysis-creation operation
        api_response = api_instance.v3_get_analysis_operation(analysis_id)
        print("The response of AnalysesCoreApi->v3_get_analysis_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationCreateMetadataCreateResult**](OperationCreateMetadataCreateResult.md)

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

# **v3_get_analysis_strings**
> ListAnalysisStringsOutputBody v3_get_analysis_strings(analysis_id, page=page, page_size=page_size, search=search, search_operator=search_operator, function_search=function_search, order_by=order_by, sort_order=sort_order)

List strings for an analysis.

Returns the strings discovered in an analysis, combining function-level and analysis-level strings. Supports value/function-name search, sorting and pagination.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_analysis_strings_output_body import ListAnalysisStringsOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    page = 1 # int | Page number (1-indexed). (optional) (default to 1)
    page_size = 100 # int | Number of results per page. (optional) (default to 100)
    search = 'search_example' # str | Filter by string value (case-insensitive substring match). (optional)
    search_operator = CONTAINS # str | How the search term matches string values. (optional) (default to CONTAINS)
    function_search = 'function_search_example' # str | Filter by function name (case-insensitive substring match). (optional)
    order_by = value # str | Field to order results by. (optional) (default to value)
    sort_order = ASC # str | Sort direction. (optional) (default to ASC)

    try:
        # List strings for an analysis.
        api_response = api_instance.v3_get_analysis_strings(analysis_id, page=page, page_size=page_size, search=search, search_operator=search_operator, function_search=function_search, order_by=order_by, sort_order=sort_order)
        print("The response of AnalysesCoreApi->v3_get_analysis_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis_strings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **page** | **int**| Page number (1-indexed). | [optional] [default to 1]
 **page_size** | **int**| Number of results per page. | [optional] [default to 100]
 **search** | **str**| Filter by string value (case-insensitive substring match). | [optional] 
 **search_operator** | **str**| How the search term matches string values. | [optional] [default to CONTAINS]
 **function_search** | **str**| Filter by function name (case-insensitive substring match). | [optional] 
 **order_by** | **str**| Field to order results by. | [optional] [default to value]
 **sort_order** | **str**| Sort direction. | [optional] [default to ASC]

### Return type

[**ListAnalysisStringsOutputBody**](ListAnalysisStringsOutputBody.md)

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

# **v3_get_analysis_strings_status**
> GetAnalysisStringsStatusOutputBody v3_get_analysis_strings_status(analysis_id)

Get the string-extraction status for an analysis.

Returns the status of the string-extraction task for the binary backing the analysis. One of UNINITIALISED, PENDING, RUNNING, COMPLETED, FAILED.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_analysis_strings_status_output_body import GetAnalysisStringsStatusOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get the string-extraction status for an analysis.
        api_response = api_instance.v3_get_analysis_strings_status(analysis_id)
        print("The response of AnalysesCoreApi->v3_get_analysis_strings_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_analysis_strings_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**GetAnalysisStringsStatusOutputBody**](GetAnalysisStringsStatusOutputBody.md)

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

# **v3_get_binary_export_operation**
> OperationBinaryExportMetadataBinaryExportResult v3_get_binary_export_operation(task_id)

Get a binary export operation

Returns the current state of the export started for this task ID. `done` is the only readiness signal: while false, poll again; once true, exactly one of `response` or `error` is set. A task ID the platform no longer recognises -- whether it never existed or its history has expired -- resolves to a failed operation, since either way the caller must export again.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_binary_export_metadata_binary_export_result import OperationBinaryExportMetadataBinaryExportResult
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    task_id = 'task_id_example' # str | Task ID returned by queueing the export

    try:
        # Get a binary export operation
        api_response = api_instance.v3_get_binary_export_operation(task_id)
        print("The response of AnalysesCoreApi->v3_get_binary_export_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_get_binary_export_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task ID returned by queueing the export | 

### Return type

[**OperationBinaryExportMetadataBinaryExportResult**](OperationBinaryExportMetadataBinaryExportResult.md)

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

# **v3_list_analyses**
> ListAnalysesOutputBody v3_list_analyses(search_term=search_term, analysis_scope=analysis_scope, status=status, model_name=model_name, usernames=usernames, sha256_hash=sha256_hash, binary_id=binary_id, platform=platform, architecture=architecture, page_size=page_size, next_page_token=next_page_token, order_by=order_by, order=order)

List analyses

Returns a page of analyses visible to the caller, filtered and ordered by the query parameters.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_analyses_output_body import ListAnalysesOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    search_term = 'search_term_example' # str |  (optional)
    analysis_scope = ['analysis_scope_example'] # List[str] | Leave empty to search your own, your team's and all public analyses (optional)
    status = ['status_example'] # List[str] |  (optional)
    model_name = ['model_name_example'] # List[Optional[str]] |  (optional)
    usernames = ['usernames_example'] # List[Optional[str]] |  (optional)
    sha256_hash = 'sha256_hash_example' # str |  (optional)
    binary_id = 56 # int | Restrict to analyses of this binary. A binary can carry more than one analysis; they are returned newest first under the default sort (optional)
    platform = ['platform_example'] # List[str] | Restrict to binaries running on one of these operating-system platforms. Matches the uploader's override when they set one, the detected platform otherwise; a binary with neither is never matched. Leave empty for no filter (optional)
    architecture = ['architecture_example'] # List[str] | Restrict to binaries built for one of these instruction-set architectures. Resolved the same way as platform. Leave empty for no filter (optional)
    page_size = 20 # int |  (optional) (default to 20)
    next_page_token = 'next_page_token_example' # str | Forward-pagination cursor from a prior response. When set, order_by/order are taken from the token (the sort cannot change mid-pagination). (optional)
    order_by = created # str |  (optional) (default to created)
    order = DESC # str |  (optional) (default to DESC)

    try:
        # List analyses
        api_response = api_instance.v3_list_analyses(search_term=search_term, analysis_scope=analysis_scope, status=status, model_name=model_name, usernames=usernames, sha256_hash=sha256_hash, binary_id=binary_id, platform=platform, architecture=architecture, page_size=page_size, next_page_token=next_page_token, order_by=order_by, order=order)
        print("The response of AnalysesCoreApi->v3_list_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_list_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 
 **analysis_scope** | [**List[str]**](str.md)| Leave empty to search your own, your team&#39;s and all public analyses | [optional] 
 **status** | [**List[str]**](str.md)|  | [optional] 
 **model_name** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **usernames** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **sha256_hash** | **str**|  | [optional] 
 **binary_id** | **int**| Restrict to analyses of this binary. A binary can carry more than one analysis; they are returned newest first under the default sort | [optional] 
 **platform** | [**List[str]**](str.md)| Restrict to binaries running on one of these operating-system platforms. Matches the uploader&#39;s override when they set one, the detected platform otherwise; a binary with neither is never matched. Leave empty for no filter | [optional] 
 **architecture** | [**List[str]**](str.md)| Restrict to binaries built for one of these instruction-set architectures. Resolved the same way as platform. Leave empty for no filter | [optional] 
 **page_size** | **int**|  | [optional] [default to 20]
 **next_page_token** | **str**| Forward-pagination cursor from a prior response. When set, order_by/order are taken from the token (the sort cannot change mid-pagination). | [optional] 
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**ListAnalysesOutputBody**](ListAnalysesOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_list_example_analyses**
> ListExampleAnalysesOutputBody v3_list_example_analyses()

List example analyses

Returns the curated example Analyses.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_example_analyses_output_body import ListExampleAnalysesOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)

    try:
        # List example analyses
        api_response = api_instance.v3_list_example_analyses()
        print("The response of AnalysesCoreApi->v3_list_example_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_list_example_analyses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListExampleAnalysesOutputBody**](ListExampleAnalysesOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_lookup_analysis_by_binary_id**
> LookupAnalysisByBinaryIDOutputBody v3_lookup_analysis_by_binary_id(binary_id)

Look up the most recent analysis for a binary.

Returns the ID of the most recent analysis of this binary that the caller may see (their own, their team's, or public). Returns 404 if the binary has none, whether because it has never been analysed or because every analysis of it is private to someone else.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.lookup_analysis_by_binary_id_output_body import LookupAnalysisByBinaryIDOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Look up the most recent analysis for a binary.
        api_response = api_instance.v3_lookup_analysis_by_binary_id(binary_id)
        print("The response of AnalysesCoreApi->v3_lookup_analysis_by_binary_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_lookup_analysis_by_binary_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**LookupAnalysisByBinaryIDOutputBody**](LookupAnalysisByBinaryIDOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_queue_binary_export**
> OperationBinaryExportMetadataBinaryExportResult v3_queue_binary_export(analysis_id)

Queue a binary export

Starts an asynchronous export of the binary with its current symbols rewritten in, and returns the operation to poll for its outcome. Only the owner may call it, and it requires a subscription tier that supports symbol export. Download the result once the operation reports done.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_binary_export_metadata_binary_export_result import OperationBinaryExportMetadataBinaryExportResult
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Queue a binary export
        api_response = api_instance.v3_queue_binary_export(analysis_id)
        print("The response of AnalysesCoreApi->v3_queue_binary_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_queue_binary_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**OperationBinaryExportMetadataBinaryExportResult**](OperationBinaryExportMetadataBinaryExportResult.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_update_analysis**
> AnalysisDetailOutputBody v3_update_analysis(analysis_id, update_analysis_input_body)

Update an analysis.

Renames the analysis' binary and/or changes its scope. Only the owner may call it. Changing to a non-PUBLIC scope requires a subscription tier that supports private analyses.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_detail_output_body import AnalysisDetailOutputBody
from revengai.models.update_analysis_input_body import UpdateAnalysisInputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    update_analysis_input_body = revengai.UpdateAnalysisInputBody() # UpdateAnalysisInputBody | 

    try:
        # Update an analysis.
        api_response = api_instance.v3_update_analysis(analysis_id, update_analysis_input_body)
        print("The response of AnalysesCoreApi->v3_update_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_update_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **update_analysis_input_body** | [**UpdateAnalysisInputBody**](UpdateAnalysisInputBody.md)|  | 

### Return type

[**AnalysisDetailOutputBody**](AnalysisDetailOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_upgrade_analysis_model**
> UpgradeAnalysisModelOutputBody v3_upgrade_analysis_model(analysis_id)

Re-analyse on the latest model

Re-runs an analysis created on an older model against the current unified model, in place — the analysis ID does not change. No credits are consumed. Only the owner may call it, and only once the analysis has settled: the pipeline clears the binary's functions, names, data types and signatures before re-running. Returns 409 if the analysis is already on the latest model, or is still running. Poll `GET /v3/analyses/{analysis_id}/basic` for status, as with any other run.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.upgrade_analysis_model_output_body import UpgradeAnalysisModelOutputBody
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Re-analyse on the latest model
        api_response = api_instance.v3_upgrade_analysis_model(analysis_id)
        print("The response of AnalysesCoreApi->v3_upgrade_analysis_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->v3_upgrade_analysis_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**UpgradeAnalysisModelOutputBody**](UpgradeAnalysisModelOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

