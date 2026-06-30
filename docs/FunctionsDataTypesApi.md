# revengai.FunctionsDataTypesApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_function_data_types**](FunctionsDataTypesApi.md#batch_update_function_data_types) | **PUT** /v3/analyses/{analysis_id}/functions/data-types | Batch update function data types
[**generate_function_data_types_for_analysis**](FunctionsDataTypesApi.md#generate_function_data_types_for_analysis) | **POST** /v2/analyses/{analysis_id}/functions/data_types | Generate Function Data Types
[**generate_function_data_types_for_functions**](FunctionsDataTypesApi.md#generate_function_data_types_for_functions) | **POST** /v2/functions/data_types | Generate Function Data Types for an arbitrary list of functions
[**get_function_data_types**](FunctionsDataTypesApi.md#get_function_data_types) | **GET** /v3/analyses/{analysis_id}/functions/{function_id}/data-types | Get data types for a single function
[**list_analysis_functions_data_types**](FunctionsDataTypesApi.md#list_analysis_functions_data_types) | **GET** /v3/analyses/{analysis_id}/functions/data-types | List data types for all functions in an analysis
[**list_function_data_types_for_analysis**](FunctionsDataTypesApi.md#list_function_data_types_for_analysis) | **GET** /v2/analyses/{analysis_id}/functions/data_types | List Function Data Types
[**list_function_data_types_for_functions**](FunctionsDataTypesApi.md#list_function_data_types_for_functions) | **GET** /v2/functions/data_types | List Function Data Types
[**list_functions_data_types**](FunctionsDataTypesApi.md#list_functions_data_types) | **GET** /v3/functions/data-types | Get data types for many functions
[**update_function_data_types**](FunctionsDataTypesApi.md#update_function_data_types) | **PUT** /v2/analyses/{analysis_id}/functions/{function_id}/data_types | Update function data types


# **batch_update_function_data_types**
> BatchUpdateDataTypesOutputBody batch_update_function_data_types(analysis_id, batch_update_data_types_input_body)

Batch update function data types

Updates data types for multiple functions in one analysis. All function IDs in the body must belong to the analysis. Each item is processed independently and reports its own outcome: a stale `data_types_version` yields `version_conflict` for that item without affecting the rest of the batch.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.batch_update_data_types_input_body import BatchUpdateDataTypesInputBody
from revengai.models.batch_update_data_types_output_body import BatchUpdateDataTypesOutputBody
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    batch_update_data_types_input_body = revengai.BatchUpdateDataTypesInputBody() # BatchUpdateDataTypesInputBody | 

    try:
        # Batch update function data types
        api_response = api_instance.batch_update_function_data_types(analysis_id, batch_update_data_types_input_body)
        print("The response of FunctionsDataTypesApi->batch_update_function_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->batch_update_function_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **batch_update_data_types_input_body** | [**BatchUpdateDataTypesInputBody**](BatchUpdateDataTypesInputBody.md)|  | 

### Return type

[**BatchUpdateDataTypesOutputBody**](BatchUpdateDataTypesOutputBody.md)

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

# **generate_function_data_types_for_analysis**
> BaseResponseGenerateFunctionDataTypes generate_function_data_types_for_analysis(analysis_id, function_data_types_params)

Generate Function Data Types

Submits a request to generate the function data types

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_generate_function_data_types import BaseResponseGenerateFunctionDataTypes
from revengai.models.function_data_types_params import FunctionDataTypesParams
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    analysis_id = 56 # int | 
    function_data_types_params = revengai.FunctionDataTypesParams() # FunctionDataTypesParams | 

    try:
        # Generate Function Data Types
        api_response = api_instance.generate_function_data_types_for_analysis(analysis_id, function_data_types_params)
        print("The response of FunctionsDataTypesApi->generate_function_data_types_for_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->generate_function_data_types_for_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **function_data_types_params** | [**FunctionDataTypesParams**](FunctionDataTypesParams.md)|  | 

### Return type

[**BaseResponseGenerateFunctionDataTypes**](BaseResponseGenerateFunctionDataTypes.md)

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

# **generate_function_data_types_for_functions**
> BaseResponseGenerationStatusList generate_function_data_types_for_functions(function_data_types_params)

Generate Function Data Types for an arbitrary list of functions

Submits a request to generate the function data types

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_generation_status_list import BaseResponseGenerationStatusList
from revengai.models.function_data_types_params import FunctionDataTypesParams
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    function_data_types_params = revengai.FunctionDataTypesParams() # FunctionDataTypesParams | 

    try:
        # Generate Function Data Types for an arbitrary list of functions
        api_response = api_instance.generate_function_data_types_for_functions(function_data_types_params)
        print("The response of FunctionsDataTypesApi->generate_function_data_types_for_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->generate_function_data_types_for_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_data_types_params** | [**FunctionDataTypesParams**](FunctionDataTypesParams.md)|  | 

### Return type

[**BaseResponseGenerationStatusList**](BaseResponseGenerationStatusList.md)

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

# **get_function_data_types**
> DataTypesEntry get_function_data_types(analysis_id, function_id)

Get data types for a single function

Returns the stored data-types blob for one function. The function must belong to the supplied analysis.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.data_types_entry import DataTypesEntry
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    function_id = 56 # int | Function ID

    try:
        # Get data types for a single function
        api_response = api_instance.get_function_data_types(analysis_id, function_id)
        print("The response of FunctionsDataTypesApi->get_function_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->get_function_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **function_id** | **int**| Function ID | 

### Return type

[**DataTypesEntry**](DataTypesEntry.md)

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

# **list_analysis_functions_data_types**
> ListAnalysisFunctionsDataTypesOutputBody list_analysis_functions_data_types(analysis_id, offset=offset, limit=limit)

List data types for all functions in an analysis

Paginated read of the stored data-types blob for each function in the analysis.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_analysis_functions_data_types_output_body import ListAnalysisFunctionsDataTypesOutputBody
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    offset = 56 # int | Pagination offset. Defaults to 0. (optional)
    limit = 56 # int | Page size. Defaults to 100. (optional)

    try:
        # List data types for all functions in an analysis
        api_response = api_instance.list_analysis_functions_data_types(analysis_id, offset=offset, limit=limit)
        print("The response of FunctionsDataTypesApi->list_analysis_functions_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->list_analysis_functions_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **offset** | **int**| Pagination offset. Defaults to 0. | [optional] 
 **limit** | **int**| Page size. Defaults to 100. | [optional] 

### Return type

[**ListAnalysisFunctionsDataTypesOutputBody**](ListAnalysisFunctionsDataTypesOutputBody.md)

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

# **list_function_data_types_for_analysis**
> BaseResponseFunctionDataTypesList list_function_data_types_for_analysis(analysis_id, function_ids=function_ids)

List Function Data Types

Returns data types for multiple functions with optional function ID filtering

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_function_data_types_list import BaseResponseFunctionDataTypesList
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    analysis_id = 56 # int | 
    function_ids = [56] # List[Optional[int]] |  (optional)

    try:
        # List Function Data Types
        api_response = api_instance.list_function_data_types_for_analysis(analysis_id, function_ids=function_ids)
        print("The response of FunctionsDataTypesApi->list_function_data_types_for_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->list_function_data_types_for_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **function_ids** | [**List[Optional[int]]**](int.md)|  | [optional] 

### Return type

[**BaseResponseFunctionDataTypesList**](BaseResponseFunctionDataTypesList.md)

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

# **list_function_data_types_for_functions**
> BaseResponseFunctionDataTypesList list_function_data_types_for_functions(function_ids=function_ids)

List Function Data Types

Returns data types for multiple function IDs

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_function_data_types_list import BaseResponseFunctionDataTypesList
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    function_ids = [56] # List[Optional[int]] |  (optional)

    try:
        # List Function Data Types
        api_response = api_instance.list_function_data_types_for_functions(function_ids=function_ids)
        print("The response of FunctionsDataTypesApi->list_function_data_types_for_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->list_function_data_types_for_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_ids** | [**List[Optional[int]]**](int.md)|  | [optional] 

### Return type

[**BaseResponseFunctionDataTypesList**](BaseResponseFunctionDataTypesList.md)

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

# **list_functions_data_types**
> ListFunctionsDataTypesOutputBody list_functions_data_types(function_ids)

Get data types for many functions

Returns the stored data-types blob for each supplied function ID. Caller must have read access to every function or the request is rejected.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_functions_data_types_output_body import ListFunctionsDataTypesOutputBody
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    function_ids = [56] # List[int] | Function IDs to fetch data-types for.

    try:
        # Get data types for many functions
        api_response = api_instance.list_functions_data_types(function_ids)
        print("The response of FunctionsDataTypesApi->list_functions_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->list_functions_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_ids** | [**List[int]**](int.md)| Function IDs to fetch data-types for. | 

### Return type

[**ListFunctionsDataTypesOutputBody**](ListFunctionsDataTypesOutputBody.md)

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

# **update_function_data_types**
> UpdateDataTypesOutputBody update_function_data_types(analysis_id, function_id, update_data_types_input_body)

Update function data types

Stores user-specific overrides for a function's data types. Uses optimistic concurrency: if the stored version doesn't match `data_types_version`, the update is rejected with 409.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.update_data_types_input_body import UpdateDataTypesInputBody
from revengai.models.update_data_types_output_body import UpdateDataTypesOutputBody
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
    api_instance = revengai.FunctionsDataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    function_id = 56 # int | Function ID
    update_data_types_input_body = revengai.UpdateDataTypesInputBody() # UpdateDataTypesInputBody | 

    try:
        # Update function data types
        api_response = api_instance.update_function_data_types(analysis_id, function_id, update_data_types_input_body)
        print("The response of FunctionsDataTypesApi->update_function_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsDataTypesApi->update_function_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **function_id** | **int**| Function ID | 
 **update_data_types_input_body** | [**UpdateDataTypesInputBody**](UpdateDataTypesInputBody.md)|  | 

### Return type

[**UpdateDataTypesOutputBody**](UpdateDataTypesOutputBody.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

