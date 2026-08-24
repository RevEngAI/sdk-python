# revengai.DataTypesApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_copy_function_signatures**](DataTypesApi.md#v3_copy_function_signatures) | **POST** /v3/analyses/{analysis_id}/signatures/copy | Copy function signatures
[**v3_create_analysis_data_types**](DataTypesApi.md#v3_create_analysis_data_types) | **POST** /v3/analyses/{analysis_id}/data-types | Create an analysis&#39;s data types
[**v3_get_analysis_data_type**](DataTypesApi.md#v3_get_analysis_data_type) | **GET** /v3/analyses/{analysis_id}/data-types/{data_type_id} | Get one of an analysis&#39;s data types
[**v3_get_analysis_data_type_history**](DataTypesApi.md#v3_get_analysis_data_type_history) | **GET** /v3/analyses/{analysis_id}/data-types/{data_type_id}/history | Get a data type&#39;s edit history
[**v3_get_function_signature**](DataTypesApi.md#v3_get_function_signature) | **GET** /v3/analyses/{analysis_id}/functions/{function_id}/signature | Get a function&#39;s signature
[**v3_get_function_signature_history**](DataTypesApi.md#v3_get_function_signature_history) | **GET** /v3/analyses/{analysis_id}/functions/{function_id}/signature/history | Get a function signature&#39;s edit history
[**v3_list_analysis_data_types**](DataTypesApi.md#v3_list_analysis_data_types) | **GET** /v3/analyses/{analysis_id}/data-types | List an analysis&#39;s data types
[**v3_list_data_type_functions**](DataTypesApi.md#v3_list_data_type_functions) | **GET** /v3/analyses/{analysis_id}/data-types/{data_type_id}/functions | List the functions using a data type
[**v3_list_function_signatures**](DataTypesApi.md#v3_list_function_signatures) | **GET** /v3/functions/signatures | Get signatures for many functions
[**v3_update_analysis_data_types**](DataTypesApi.md#v3_update_analysis_data_types) | **PUT** /v3/analyses/{analysis_id}/data-types | Update an analysis&#39;s data types
[**v3_update_function_signature**](DataTypesApi.md#v3_update_function_signature) | **PUT** /v3/analyses/{analysis_id}/functions/{function_id}/signature | Update a function&#39;s signature


# **v3_copy_function_signatures**
> CopyFunctionSignaturesOutputBody v3_copy_function_signatures(analysis_id, copy_function_signatures_input_body)

Copy function signatures

Replaces each target function's signature with a copy of its source's parameters, return type and calling convention. Every target must belong to this analysis; a source may belong to any analysis the caller can read. The whole request is rejected if any pair is invalid.

A `data_type_id` means nothing outside the analysis that issued it, so the types a copied signature needs are resolved against this analysis by namespace, name and kind. A type this analysis already has under that key has its definition replaced by the source's; a type it lacks is created. Copied signatures get a `source_type` of `USER` and a `source_function_id`, and their previous value is retained.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.copy_function_signatures_input_body import CopyFunctionSignaturesInputBody
from revengai.models.copy_function_signatures_output_body import CopyFunctionSignaturesOutputBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    copy_function_signatures_input_body = revengai.CopyFunctionSignaturesInputBody() # CopyFunctionSignaturesInputBody | 

    try:
        # Copy function signatures
        api_response = api_instance.v3_copy_function_signatures(analysis_id, copy_function_signatures_input_body)
        print("The response of DataTypesApi->v3_copy_function_signatures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_copy_function_signatures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **copy_function_signatures_input_body** | [**CopyFunctionSignaturesInputBody**](CopyFunctionSignaturesInputBody.md)|  | 

### Return type

[**CopyFunctionSignaturesOutputBody**](CopyFunctionSignaturesOutputBody.md)

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

# **v3_create_analysis_data_types**
> AnalysisDataTypesOutputBody v3_create_analysis_data_types(analysis_id, create_analysis_data_types_input_body)

Create an analysis's data types

Adds user-authored types to an analysis. Many types can be created in one request; the whole request is rejected if any of them is invalid. Ids are assigned by the server and returned here. Stored types get a `source_type` of `USER`.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_data_types_output_body import AnalysisDataTypesOutputBody
from revengai.models.create_analysis_data_types_input_body import CreateAnalysisDataTypesInputBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    create_analysis_data_types_input_body = revengai.CreateAnalysisDataTypesInputBody() # CreateAnalysisDataTypesInputBody | 

    try:
        # Create an analysis's data types
        api_response = api_instance.v3_create_analysis_data_types(analysis_id, create_analysis_data_types_input_body)
        print("The response of DataTypesApi->v3_create_analysis_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_create_analysis_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **create_analysis_data_types_input_body** | [**CreateAnalysisDataTypesInputBody**](CreateAnalysisDataTypesInputBody.md)|  | 

### Return type

[**AnalysisDataTypesOutputBody**](AnalysisDataTypesOutputBody.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_analysis_data_type**
> DataTypeEntry v3_get_analysis_data_type(analysis_id, data_type_id)

Get one of an analysis's data types

Returns a single data type by its `data_type_id`, byte-identical to the entry the data types list returns for it — same variant, same fields, same definition — so a client can cache and invalidate rows from either endpoint interchangeably.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.data_type_entry import DataTypeEntry
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    data_type_id = 56 # int | Data type ID, as returned by the data types list for this analysis. 0 is a valid id.

    try:
        # Get one of an analysis's data types
        api_response = api_instance.v3_get_analysis_data_type(analysis_id, data_type_id)
        print("The response of DataTypesApi->v3_get_analysis_data_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_get_analysis_data_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **data_type_id** | **int**| Data type ID, as returned by the data types list for this analysis. 0 is a valid id. | 

### Return type

[**DataTypeEntry**](DataTypeEntry.md)

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

# **v3_get_analysis_data_type_history**
> GetDataTypeHistoryBody v3_get_analysis_data_type_history(analysis_id, data_type_id)

Get a data type's edit history

The versions a data type has held, newest first, each attributed to the edit that wrote it. The first value is the current value.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_data_type_history_body import GetDataTypeHistoryBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    data_type_id = 56 # int | Data type ID, as returned by the data types list for this analysis. 0 is a valid id.

    try:
        # Get a data type's edit history
        api_response = api_instance.v3_get_analysis_data_type_history(analysis_id, data_type_id)
        print("The response of DataTypesApi->v3_get_analysis_data_type_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_get_analysis_data_type_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **data_type_id** | **int**| Data type ID, as returned by the data types list for this analysis. 0 is a valid id. | 

### Return type

[**GetDataTypeHistoryBody**](GetDataTypeHistoryBody.md)

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

# **v3_get_function_signature**
> FunctionSignatureBody v3_get_function_signature(analysis_id, function_id, include_data_types=include_data_types)

Get a function's signature

Returns the extracted signature for one function: its parameters, return type and calling convention. Pass `include_data_types=true` to also get the data types it names.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.function_signature_body import FunctionSignatureBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    function_id = 56 # int | Function ID
    include_data_types = True # bool | Include the data types the signature names in the response. (optional)

    try:
        # Get a function's signature
        api_response = api_instance.v3_get_function_signature(analysis_id, function_id, include_data_types=include_data_types)
        print("The response of DataTypesApi->v3_get_function_signature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_get_function_signature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **function_id** | **int**| Function ID | 
 **include_data_types** | **bool**| Include the data types the signature names in the response. | [optional] 

### Return type

[**FunctionSignatureBody**](FunctionSignatureBody.md)

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

# **v3_get_function_signature_history**
> GetFunctionSignatureHistoryBody v3_get_function_signature_history(analysis_id, function_id)

Get a function signature's edit history

The versions a function's signature has held, newest first, each attributed to the edit that wrote it. The first value is the current value.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_function_signature_history_body import GetFunctionSignatureHistoryBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    function_id = 56 # int | Function ID

    try:
        # Get a function signature's edit history
        api_response = api_instance.v3_get_function_signature_history(analysis_id, function_id)
        print("The response of DataTypesApi->v3_get_function_signature_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_get_function_signature_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **function_id** | **int**| Function ID | 

### Return type

[**GetFunctionSignatureHistoryBody**](GetFunctionSignatureHistoryBody.md)

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

# **v3_list_analysis_data_types**
> ListAnalysisDataTypesOutputBody v3_list_analysis_data_types(analysis_id, offset=offset, limit=limit, kind=kind, namespace=namespace, search=search, source_type=source_type, order_by=order_by, order=order)

List an analysis's data types

Paginated, filterable list of the data types extracted from the binary — structs, unions, enums, typedefs and the rest. Every entry carries its full definition, so paging this list once resolves every `data_type_id` a definition or signature refers to; no follow-up request per id is needed.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_analysis_data_types_output_body import ListAnalysisDataTypesOutputBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    offset = 0 # int | Pagination offset. (optional) (default to 0)
    limit = 100 # int | Page size. (optional) (default to 100)
    kind = ['kind_example'] # List[str] | Only return types of these kinds. Repeat for more than one; empty means no filter. (optional)
    namespace = ['namespace_example'] # List[Optional[str]] | Only return types in these namespaces, matched exactly. Omit for no filter; pass an empty value (namespace=) for the binary's own types, which have no namespace. (optional)
    search = 'search_example' # str | Only return types whose name contains this term. Wildcards in the term are matched literally. (optional)
    source_type = ['source_type_example'] # List[str] | Only return types from these sources. Empty means no filter. (optional)
    order_by = name # str | Field to order by. name orders by namespace, then name, then kind; size orders by size with types of unknown size last, then by namespace, name and kind. (optional) (default to name)
    order = ASC # str | Sort direction. (optional) (default to ASC)

    try:
        # List an analysis's data types
        api_response = api_instance.v3_list_analysis_data_types(analysis_id, offset=offset, limit=limit, kind=kind, namespace=namespace, search=search, source_type=source_type, order_by=order_by, order=order)
        print("The response of DataTypesApi->v3_list_analysis_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_list_analysis_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **offset** | **int**| Pagination offset. | [optional] [default to 0]
 **limit** | **int**| Page size. | [optional] [default to 100]
 **kind** | [**List[str]**](str.md)| Only return types of these kinds. Repeat for more than one; empty means no filter. | [optional] 
 **namespace** | [**List[Optional[str]]**](str.md)| Only return types in these namespaces, matched exactly. Omit for no filter; pass an empty value (namespace&#x3D;) for the binary&#39;s own types, which have no namespace. | [optional] 
 **search** | **str**| Only return types whose name contains this term. Wildcards in the term are matched literally. | [optional] 
 **source_type** | [**List[str]**](str.md)| Only return types from these sources. Empty means no filter. | [optional] 
 **order_by** | **str**| Field to order by. name orders by namespace, then name, then kind; size orders by size with types of unknown size last, then by namespace, name and kind. | [optional] [default to name]
 **order** | **str**| Sort direction. | [optional] [default to ASC]

### Return type

[**ListAnalysisDataTypesOutputBody**](ListAnalysisDataTypesOutputBody.md)

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

# **v3_list_data_type_functions**
> ListDataTypeFunctionsBody v3_list_data_type_functions(analysis_id, data_type_id, page_size=page_size, after_function_id=after_function_id)

List the functions using a data type

Functions that use this data type as their return type or as a parameter. Matches the `data_type_id` exactly as it appears in the signature, so a function taking `sockaddr_in *` matches the pointer type rather than `sockaddr_in`. Ordered by function ID. There is no total count; page with `after_function_id`.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_data_type_functions_body import ListDataTypeFunctionsBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    data_type_id = 56 # int | Data type ID, as returned by the data types list for this analysis. 0 is a valid id.
    page_size = 50 # int | Page size. (optional) (default to 50)
    after_function_id = 0 # int | Return functions with an ID greater than this. Pass the previous page's next_after_function_id; 0 starts at the first function. (optional) (default to 0)

    try:
        # List the functions using a data type
        api_response = api_instance.v3_list_data_type_functions(analysis_id, data_type_id, page_size=page_size, after_function_id=after_function_id)
        print("The response of DataTypesApi->v3_list_data_type_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_list_data_type_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **data_type_id** | **int**| Data type ID, as returned by the data types list for this analysis. 0 is a valid id. | 
 **page_size** | **int**| Page size. | [optional] [default to 50]
 **after_function_id** | **int**| Return functions with an ID greater than this. Pass the previous page&#39;s next_after_function_id; 0 starts at the first function. | [optional] [default to 0]

### Return type

[**ListDataTypeFunctionsBody**](ListDataTypeFunctionsBody.md)

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

# **v3_list_function_signatures**
> ListFunctionSignaturesOutputBody v3_list_function_signatures(function_ids, include_data_types=include_data_types)

Get signatures for many functions

Returns the extracted signature for each supplied function ID, in request order. The functions need not share an analysis; each entry names the analysis its `data_type_id`s resolve against. Pass `include_data_types=true` to also get those data types, grouped by analysis. The caller must have read access to every function or the request is rejected.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_function_signatures_output_body import ListFunctionSignaturesOutputBody
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
    api_instance = revengai.DataTypesApi(api_client)
    function_ids = [56] # List[int] | Function IDs to fetch signatures for.
    include_data_types = True # bool | Include the data types the signatures name in the response. (optional)

    try:
        # Get signatures for many functions
        api_response = api_instance.v3_list_function_signatures(function_ids, include_data_types=include_data_types)
        print("The response of DataTypesApi->v3_list_function_signatures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_list_function_signatures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_ids** | [**List[int]**](int.md)| Function IDs to fetch signatures for. | 
 **include_data_types** | **bool**| Include the data types the signatures name in the response. | [optional] 

### Return type

[**ListFunctionSignaturesOutputBody**](ListFunctionSignaturesOutputBody.md)

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

# **v3_update_analysis_data_types**
> AnalysisDataTypesOutputBody v3_update_analysis_data_types(analysis_id, update_analysis_data_types_input_body)

Update an analysis's data types

Replaces stored types in full: a field left out of the request is cleared. Many types can be updated in one request; the whole request is rejected if any of them is invalid. `kind` may be changed, and the definition must then match the new kind. Updated types get a `source_type` of `USER`, and their previous value is retained.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_data_types_output_body import AnalysisDataTypesOutputBody
from revengai.models.update_analysis_data_types_input_body import UpdateAnalysisDataTypesInputBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    update_analysis_data_types_input_body = revengai.UpdateAnalysisDataTypesInputBody() # UpdateAnalysisDataTypesInputBody | 

    try:
        # Update an analysis's data types
        api_response = api_instance.v3_update_analysis_data_types(analysis_id, update_analysis_data_types_input_body)
        print("The response of DataTypesApi->v3_update_analysis_data_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_update_analysis_data_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **update_analysis_data_types_input_body** | [**UpdateAnalysisDataTypesInputBody**](UpdateAnalysisDataTypesInputBody.md)|  | 

### Return type

[**AnalysisDataTypesOutputBody**](AnalysisDataTypesOutputBody.md)

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

# **v3_update_function_signature**
> FunctionSignatureEntry v3_update_function_signature(analysis_id, function_id, update_function_signature_input_body)

Update a function's signature

Replaces a function's parameters, return type and calling convention in full — anything left out of the request is cleared. Parameter and return types are `data_type_id`s belonging to this analysis. Edits an extracted signature only: a function with `has_signature` false is rejected with 404. The stored signature gets a `source_type` of `USER`, and its previous value is retained.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.function_signature_entry import FunctionSignatureEntry
from revengai.models.update_function_signature_input_body import UpdateFunctionSignatureInputBody
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
    api_instance = revengai.DataTypesApi(api_client)
    analysis_id = 56 # int | Analysis ID
    function_id = 56 # int | Function ID
    update_function_signature_input_body = revengai.UpdateFunctionSignatureInputBody() # UpdateFunctionSignatureInputBody | 

    try:
        # Update a function's signature
        api_response = api_instance.v3_update_function_signature(analysis_id, function_id, update_function_signature_input_body)
        print("The response of DataTypesApi->v3_update_function_signature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->v3_update_function_signature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **function_id** | **int**| Function ID | 
 **update_function_signature_input_body** | [**UpdateFunctionSignatureInputBody**](UpdateFunctionSignatureInputBody.md)|  | 

### Return type

[**FunctionSignatureEntry**](FunctionSignatureEntry.md)

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

