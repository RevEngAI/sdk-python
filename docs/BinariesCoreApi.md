# revengai.BinariesCoreApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_binary_additional_details**](BinariesCoreApi.md#get_binary_additional_details) | **GET** /v3/binaries/{binary_id}/additional-details | Get additional details for a binary.
[**get_binary_additional_details_status**](BinariesCoreApi.md#get_binary_additional_details_status) | **GET** /v3/binaries/{binary_id}/additional-details/status | Get the additional-details extraction status for a binary.


# **get_binary_additional_details**
> GetAdditionalDetailsOutputBody get_binary_additional_details(binary_id)

Get additional details for a binary.

Returns structured metadata extracted by the additional-details pipeline for the given binary. Returns `null` for `details` when the pipeline has not yet run.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.get_additional_details_output_body import GetAdditionalDetailsOutputBody
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
    api_instance = revengai.BinariesCoreApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get additional details for a binary.
        api_response = api_instance.get_binary_additional_details(binary_id)
        print("The response of BinariesCoreApi->get_binary_additional_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesCoreApi->get_binary_additional_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetAdditionalDetailsOutputBody**](GetAdditionalDetailsOutputBody.md)

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

# **get_binary_additional_details_status**
> GetAdditionalDetailsStatusOutputBody get_binary_additional_details_status(binary_id)

Get the additional-details extraction status for a binary.

Returns the status of the additional-details extraction task. One of `UNINITIALISED`, `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.get_additional_details_status_output_body import GetAdditionalDetailsStatusOutputBody
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
    api_instance = revengai.BinariesCoreApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get the additional-details extraction status for a binary.
        api_response = api_instance.get_binary_additional_details_status(binary_id)
        print("The response of BinariesCoreApi->get_binary_additional_details_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesCoreApi->get_binary_additional_details_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetAdditionalDetailsStatusOutputBody**](GetAdditionalDetailsStatusOutputBody.md)

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

