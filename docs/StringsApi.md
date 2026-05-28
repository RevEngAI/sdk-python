# revengai.StringsApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_string_to_analysis**](StringsApi.md#add_user_string_to_analysis) | **POST** /v3/analyses/{analysis_id}/user-provided-strings | Add a user-provided string to an analysis.
[**add_user_string_to_function**](StringsApi.md#add_user_string_to_function) | **POST** /v3/functions/{function_id}/user-provided-strings | Add a user-provided string to a function.


# **add_user_string_to_analysis**
> Dict[str, object] add_user_string_to_analysis(analysis_id, add_user_string_input_body)

Add a user-provided string to an analysis.

Attaches a user-provided string to an analysis at the given virtual address. The string is stored with source `USER` and complements strings discovered automatically during analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.StringsApi(api_client)
    analysis_id = 56 # int | Analysis ID
    add_user_string_input_body = revengai.AddUserStringInputBody() # AddUserStringInputBody | 

    try:
        # Add a user-provided string to an analysis.
        api_response = api_instance.add_user_string_to_analysis(analysis_id, add_user_string_input_body)
        print("The response of StringsApi->add_user_string_to_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->add_user_string_to_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **add_user_string_input_body** | [**AddUserStringInputBody**](AddUserStringInputBody.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[APIKey](../README.md#APIKey)

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

# **add_user_string_to_function**
> Dict[str, object] add_user_string_to_function(function_id, add_user_string_to_function_input_body)

Add a user-provided string to a function.

Attaches a user-provided string to a function at the given virtual address. The string is stored with source `USER` and complements strings discovered automatically during analysis.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.StringsApi(api_client)
    function_id = 56 # int | Function ID
    add_user_string_to_function_input_body = revengai.AddUserStringToFunctionInputBody() # AddUserStringToFunctionInputBody | 

    try:
        # Add a user-provided string to a function.
        api_response = api_instance.add_user_string_to_function(function_id, add_user_string_to_function_input_body)
        print("The response of StringsApi->add_user_string_to_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StringsApi->add_user_string_to_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **int**| Function ID | 
 **add_user_string_to_function_input_body** | [**AddUserStringToFunctionInputBody**](AddUserStringToFunctionInputBody.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[APIKey](../README.md#APIKey)

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

