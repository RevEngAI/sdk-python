# revengai.FunctionsAIDecompilationApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ai_decompilation**](FunctionsAIDecompilationApi.md#create_ai_decompilation) | **POST** /v3/functions/{function_id}/ai-decompilation | Start AI decompilation
[**create_ai_decompilation_comment**](FunctionsAIDecompilationApi.md#create_ai_decompilation_comment) | **POST** /v2/functions/{function_id}/ai-decompilation/comments | Create a comment for this function
[**create_ai_decompilation_task**](FunctionsAIDecompilationApi.md#create_ai_decompilation_task) | **POST** /v2/functions/{function_id}/ai-decompilation | Begins AI Decompilation Process
[**delete_ai_decompilation_comment**](FunctionsAIDecompilationApi.md#delete_ai_decompilation_comment) | **DELETE** /v2/functions/{function_id}/ai-decompilation/comments/{comment_id} | Delete a comment
[**get_ai_decompilation**](FunctionsAIDecompilationApi.md#get_ai_decompilation) | **GET** /v3/functions/{function_id}/ai-decompilation | Get AI decompilation result
[**get_ai_decompilation_comments**](FunctionsAIDecompilationApi.md#get_ai_decompilation_comments) | **GET** /v2/functions/{function_id}/ai-decompilation/comments | Get comments for this function
[**get_ai_decompilation_inline_comments**](FunctionsAIDecompilationApi.md#get_ai_decompilation_inline_comments) | **GET** /v3/functions/{function_id}/ai-decompilation/inline-comments | Get AI decompilation inline comments
[**get_ai_decompilation_inline_comments_status**](FunctionsAIDecompilationApi.md#get_ai_decompilation_inline_comments_status) | **GET** /v3/functions/{function_id}/ai-decompilation/inline-comments/status | Get inline comments generation workflow status
[**get_ai_decompilation_rating**](FunctionsAIDecompilationApi.md#get_ai_decompilation_rating) | **GET** /v2/functions/{function_id}/ai-decompilation/rating | Get rating for AI decompilation
[**get_ai_decompilation_status**](FunctionsAIDecompilationApi.md#get_ai_decompilation_status) | **GET** /v3/functions/{function_id}/ai-decompilation/status | Get AI decompilation workflow status
[**get_ai_decompilation_summary**](FunctionsAIDecompilationApi.md#get_ai_decompilation_summary) | **GET** /v3/functions/{function_id}/ai-decompilation/summary | Get AI decompilation summary
[**get_ai_decompilation_summary_status**](FunctionsAIDecompilationApi.md#get_ai_decompilation_summary_status) | **GET** /v3/functions/{function_id}/ai-decompilation/summary/status | Get summary generation workflow status
[**get_ai_decompilation_task_result**](FunctionsAIDecompilationApi.md#get_ai_decompilation_task_result) | **GET** /v2/functions/{function_id}/ai-decompilation | Polls AI Decompilation Process
[**get_ai_decompilation_task_status**](FunctionsAIDecompilationApi.md#get_ai_decompilation_task_status) | **GET** /v2/functions/{function_id}/ai-decompilation/status | Check the status of a function ai decompilation
[**get_ai_decompilation_tokenised**](FunctionsAIDecompilationApi.md#get_ai_decompilation_tokenised) | **GET** /v3/functions/{function_id}/ai-decompilation/tokenised | Get tokenised AI decompilation with function mapping
[**regenerate_ai_decompilation_inline_comments**](FunctionsAIDecompilationApi.md#regenerate_ai_decompilation_inline_comments) | **POST** /v3/functions/{function_id}/ai-decompilation/inline-comments | Regenerate AI decompilation inline comments
[**regenerate_ai_decompilation_summary**](FunctionsAIDecompilationApi.md#regenerate_ai_decompilation_summary) | **POST** /v3/functions/{function_id}/ai-decompilation/summary | Regenerate AI decompilation summary
[**update_ai_decompilation_comment**](FunctionsAIDecompilationApi.md#update_ai_decompilation_comment) | **PATCH** /v2/functions/{function_id}/ai-decompilation/comments/{comment_id} | Update a comment
[**upsert_ai_decompilation_overrides**](FunctionsAIDecompilationApi.md#upsert_ai_decompilation_overrides) | **PATCH** /v3/functions/{function_id}/ai-decompilation/overrides | Upsert variable/function name overrides
[**upsert_ai_decompilation_rating**](FunctionsAIDecompilationApi.md#upsert_ai_decompilation_rating) | **PATCH** /v2/functions/{function_id}/ai-decompilation/rating | Upsert rating for AI decompilation


# **create_ai_decompilation**
> CreateAIDecompOutputBody create_ai_decompilation(function_id, context_aware=context_aware)

Start AI decompilation

Begins the AI decompilation process for a function. Charges team credits and starts the workflow.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.create_ai_decomp_output_body import CreateAIDecompOutputBody
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID
    context_aware = False # bool | Use context-aware decompilation (optional) (default to False)

    try:
        # Start AI decompilation
        api_response = api_instance.create_ai_decompilation(function_id, context_aware=context_aware)
        print("The response of FunctionsAIDecompilationApi->create_ai_decompilation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->create_ai_decompilation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **context_aware** | **bool**| Use context-aware decompilation | [optional] [default to False]

### Return type

[**CreateAIDecompOutputBody**](CreateAIDecompOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_decompilation_comment**
> BaseResponseCommentResponse create_ai_decompilation_comment(function_id, function_comment_create_request)

Create a comment for this function

Creates a comment associated with a specified function).

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_comment_response import BaseResponseCommentResponse
from revengai.models.function_comment_create_request import FunctionCommentCreateRequest
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | 
    function_comment_create_request = revengai.FunctionCommentCreateRequest() # FunctionCommentCreateRequest | 

    try:
        # Create a comment for this function
        api_response = api_instance.create_ai_decompilation_comment(function_id, function_comment_create_request)
        print("The response of FunctionsAIDecompilationApi->create_ai_decompilation_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->create_ai_decompilation_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 
 **function_comment_create_request** | [**FunctionCommentCreateRequest**](FunctionCommentCreateRequest.md)|  | 

### Return type

[**BaseResponseCommentResponse**](BaseResponseCommentResponse.md)

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_decompilation_task**
> BaseResponse create_ai_decompilation_task(function_id)

Begins AI Decompilation Process

Begins the AI Decompilation Process

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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | The ID of the function for which we are creating the decompilation task

    try:
        # Begins AI Decompilation Process
        api_response = api_instance.create_ai_decompilation_task(function_id)
        print("The response of FunctionsAIDecompilationApi->create_ai_decompilation_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->create_ai_decompilation_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| The ID of the function for which we are creating the decompilation task | 

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
**201** | Successful Response |  -  |
**422** | Invalid request parameters |  -  |
**403** | Forbidden |  -  |
**402** | Payment Required |  -  |
**409** | Conflict |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_decompilation_comment**
> BaseResponseBool delete_ai_decompilation_comment(comment_id, function_id)

Delete a comment

Deletes an existing comment. Users can only delete their own comments.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_bool import BaseResponseBool
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    comment_id = 56 # int | 
    function_id = 56 # int | 

    try:
        # Delete a comment
        api_response = api_instance.delete_ai_decompilation_comment(comment_id, function_id)
        print("The response of FunctionsAIDecompilationApi->delete_ai_decompilation_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->delete_ai_decompilation_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  | 
 **function_id** | **int**|  | 

### Return type

[**BaseResponseBool**](BaseResponseBool.md)

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
**403** | You can only delete your own comments |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_decompilation**
> DecompilationData get_ai_decompilation(function_id)

Get AI decompilation result

Returns the decompilation source code.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `500` [`INTERNAL_ERROR`](/errors/INTERNAL_ERROR) — Internal Server Error

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.decompilation_data import DecompilationData
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get AI decompilation result
        api_response = api_instance.get_ai_decompilation(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**DecompilationData**](DecompilationData.md)

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

# **get_ai_decompilation_comments**
> BaseResponseListCommentResponse get_ai_decompilation_comments(function_id)

Get comments for this function

Retrieves all comments created for a specific function. Only returns comments for resources the requesting user has access to.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_list_comment_response import BaseResponseListCommentResponse
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | 

    try:
        # Get comments for this function
        api_response = api_instance.get_ai_decompilation_comments(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**|  | 

### Return type

[**BaseResponseListCommentResponse**](BaseResponseListCommentResponse.md)

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

# **get_ai_decompilation_inline_comments**
> CommentsData get_ai_decompilation_inline_comments(function_id)

Get AI decompilation inline comments

Returns the commented source if available. Returns pending status if comments are still being generated.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.comments_data import CommentsData
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get AI decompilation inline comments
        api_response = api_instance.get_ai_decompilation_inline_comments(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_inline_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_inline_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**CommentsData**](CommentsData.md)

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

# **get_ai_decompilation_inline_comments_status**
> WorkflowProgress get_ai_decompilation_inline_comments_status(function_id)

Get inline comments generation workflow status

Returns fine-grained progress of the inline comments generation workflow.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.workflow_progress import WorkflowProgress
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get inline comments generation workflow status
        api_response = api_instance.get_ai_decompilation_inline_comments_status(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_inline_comments_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_inline_comments_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**WorkflowProgress**](WorkflowProgress.md)

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

# **get_ai_decompilation_rating**
> BaseResponseUnionGetAiDecompilationRatingResponseNoneType get_ai_decompilation_rating(function_id)

Get rating for AI decompilation

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_union_get_ai_decompilation_rating_response_none_type import BaseResponseUnionGetAiDecompilationRatingResponseNoneType
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | The ID of the function for which to get the rating

    try:
        # Get rating for AI decompilation
        api_response = api_instance.get_ai_decompilation_rating(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| The ID of the function for which to get the rating | 

### Return type

[**BaseResponseUnionGetAiDecompilationRatingResponseNoneType**](BaseResponseUnionGetAiDecompilationRatingResponseNoneType.md)

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

# **get_ai_decompilation_status**
> WorkflowProgress get_ai_decompilation_status(function_id)

Get AI decompilation workflow status

Returns fine-grained progress of the running workflow including current step, total steps, and messages. Falls back to the database task status when no workflow is running.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.workflow_progress import WorkflowProgress
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get AI decompilation workflow status
        api_response = api_instance.get_ai_decompilation_status(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**WorkflowProgress**](WorkflowProgress.md)

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

# **get_ai_decompilation_summary**
> SummaryData get_ai_decompilation_summary(function_id)

Get AI decompilation summary

Returns the summary if available. Returns pending status if summary is still being generated.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.summary_data import SummaryData
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get AI decompilation summary
        api_response = api_instance.get_ai_decompilation_summary(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**SummaryData**](SummaryData.md)

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

# **get_ai_decompilation_summary_status**
> WorkflowProgress get_ai_decompilation_summary_status(function_id)

Get summary generation workflow status

Returns fine-grained progress of the summary generation workflow.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.workflow_progress import WorkflowProgress
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get summary generation workflow status
        api_response = api_instance.get_ai_decompilation_summary_status(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_summary_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_summary_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**WorkflowProgress**](WorkflowProgress.md)

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

# **get_ai_decompilation_task_result**
> BaseResponseGetAiDecompilationTask get_ai_decompilation_task_result(function_id, summarise=summarise, generate_inline_comments=generate_inline_comments, force_regenerate=force_regenerate)

Polls AI Decompilation Process

Polls the AI Decompilation Process

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_get_ai_decompilation_task import BaseResponseGetAiDecompilationTask
from revengai.models.regenerate_target import RegenerateTarget
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | The ID of the function being decompiled
    summarise = True # bool | Generate a summary for the decompilation (optional) (default to True)
    generate_inline_comments = True # bool | Generate inline comments for the decompilation (optional) (default to True)
    force_regenerate = [] # List[RegenerateTarget] | Force regeneration of summary and/or comments. (optional) (default to [])

    try:
        # Polls AI Decompilation Process
        api_response = api_instance.get_ai_decompilation_task_result(function_id, summarise=summarise, generate_inline_comments=generate_inline_comments, force_regenerate=force_regenerate)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_task_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_task_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| The ID of the function being decompiled | 
 **summarise** | **bool**| Generate a summary for the decompilation | [optional] [default to True]
 **generate_inline_comments** | **bool**| Generate inline comments for the decompilation | [optional] [default to True]
 **force_regenerate** | [**List[RegenerateTarget]**](RegenerateTarget.md)| Force regeneration of summary and/or comments. | [optional] [default to []]

### Return type

[**BaseResponseGetAiDecompilationTask**](BaseResponseGetAiDecompilationTask.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_decompilation_task_status**
> BaseResponseFunctionTaskResponse get_ai_decompilation_task_status(function_id)

Check the status of a function ai decompilation

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_function_task_response import BaseResponseFunctionTaskResponse
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | The ID of the function being checked

    try:
        # Check the status of a function ai decompilation
        api_response = api_instance.get_ai_decompilation_task_status(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_task_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_task_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| The ID of the function being checked | 

### Return type

[**BaseResponseFunctionTaskResponse**](BaseResponseFunctionTaskResponse.md)

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

# **get_ai_decompilation_tokenised**
> TokenisedData get_ai_decompilation_tokenised(function_id)

Get tokenised AI decompilation with function mapping

Returns the decompilation with placeholder tokens, the function mapping for token resolution, and the predicted function name.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `500` [`INTERNAL_ERROR`](/errors/INTERNAL_ERROR) — Internal Server Error

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.tokenised_data import TokenisedData
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Get tokenised AI decompilation with function mapping
        api_response = api_instance.get_ai_decompilation_tokenised(function_id)
        print("The response of FunctionsAIDecompilationApi->get_ai_decompilation_tokenised:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->get_ai_decompilation_tokenised: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**TokenisedData**](TokenisedData.md)

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

# **regenerate_ai_decompilation_inline_comments**
> RegenerateOutputBody regenerate_ai_decompilation_inline_comments(function_id)

Regenerate AI decompilation inline comments

Starts a new inline comments generation workflow for the function. Requires an existing decompilation with a summary.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.regenerate_output_body import RegenerateOutputBody
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Regenerate AI decompilation inline comments
        api_response = api_instance.regenerate_ai_decompilation_inline_comments(function_id)
        print("The response of FunctionsAIDecompilationApi->regenerate_ai_decompilation_inline_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->regenerate_ai_decompilation_inline_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**RegenerateOutputBody**](RegenerateOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey)

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

# **regenerate_ai_decompilation_summary**
> RegenerateOutputBody regenerate_ai_decompilation_summary(function_id)

Regenerate AI decompilation summary

Starts a new summary generation workflow for the function. Requires an existing decompilation.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.regenerate_output_body import RegenerateOutputBody
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID

    try:
        # Regenerate AI decompilation summary
        api_response = api_instance.regenerate_ai_decompilation_summary(function_id)
        print("The response of FunctionsAIDecompilationApi->regenerate_ai_decompilation_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->regenerate_ai_decompilation_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 

### Return type

[**RegenerateOutputBody**](RegenerateOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey)

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

# **update_ai_decompilation_comment**
> BaseResponseCommentResponse update_ai_decompilation_comment(comment_id, function_id, comment_update_request)

Update a comment

Updates the content of an existing comment. Users can only update their own comments.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_comment_response import BaseResponseCommentResponse
from revengai.models.comment_update_request import CommentUpdateRequest
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    comment_id = 56 # int | 
    function_id = 56 # int | 
    comment_update_request = revengai.CommentUpdateRequest() # CommentUpdateRequest | 

    try:
        # Update a comment
        api_response = api_instance.update_ai_decompilation_comment(comment_id, function_id, comment_update_request)
        print("The response of FunctionsAIDecompilationApi->update_ai_decompilation_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->update_ai_decompilation_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  | 
 **function_id** | **int**|  | 
 **comment_update_request** | [**CommentUpdateRequest**](CommentUpdateRequest.md)|  | 

### Return type

[**BaseResponseCommentResponse**](BaseResponseCommentResponse.md)

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
**403** | You can only update your own comments |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_ai_decompilation_overrides**
> UpsertOverridesData upsert_ai_decompilation_overrides(function_id, upsert_overrides_input_body)

Upsert variable/function name overrides

Applies user-provided name overrides to placeholder tokens in the decompilation.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.upsert_overrides_data import UpsertOverridesData
from revengai.models.upsert_overrides_input_body import UpsertOverridesInputBody
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | Function ID
    upsert_overrides_input_body = revengai.UpsertOverridesInputBody() # UpsertOverridesInputBody | 

    try:
        # Upsert variable/function name overrides
        api_response = api_instance.upsert_ai_decompilation_overrides(function_id, upsert_overrides_input_body)
        print("The response of FunctionsAIDecompilationApi->upsert_ai_decompilation_overrides:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->upsert_ai_decompilation_overrides: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **upsert_overrides_input_body** | [**UpsertOverridesInputBody**](UpsertOverridesInputBody.md)|  | 

### Return type

[**UpsertOverridesData**](UpsertOverridesData.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_ai_decompilation_rating**
> BaseResponse upsert_ai_decompilation_rating(function_id, upsert_ai_decomplation_rating_request)

Upsert rating for AI decompilation

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response import BaseResponse
from revengai.models.upsert_ai_decomplation_rating_request import UpsertAiDecomplationRatingRequest
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
    api_instance = revengai.FunctionsAIDecompilationApi(api_client)
    function_id = 56 # int | The ID of the function being rated
    upsert_ai_decomplation_rating_request = revengai.UpsertAiDecomplationRatingRequest() # UpsertAiDecomplationRatingRequest | 

    try:
        # Upsert rating for AI decompilation
        api_response = api_instance.upsert_ai_decompilation_rating(function_id, upsert_ai_decomplation_rating_request)
        print("The response of FunctionsAIDecompilationApi->upsert_ai_decompilation_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsAIDecompilationApi->upsert_ai_decompilation_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| The ID of the function being rated | 
 **upsert_ai_decomplation_rating_request** | [**UpsertAiDecomplationRatingRequest**](UpsertAiDecomplationRatingRequest.md)|  | 

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

