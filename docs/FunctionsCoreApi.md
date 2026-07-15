# revengai.FunctionsCoreApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_function_callee**](FunctionsCoreApi.md#add_function_callee) | **POST** /v3/functions/{function_id}/callees | Add a callee to a function
[**add_user_string_to_function**](FunctionsCoreApi.md#add_user_string_to_function) | **POST** /v3/functions/{function_id}/user-provided-strings | Add a user-provided string to a function.
[**get_analysis_strings**](FunctionsCoreApi.md#get_analysis_strings) | **GET** /v2/analyses/{analysis_id}/functions/strings | Get string information found in the Analysis
[**get_analysis_strings_status**](FunctionsCoreApi.md#get_analysis_strings_status) | **GET** /v2/analyses/{analysis_id}/functions/strings/status | Get string processing state for the Analysis
[**get_function_blocks**](FunctionsCoreApi.md#get_function_blocks) | **GET** /v2/functions/{function_id}/blocks | Get disassembly blocks related to the function
[**get_function_blocks_0**](FunctionsCoreApi.md#get_function_blocks_0) | **GET** /v3/functions/{function_id}/blocks | Get function disassembly
[**get_function_callees_callers**](FunctionsCoreApi.md#get_function_callees_callers) | **GET** /v2/functions/{function_id}/callees_callers | Get list of functions that call or are called by the specified function
[**get_function_callees_callers_0**](FunctionsCoreApi.md#get_function_callees_callers_0) | **GET** /v3/functions/{function_id}/callees-callers | Get callees and callers for a function
[**get_function_callees_callers_bulk**](FunctionsCoreApi.md#get_function_callees_callers_bulk) | **GET** /v2/functions/callees_callers | Get list of functions that call or are called for a list of functions
[**get_function_capabilities**](FunctionsCoreApi.md#get_function_capabilities) | **GET** /v2/functions/{function_id}/capabilities | Retrieve a functions capabilities
[**get_function_capabilities_0**](FunctionsCoreApi.md#get_function_capabilities_0) | **GET** /v3/functions/{function_id}/capabilities | Get capabilities for a function
[**get_function_details**](FunctionsCoreApi.md#get_function_details) | **GET** /v2/functions/{function_id} | Get function details
[**get_function_details_0**](FunctionsCoreApi.md#get_function_details_0) | **GET** /v3/functions/{function_id} | Get function details
[**get_function_indirect_call_sites**](FunctionsCoreApi.md#get_function_indirect_call_sites) | **GET** /v3/functions/{function_id}/indirect-call-sites | Get indirect call sites for a function
[**get_function_strings**](FunctionsCoreApi.md#get_function_strings) | **GET** /v2/functions/{function_id}/strings | Get string information found in the function
[**get_function_strings_0**](FunctionsCoreApi.md#get_function_strings_0) | **GET** /v3/functions/{function_id}/strings | List strings for a function.
[**get_functions_callees_callers**](FunctionsCoreApi.md#get_functions_callees_callers) | **GET** /v3/functions/callees-callers | Get callees and callers for many functions
[**get_functions_matches**](FunctionsCoreApi.md#get_functions_matches) | **GET** /v3/functions/matches | Get function-matching results for an explicit set of functions
[**get_functions_matching_status**](FunctionsCoreApi.md#get_functions_matching_status) | **GET** /v3/functions/matches/status | Get function-matching status for an explicit set of functions
[**get_imported_function**](FunctionsCoreApi.md#get_imported_function) | **GET** /v3/analyses/{analysis_id}/imported-functions/{imported_function_id} | Get an imported function with its callers
[**list_analysis_functions**](FunctionsCoreApi.md#list_analysis_functions) | **GET** /v3/analyses/{analysis_id}/functions | List functions in an analysis
[**list_imported_functions**](FunctionsCoreApi.md#list_imported_functions) | **GET** /v3/analyses/{analysis_id}/imported-functions | List imported functions in an analysis
[**start_functions_matching**](FunctionsCoreApi.md#start_functions_matching) | **POST** /v3/functions/matches | Start function matching for an explicit set of functions
[**v3_canonicalize_function_names**](FunctionsCoreApi.md#v3_canonicalize_function_names) | **POST** /v3/functions/canonical-names | Canonicalize a batch of function names


# **add_function_callee**
> Dict[str, object] add_function_callee(function_id, add_callee_input_body)

Add a callee to a function

Records an outgoing call edge from the given function to a callee.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.add_callee_input_body import AddCalleeInputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID
    add_callee_input_body = revengai.AddCalleeInputBody() # AddCalleeInputBody | 

    try:
        # Add a callee to a function
        api_response = api_instance.add_function_callee(function_id, add_callee_input_body)
        print("The response of FunctionsCoreApi->add_function_callee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->add_function_callee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **add_callee_input_body** | [**AddCalleeInputBody**](AddCalleeInputBody.md)|  | 

### Return type

**Dict[str, object]**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_string_to_function**
> Dict[str, object] add_user_string_to_function(function_id, add_user_string_to_function_input_body)

Add a user-provided string to a function.

Attaches a user-provided string to a function at the given virtual address. The string is stored with source `USER` and complements strings discovered automatically during analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.add_user_string_to_function_input_body import AddUserStringToFunctionInputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID
    add_user_string_to_function_input_body = revengai.AddUserStringToFunctionInputBody() # AddUserStringToFunctionInputBody | 

    try:
        # Add a user-provided string to a function.
        api_response = api_instance.add_user_string_to_function(function_id, add_user_string_to_function_input_body)
        print("The response of FunctionsCoreApi->add_user_string_to_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->add_user_string_to_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **add_user_string_to_function_input_body** | [**AddUserStringToFunctionInputBody**](AddUserStringToFunctionInputBody.md)|  | 

### Return type

**Dict[str, object]**

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

# **get_analysis_strings**
> BaseResponseAnalysisStringsResponse get_analysis_strings(analysis_id, page=page, page_size=page_size, search=search, function_search=function_search, order_by=order_by, sort_order=sort_order)

Get string information found in the Analysis

Get string information found in the analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_analysis_strings_response import BaseResponseAnalysisStringsResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    analysis_id = 56 # int | 
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 100 # int | Number of items per page. (optional) (default to 100)
    search = 'search_example' # str | Search is applied to string value (optional)
    function_search = 'function_search_example' # str | Search is applied to function names (optional)
    order_by = value # str | Order by field (optional) (default to value)
    sort_order = ASC # str | Sort order for the results (optional) (default to ASC)

    try:
        # Get string information found in the Analysis
        api_response = api_instance.get_analysis_strings(analysis_id, page=page, page_size=page_size, search=search, function_search=function_search, order_by=order_by, sort_order=sort_order)
        print("The response of FunctionsCoreApi->get_analysis_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_analysis_strings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page. | [optional] [default to 100]
 **search** | **str**| Search is applied to string value | [optional] 
 **function_search** | **str**| Search is applied to function names | [optional] 
 **order_by** | **str**| Order by field | [optional] [default to value]
 **sort_order** | **str**| Sort order for the results | [optional] [default to ASC]

### Return type

[**BaseResponseAnalysisStringsResponse**](BaseResponseAnalysisStringsResponse.md)

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

# **get_analysis_strings_status**
> BaseResponseAnalysisStringsStatusResponse get_analysis_strings_status(analysis_id)

Get string processing state for the Analysis

Get string processing state for the Analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_analysis_strings_status_response import BaseResponseAnalysisStringsStatusResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get string processing state for the Analysis
        api_response = api_instance.get_analysis_strings_status(analysis_id)
        print("The response of FunctionsCoreApi->get_analysis_strings_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_analysis_strings_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseAnalysisStringsStatusResponse**](BaseResponseAnalysisStringsStatusResponse.md)

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

# **get_function_blocks**
> BaseResponseFunctionBlocksResponse get_function_blocks(function_id)

Get disassembly blocks related to the function

Get disassembly blocks related to the function

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_function_blocks_response import BaseResponseFunctionBlocksResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | 

    try:
        # Get disassembly blocks related to the function
        api_response = api_instance.get_function_blocks(function_id)
        print("The response of FunctionsCoreApi->get_function_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 

### Return type

[**BaseResponseFunctionBlocksResponse**](BaseResponseFunctionBlocksResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_blocks_0**
> DisassemblyOutputBody get_function_blocks_0(function_id)

Get function disassembly

Returns the function's disassembly metadata (JSON blob containing basic blocks + local variables) along with parameter and return-type info.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.disassembly_output_body import DisassemblyOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get function disassembly
        api_response = api_instance.get_function_blocks_0(function_id)
        print("The response of FunctionsCoreApi->get_function_blocks_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_blocks_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**DisassemblyOutputBody**](DisassemblyOutputBody.md)

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

# **get_function_callees_callers**
> BaseResponseCalleesCallerFunctionsResponse get_function_callees_callers(function_id)

Get list of functions that call or are called by the specified function

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_callees_caller_functions_response import BaseResponseCalleesCallerFunctionsResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | 

    try:
        # Get list of functions that call or are called by the specified function
        api_response = api_instance.get_function_callees_callers(function_id)
        print("The response of FunctionsCoreApi->get_function_callees_callers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_callees_callers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 

### Return type

[**BaseResponseCalleesCallerFunctionsResponse**](BaseResponseCalleesCallerFunctionsResponse.md)

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

# **get_function_callees_callers_0**
> CallEdgesOutputBody get_function_callees_callers_0(function_id)

Get callees and callers for a function

Returns both the outgoing call edges (callees) and incoming call edges (callers) for a single function.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.call_edges_output_body import CallEdgesOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get callees and callers for a function
        api_response = api_instance.get_function_callees_callers_0(function_id)
        print("The response of FunctionsCoreApi->get_function_callees_callers_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_callees_callers_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**CallEdgesOutputBody**](CallEdgesOutputBody.md)

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

# **get_function_callees_callers_bulk**
> BaseResponseListCalleesCallerFunctionsResponse get_function_callees_callers_bulk(function_ids)

Get list of functions that call or are called for a list of functions

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_list_callees_caller_functions_response import BaseResponseListCalleesCallerFunctionsResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_ids = [56] # List[Optional[int]] | 

    try:
        # Get list of functions that call or are called for a list of functions
        api_response = api_instance.get_function_callees_callers_bulk(function_ids)
        print("The response of FunctionsCoreApi->get_function_callees_callers_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_callees_callers_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_ids** | [**List[Optional[int]]**](int.md)|  | 

### Return type

[**BaseResponseListCalleesCallerFunctionsResponse**](BaseResponseListCalleesCallerFunctionsResponse.md)

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

# **get_function_capabilities**
> BaseResponseFunctionCapabilityResponse get_function_capabilities(function_id)

Retrieve a functions capabilities

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_function_capability_response import BaseResponseFunctionCapabilityResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | 

    try:
        # Retrieve a functions capabilities
        api_response = api_instance.get_function_capabilities(function_id)
        print("The response of FunctionsCoreApi->get_function_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 

### Return type

[**BaseResponseFunctionCapabilityResponse**](BaseResponseFunctionCapabilityResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_capabilities_0**
> CapabilitiesOutputBody get_function_capabilities_0(function_id)

Get capabilities for a function

Returns the capability findings (CAPA-style behaviour matches) associated with the given function.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.capabilities_output_body import CapabilitiesOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get capabilities for a function
        api_response = api_instance.get_function_capabilities_0(function_id)
        print("The response of FunctionsCoreApi->get_function_capabilities_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_capabilities_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**CapabilitiesOutputBody**](CapabilitiesOutputBody.md)

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

# **get_function_details**
> BaseResponseFunctionsDetailResponse get_function_details(function_id)

Get function details

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_functions_detail_response import BaseResponseFunctionsDetailResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | 

    try:
        # Get function details
        api_response = api_instance.get_function_details(function_id)
        print("The response of FunctionsCoreApi->get_function_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 

### Return type

[**BaseResponseFunctionsDetailResponse**](BaseResponseFunctionsDetailResponse.md)

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

# **get_function_details_0**
> FunctionDetailsOutputBody get_function_details_0(function_id)

Get function details

Returns metadata for a single function — name, virtual address, size, debug status, binary it belongs to.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.function_details_output_body import FunctionDetailsOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get function details
        api_response = api_instance.get_function_details_0(function_id)
        print("The response of FunctionsCoreApi->get_function_details_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_details_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**FunctionDetailsOutputBody**](FunctionDetailsOutputBody.md)

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

# **get_function_indirect_call_sites**
> IndirectCallSitesOutputBody get_function_indirect_call_sites(function_id)

Get indirect call sites for a function

Returns the function's indirect call instructions with their resolved call target.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.indirect_call_sites_output_body import IndirectCallSitesOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get indirect call sites for a function
        api_response = api_instance.get_function_indirect_call_sites(function_id)
        print("The response of FunctionsCoreApi->get_function_indirect_call_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_indirect_call_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**IndirectCallSitesOutputBody**](IndirectCallSitesOutputBody.md)

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

# **get_function_strings**
> BaseResponseFunctionStringsResponse get_function_strings(function_id, page=page, page_size=page_size, search=search)

Get string information found in the function

Get string information found in the function

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_function_strings_response import BaseResponseFunctionStringsResponse
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | 
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 100 # int | Number of items per page. (optional) (default to 100)
    search = 'search_example' # str | Search is applied to string value (optional)

    try:
        # Get string information found in the function
        api_response = api_instance.get_function_strings(function_id, page=page, page_size=page_size, search=search)
        print("The response of FunctionsCoreApi->get_function_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_strings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page. | [optional] [default to 100]
 **search** | **str**| Search is applied to string value | [optional] 

### Return type

[**BaseResponseFunctionStringsResponse**](BaseResponseFunctionStringsResponse.md)

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

# **get_function_strings_0**
> ListFunctionStringsOutputBody get_function_strings_0(function_id, page=page, page_size=page_size, search=search)

List strings for a function.

Returns the strings discovered in a function. Supports value search and pagination.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_function_strings_output_body import ListFunctionStringsOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_id = 56 # int | Function ID
    page = 1 # int | Page number (1-indexed). (optional) (default to 1)
    page_size = 100 # int | Number of results per page. (optional) (default to 100)
    search = 'search_example' # str | Filter by string value (case-insensitive substring match). (optional)

    try:
        # List strings for a function.
        api_response = api_instance.get_function_strings_0(function_id, page=page, page_size=page_size, search=search)
        print("The response of FunctionsCoreApi->get_function_strings_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_function_strings_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **page** | **int**| Page number (1-indexed). | [optional] [default to 1]
 **page_size** | **int**| Number of results per page. | [optional] [default to 100]
 **search** | **str**| Filter by string value (case-insensitive substring match). | [optional] 

### Return type

[**ListFunctionStringsOutputBody**](ListFunctionStringsOutputBody.md)

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

# **get_functions_callees_callers**
> CallEdgesOutputBody get_functions_callees_callers(function_ids)

Get callees and callers for many functions

Bulk variant — pass `function_ids` as a query parameter (comma-separated or repeated). Caller must have access to every supplied function or the whole request is rejected.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.call_edges_output_body import CallEdgesOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    function_ids = [56] # List[int] | Function IDs to fetch edges for.

    try:
        # Get callees and callers for many functions
        api_response = api_instance.get_functions_callees_callers(function_ids)
        print("The response of FunctionsCoreApi->get_functions_callees_callers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_functions_callees_callers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_ids** | [**List[int]**](int.md)| Function IDs to fetch edges for. | 

### Return type

[**CallEdgesOutputBody**](CallEdgesOutputBody.md)

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

# **get_functions_matches**
> GetMatchesOutputBody get_functions_matches(match_id=match_id, function_ids=function_ids)

Get function-matching results for an explicit set of functions

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
    api_instance = revengai.FunctionsCoreApi(api_client)
    match_id = 'match_id_example' # str | Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. (optional)
    function_ids = [56] # List[int] | Source function IDs whose matches to fetch. Required unless match_id is supplied. (optional)

    try:
        # Get function-matching results for an explicit set of functions
        api_response = api_instance.get_functions_matches(match_id=match_id, function_ids=function_ids)
        print("The response of FunctionsCoreApi->get_functions_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_functions_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. | [optional] 
 **function_ids** | [**List[int]**](int.md)| Source function IDs whose matches to fetch. Required unless match_id is supplied. | [optional] 

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

# **get_functions_matching_status**
> GetMatchesStatusOutputBody get_functions_matching_status(match_id=match_id, function_ids=function_ids)

Get function-matching status for an explicit set of functions

Returns the matching workflow's current status for the supplied function IDs. Does not include the matches blob — use GET /matches for that.

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
    api_instance = revengai.FunctionsCoreApi(api_client)
    match_id = 'match_id_example' # str | Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. (optional)
    function_ids = [56] # List[int] | Source function IDs whose matches to fetch. Required unless match_id is supplied. (optional)

    try:
        # Get function-matching status for an explicit set of functions
        api_response = api_instance.get_functions_matching_status(match_id=match_id, function_ids=function_ids)
        print("The response of FunctionsCoreApi->get_functions_matching_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_functions_matching_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| Opaque token from a start-matching response. When supplied, returns that specific run instead of the latest. | [optional] 
 **function_ids** | [**List[int]**](int.md)| Source function IDs whose matches to fetch. Required unless match_id is supplied. | [optional] 

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

# **get_imported_function**
> ImportedFunctionDetailOutputBody get_imported_function(analysis_id, imported_function_id)

Get an imported function with its callers

Returns a single imported symbol plus the internal functions that call it, resolved via the import's PLT/stub addresses within the binary. Answers "which functions call `free`?" for binary navigation.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.imported_function_detail_output_body import ImportedFunctionDetailOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    imported_function_id = 56 # int | Imported function ID

    try:
        # Get an imported function with its callers
        api_response = api_instance.get_imported_function(analysis_id, imported_function_id)
        print("The response of FunctionsCoreApi->get_imported_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->get_imported_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **imported_function_id** | **int**| Imported function ID | 

### Return type

[**ImportedFunctionDetailOutputBody**](ImportedFunctionDetailOutputBody.md)

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

# **list_analysis_functions**
> ListAnalysisFunctionsOutputBody list_analysis_functions(analysis_id, offset=offset, limit=limit)

List functions in an analysis

Returns a paginated list of functions belonging to the analysis. `total_count` is the full population size, ignoring pagination.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_analysis_functions_output_body import ListAnalysisFunctionsOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    offset = 56 # int | Pagination offset. Defaults to 0. (optional)
    limit = 56 # int | Page size. Defaults to 100. (optional)

    try:
        # List functions in an analysis
        api_response = api_instance.list_analysis_functions(analysis_id, offset=offset, limit=limit)
        print("The response of FunctionsCoreApi->list_analysis_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->list_analysis_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **offset** | **int**| Pagination offset. Defaults to 0. | [optional] 
 **limit** | **int**| Page size. Defaults to 100. | [optional] 

### Return type

[**ListAnalysisFunctionsOutputBody**](ListAnalysisFunctionsOutputBody.md)

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

# **list_imported_functions**
> ListImportedFunctionsOutputBody list_imported_functions(analysis_id, offset=offset, limit=limit)

List imported functions in an analysis

Returns a paginated list of external/imported symbols (e.g. libc's `free`) linked by the analysis's binary. These are display-only: they carry no embeddings, cannot be renamed, and never participate in match/diff. `total_count` is the full population size, ignoring pagination.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_imported_functions_output_body import ListImportedFunctionsOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    analysis_id = 56 # int | Analysis ID
    offset = 56 # int | Pagination offset. Defaults to 0. (optional)
    limit = 56 # int | Page size. Defaults to 100. (optional)

    try:
        # List imported functions in an analysis
        api_response = api_instance.list_imported_functions(analysis_id, offset=offset, limit=limit)
        print("The response of FunctionsCoreApi->list_imported_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->list_imported_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **offset** | **int**| Pagination offset. Defaults to 0. | [optional] 
 **limit** | **int**| Page size. Defaults to 100. | [optional] 

### Return type

[**ListImportedFunctionsOutputBody**](ListImportedFunctionsOutputBody.md)

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

# **start_functions_matching**
> StartMatchingOutputBody start_functions_matching(start_matching_for_functions_input_body)

Start function matching for an explicit set of functions

Dispatches the function-matching workflow against the provided function IDs. Returns immediately. Poll the status endpoint for progress; fetch results from the matches endpoint when status=COMPLETED.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.start_matching_for_functions_input_body import StartMatchingForFunctionsInputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    start_matching_for_functions_input_body = revengai.StartMatchingForFunctionsInputBody() # StartMatchingForFunctionsInputBody | 

    try:
        # Start function matching for an explicit set of functions
        api_response = api_instance.start_functions_matching(start_matching_for_functions_input_body)
        print("The response of FunctionsCoreApi->start_functions_matching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->start_functions_matching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_matching_for_functions_input_body** | [**StartMatchingForFunctionsInputBody**](StartMatchingForFunctionsInputBody.md)|  | 

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

# **v3_canonicalize_function_names**
> CanonicalizeNamesOutputBody v3_canonicalize_function_names(canonicalize_names_input_body)

Canonicalize a batch of function names

Accepts up to 25 raw function names and returns their canonical forms in the same order. A name with no canonical form is returned unchanged.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `503` [`SERVICE_UNAVAILABLE`](/errors/SERVICE_UNAVAILABLE) — Service Unavailable

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.canonicalize_names_input_body import CanonicalizeNamesInputBody
from revengai.models.canonicalize_names_output_body import CanonicalizeNamesOutputBody
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
    api_instance = revengai.FunctionsCoreApi(api_client)
    canonicalize_names_input_body = revengai.CanonicalizeNamesInputBody() # CanonicalizeNamesInputBody | 

    try:
        # Canonicalize a batch of function names
        api_response = api_instance.v3_canonicalize_function_names(canonicalize_names_input_body)
        print("The response of FunctionsCoreApi->v3_canonicalize_function_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsCoreApi->v3_canonicalize_function_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canonicalize_names_input_body** | [**CanonicalizeNamesInputBody**](CanonicalizeNamesInputBody.md)|  | 

### Return type

[**CanonicalizeNamesOutputBody**](CanonicalizeNamesOutputBody.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

