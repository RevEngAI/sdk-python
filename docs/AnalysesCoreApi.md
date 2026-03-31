# revengai.AnalysesCoreApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_add_analysis_tags**](AnalysesCoreApi.md#bulk_add_analysis_tags) | **PATCH** /v2/analyses/tags/add | Bulk Add Analysis Tags
[**create_analysis**](AnalysesCoreApi.md#create_analysis) | **POST** /v2/analyses | Create Analysis
[**delete_analysis**](AnalysesCoreApi.md#delete_analysis) | **DELETE** /v2/analyses/{analysis_id} | Delete Analysis
[**get_analysis_basic_info**](AnalysesCoreApi.md#get_analysis_basic_info) | **GET** /v2/analyses/{analysis_id}/basic | Gets basic analysis information
[**get_analysis_function_map**](AnalysesCoreApi.md#get_analysis_function_map) | **GET** /v2/analyses/{analysis_id}/func_maps | Get Analysis Function Map
[**get_analysis_logs**](AnalysesCoreApi.md#get_analysis_logs) | **GET** /v2/analyses/{analysis_id}/logs | Gets the logs of an analysis
[**get_analysis_params**](AnalysesCoreApi.md#get_analysis_params) | **GET** /v2/analyses/{analysis_id}/params | Gets analysis param information
[**get_analysis_status**](AnalysesCoreApi.md#get_analysis_status) | **GET** /v2/analyses/{analysis_id}/status | Gets the status of an analysis
[**insert_analysis_log**](AnalysesCoreApi.md#insert_analysis_log) | **POST** /v2/analyses/{analysis_id}/logs | Insert a log entry for an analysis
[**list_analyses**](AnalysesCoreApi.md#list_analyses) | **GET** /v2/analyses/list | Gets the most recent analyses
[**lookup_binary_id**](AnalysesCoreApi.md#lookup_binary_id) | **GET** /v2/analyses/lookup/{binary_id} | Gets the analysis ID from binary ID
[**put_analysis_strings**](AnalysesCoreApi.md#put_analysis_strings) | **PUT** /v2/analyses/{analysis_id}/strings | Add strings to the analysis
[**requeue_analysis**](AnalysesCoreApi.md#requeue_analysis) | **POST** /v2/analyses/{analysis_id}/requeue | Requeue Analysis
[**update_analysis**](AnalysesCoreApi.md#update_analysis) | **PATCH** /v2/analyses/{analysis_id} | Update Analysis
[**update_analysis_tags**](AnalysesCoreApi.md#update_analysis_tags) | **PATCH** /v2/analyses/{analysis_id}/tags | Update Analysis Tags
[**upload_file**](AnalysesCoreApi.md#upload_file) | **POST** /v2/upload | Upload File


# **bulk_add_analysis_tags**
> BaseResponseAnalysisBulkAddTagsResponse bulk_add_analysis_tags(analysis_bulk_add_tags_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Bulk Add Analysis Tags

Updates analysis tags for multiple analyses. User must be the owner.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.analysis_bulk_add_tags_request import AnalysisBulkAddTagsRequest
from revengai.models.base_response_analysis_bulk_add_tags_response import BaseResponseAnalysisBulkAddTagsResponse
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
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_bulk_add_tags_request = revengai.AnalysisBulkAddTagsRequest() # AnalysisBulkAddTagsRequest | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Bulk Add Analysis Tags
        api_response = api_instance.bulk_add_analysis_tags(analysis_bulk_add_tags_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
        print("The response of AnalysesCoreApi->bulk_add_analysis_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->bulk_add_analysis_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_bulk_add_tags_request** | [**AnalysisBulkAddTagsRequest**](AnalysisBulkAddTagsRequest.md)|  | 
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseAnalysisBulkAddTagsResponse**](BaseResponseAnalysisBulkAddTagsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis**
> BaseResponseAnalysisCreateResponse create_analysis(analysis_create_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts, x_rev_eng_application=x_rev_eng_application)

Create Analysis

Begins an analysis

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_create_request = revengai.AnalysisCreateRequest() # AnalysisCreateRequest | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)
    x_rev_eng_application = 'x_rev_eng_application_example' # str |  (optional)

    try:
        # Create Analysis
        api_response = api_instance.create_analysis(analysis_create_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts, x_rev_eng_application=x_rev_eng_application)
        print("The response of AnalysesCoreApi->create_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->create_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_create_request** | [**AnalysisCreateRequest**](AnalysisCreateRequest.md)|  | 
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]
 **x_rev_eng_application** | **str**|  | [optional] 

### Return type

[**BaseResponseAnalysisCreateResponse**](BaseResponseAnalysisCreateResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

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

# **delete_analysis**
> BaseResponseDict delete_analysis(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Delete Analysis

Deletes an analysis based on the provided analysis ID.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Delete Analysis
        api_response = api_instance.delete_analysis(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
        print("The response of AnalysesCoreApi->delete_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->delete_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseDict**](BaseResponseDict.md)

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
**404** | Not Found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_basic_info**
> BaseResponseBasic get_analysis_basic_info(analysis_id)

Gets basic analysis information

Returns basic analysis information for an analysis

### Example

* Api Key Authentication (APIKey):

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

# **get_analysis_function_map**
> BaseResponseAnalysisFunctionMapping get_analysis_function_map(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Get Analysis Function Map

Returns three maps: a map of function ids to function addresses, it's inverse and a map of function addresses to function names.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Get Analysis Function Map
        api_response = api_instance.get_analysis_function_map(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
        print("The response of AnalysesCoreApi->get_analysis_function_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_function_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseAnalysisFunctionMapping**](BaseResponseAnalysisFunctionMapping.md)

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

# **get_analysis_logs**
> BaseResponseLogs get_analysis_logs(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Gets the logs of an analysis

Given an analysis ID gets the current logs of an analysis

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Gets the logs of an analysis
        api_response = api_instance.get_analysis_logs(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
        print("The response of AnalysesCoreApi->get_analysis_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseLogs**](BaseResponseLogs.md)

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

# **get_analysis_params**
> BaseResponseParams get_analysis_params(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Gets analysis param information

Gets the params that the analysis was run with

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Gets analysis param information
        api_response = api_instance.get_analysis_params(analysis_id, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
        print("The response of AnalysesCoreApi->get_analysis_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseParams**](BaseResponseParams.md)

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

# **get_analysis_status**
> BaseResponseStatus get_analysis_status(analysis_id)

Gets the status of an analysis

Given an analysis ID gets the current status of the analysis

### Example

* Api Key Authentication (APIKey):

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

# **insert_analysis_log**
> BaseResponse insert_analysis_log(analysis_id, insert_analysis_log_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Insert a log entry for an analysis

Inserts a log record for an analysis. Only the analysis owner can insert logs.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    insert_analysis_log_request = revengai.InsertAnalysisLogRequest() # InsertAnalysisLogRequest | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Insert a log entry for an analysis
        api_response = api_instance.insert_analysis_log(analysis_id, insert_analysis_log_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
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
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

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

```python
import revengai
from revengai.models.app_api_rest_v2_analyses_enums_order_by import AppApiRestV2AnalysesEnumsOrderBy
from revengai.models.base_response_recent import BaseResponseRecent
from revengai.models.dynamic_execution_status_input import DynamicExecutionStatusInput
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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    search_term = '' # str |  (optional) (default to '')
    workspace = ["personal"] # List[Workspace] | The workspace to be viewed (optional) (default to ["personal"])
    status = ["All"] # List[StatusInput] | The status of the analysis (optional) (default to ["All"])
    model_name = [revengai.ModelName()] # List[ModelName] | Show analysis belonging to the model (optional)
    dynamic_execution_status = revengai.DynamicExecutionStatusInput() # DynamicExecutionStatusInput | Show analysis that have a dynamic execution with the given status (optional)
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
 **dynamic_execution_status** | [**DynamicExecutionStatusInput**](.md)| Show analysis that have a dynamic execution with the given status | [optional] 
 **usernames** | [**List[Optional[str]]**](str.md)| Show analysis belonging to the user | [optional] [default to []]
 **sha256_hash** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | [**AppApiRestV2AnalysesEnumsOrderBy**](.md)|  | [optional] 
 **order** | [**Order**](.md)|  | [optional] 

### Return type

[**BaseResponseRecent**](BaseResponseRecent.md)

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

# **lookup_binary_id**
> object lookup_binary_id(binary_id)

Gets the analysis ID from binary ID

Given an binary ID gets the ID of an analysis

### Example

* Api Key Authentication (APIKey):

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

# **put_analysis_strings**
> BaseResponse put_analysis_strings(analysis_id, put_analysis_strings_request)

Add strings to the analysis

Add strings to the analysis. Rejects if any string already exists at the given vaddr.

### Example

* Api Key Authentication (APIKey):

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

[APIKey](../README.md#APIKey)

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
> BaseResponseCreated requeue_analysis(analysis_id, re_analysis_form, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts, x_rev_eng_application=x_rev_eng_application)

Requeue Analysis

Re-queues an already uploaded analysis

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    re_analysis_form = revengai.ReAnalysisForm() # ReAnalysisForm | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)
    x_rev_eng_application = 'x_rev_eng_application_example' # str |  (optional)

    try:
        # Requeue Analysis
        api_response = api_instance.requeue_analysis(analysis_id, re_analysis_form, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts, x_rev_eng_application=x_rev_eng_application)
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
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]
 **x_rev_eng_application** | **str**|  | [optional] 

### Return type

[**BaseResponseCreated**](BaseResponseCreated.md)

### Authorization

[APIKey](../README.md#APIKey)

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

# **update_analysis**
> BaseResponseAnalysisDetailResponse update_analysis(analysis_id, analysis_update_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Update Analysis

Updates analysis attributes (binary_name, analysis_scope). User must be the owner.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    analysis_update_request = revengai.AnalysisUpdateRequest() # AnalysisUpdateRequest | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Update Analysis
        api_response = api_instance.update_analysis(analysis_id, analysis_update_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
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
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseAnalysisDetailResponse**](BaseResponseAnalysisDetailResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

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
> BaseResponseAnalysisUpdateTagsResponse update_analysis_tags(analysis_id, analysis_update_tags_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)

Update Analysis Tags

Updates analysis tags. User must be the owner.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 56 # int | 
    analysis_update_tags_request = revengai.AnalysisUpdateTagsRequest() # AnalysisUpdateTagsRequest | 
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)

    try:
        # Update Analysis Tags
        api_response = api_instance.update_analysis_tags(analysis_id, analysis_update_tags_request, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts)
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
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]

### Return type

[**BaseResponseAnalysisUpdateTagsResponse**](BaseResponseAnalysisUpdateTagsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

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
> BaseResponseUploadResponse upload_file(upload_file_type, file, packed_password=packed_password, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts, force_overwrite=force_overwrite)

Upload File

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    upload_file_type = revengai.UploadFileType() # UploadFileType | 
    file = None # bytearray | 
    packed_password = 'packed_password_example' # str |  (optional)
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    local_cache_dir = 'local_cache_dir_example' # str |  (optional)
    local_cache_max_size_mb = 56 # int |  (optional)
    customer_samples_bucket = 'customer_samples_bucket_example' # str |  (optional)
    firmware_samples_bucket = 'firmware_samples_bucket_example' # str |  (optional)
    max_retry_attempts = 5 # int |  (optional) (default to 5)
    force_overwrite = False # bool |  (optional) (default to False)

    try:
        # Upload File
        api_response = api_instance.upload_file(upload_file_type, file, packed_password=packed_password, endpoint_url=endpoint_url, local_cache_dir=local_cache_dir, local_cache_max_size_mb=local_cache_max_size_mb, customer_samples_bucket=customer_samples_bucket, firmware_samples_bucket=firmware_samples_bucket, max_retry_attempts=max_retry_attempts, force_overwrite=force_overwrite)
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
 **endpoint_url** | **str**|  | [optional] 
 **local_cache_dir** | **str**|  | [optional] 
 **local_cache_max_size_mb** | **int**|  | [optional] 
 **customer_samples_bucket** | **str**|  | [optional] 
 **firmware_samples_bucket** | **str**|  | [optional] 
 **max_retry_attempts** | **int**|  | [optional] [default to 5]
 **force_overwrite** | **bool**|  | [optional] [default to False]

### Return type

[**BaseResponseUploadResponse**](BaseResponseUploadResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

