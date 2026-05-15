# revengai.FunctionsRenamingHistoryApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_rename_function**](FunctionsRenamingHistoryApi.md#batch_rename_function) | **POST** /v2/functions/rename/batch | Batch Rename Functions
[**batch_rename_functions**](FunctionsRenamingHistoryApi.md#batch_rename_functions) | **POST** /v3/functions/rename | Batch rename functions
[**get_function_history**](FunctionsRenamingHistoryApi.md#get_function_history) | **GET** /v3/functions/{function_id}/history | Get function name history
[**get_function_name_history**](FunctionsRenamingHistoryApi.md#get_function_name_history) | **GET** /v2/functions/history/{function_id} | Get Function Name History
[**rename_function**](FunctionsRenamingHistoryApi.md#rename_function) | **POST** /v3/functions/{function_id}/rename | Rename a function
[**rename_function_id**](FunctionsRenamingHistoryApi.md#rename_function_id) | **POST** /v2/functions/rename/{function_id} | Rename Function
[**revert_function_name**](FunctionsRenamingHistoryApi.md#revert_function_name) | **POST** /v2/functions/history/{function_id}/{history_id} | Revert the function name
[**revert_function_name_0**](FunctionsRenamingHistoryApi.md#revert_function_name_0) | **POST** /v3/functions/{function_id}/history/{history_id}/revert | Revert function name


# **batch_rename_function**
> BaseResponse batch_rename_function(functions_list_rename)

Batch Rename Functions

Renames a list of functions using the function IDs 
 Will record name changes in history

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response import BaseResponse
from revengai.models.functions_list_rename import FunctionsListRename
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    functions_list_rename = revengai.FunctionsListRename() # FunctionsListRename | 

    try:
        # Batch Rename Functions
        api_response = api_instance.batch_rename_function(functions_list_rename)
        print("The response of FunctionsRenamingHistoryApi->batch_rename_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->batch_rename_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **functions_list_rename** | [**FunctionsListRename**](FunctionsListRename.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_rename_functions**
> BatchRenameOutputBody batch_rename_functions(batch_rename_input_body)

Batch rename functions

Renames multiple functions in a single request. Records name changes in history and copies data types from source functions.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.batch_rename_input_body import BatchRenameInputBody
from revengai.models.batch_rename_output_body import BatchRenameOutputBody
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    batch_rename_input_body = revengai.BatchRenameInputBody() # BatchRenameInputBody | 

    try:
        # Batch rename functions
        api_response = api_instance.batch_rename_functions(batch_rename_input_body)
        print("The response of FunctionsRenamingHistoryApi->batch_rename_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->batch_rename_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_rename_input_body** | [**BatchRenameInputBody**](BatchRenameInputBody.md)|  | 

### Return type

[**BatchRenameOutputBody**](BatchRenameOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_history**
> List[HistoryEntry] get_function_history(function_id)

Get function name history

Returns the name change history for a function, newest first.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.history_entry import HistoryEntry
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get function name history
        api_response = api_instance.get_function_history(function_id)
        print("The response of FunctionsRenamingHistoryApi->get_function_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->get_function_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**List[HistoryEntry]**](HistoryEntry.md)

### Authorization

[APIKey](../README.md#APIKey)

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

# **get_function_name_history**
> BaseResponseListFunctionNameHistory get_function_name_history(function_id)

Get Function Name History

Gets the name history of a function using the function ID

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_list_function_name_history import BaseResponseListFunctionNameHistory
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    function_id = 56 # int | 

    try:
        # Get Function Name History
        api_response = api_instance.get_function_name_history(function_id)
        print("The response of FunctionsRenamingHistoryApi->get_function_name_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->get_function_name_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 

### Return type

[**BaseResponseListFunctionNameHistory**](BaseResponseListFunctionNameHistory.md)

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

# **rename_function**
> RenameOutputBody rename_function(function_id, rename_input_body)

Rename a function

Renames a single function and records the change in history.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.rename_input_body import RenameInputBody
from revengai.models.rename_output_body import RenameOutputBody
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    function_id = 56 # int | Function ID
    rename_input_body = revengai.RenameInputBody() # RenameInputBody | 

    try:
        # Rename a function
        api_response = api_instance.rename_function(function_id, rename_input_body)
        print("The response of FunctionsRenamingHistoryApi->rename_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->rename_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **rename_input_body** | [**RenameInputBody**](RenameInputBody.md)|  | 

### Return type

[**RenameOutputBody**](RenameOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **rename_function_id**
> BaseResponse rename_function_id(function_id, function_rename)

Rename Function

Renames a function using the function ID 
 Will record name change history

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response import BaseResponse
from revengai.models.function_rename import FunctionRename
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    function_id = 56 # int | 
    function_rename = revengai.FunctionRename() # FunctionRename | 

    try:
        # Rename Function
        api_response = api_instance.rename_function_id(function_id, function_rename)
        print("The response of FunctionsRenamingHistoryApi->rename_function_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->rename_function_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 
 **function_rename** | [**FunctionRename**](FunctionRename.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_function_name**
> BaseResponse revert_function_name(function_id, history_id)

Revert the function name

Reverts the function name to a previous name using the function ID and history ID

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response import BaseResponse
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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    function_id = 56 # int | 
    history_id = 56 # int | 

    try:
        # Revert the function name
        api_response = api_instance.revert_function_name(function_id, history_id)
        print("The response of FunctionsRenamingHistoryApi->revert_function_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->revert_function_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 
 **history_id** | **int**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **revert_function_name_0**
> Dict[str, object] revert_function_name_0(function_id, history_id)

Revert function name

Reverts a function's name to a previous value from its history.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

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
    api_instance = revengai.FunctionsRenamingHistoryApi(api_client)
    function_id = 56 # int | Function ID
    history_id = 56 # int | History ID to revert to

    try:
        # Revert function name
        api_response = api_instance.revert_function_name_0(function_id, history_id)
        print("The response of FunctionsRenamingHistoryApi->revert_function_name_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsRenamingHistoryApi->revert_function_name_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **history_id** | **int**| History ID to revert to | 

### Return type

**Dict[str, object]**

### Authorization

[APIKey](../README.md#APIKey)

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

