# revengai.ConfigApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](ConfigApi.md#get_config) | **GET** /v2/config | Get Config
[**v3_get_config**](ConfigApi.md#v3_get_config) | **GET** /v3/config | Get client configuration.
[**v3_get_models**](ConfigApi.md#v3_get_models) | **GET** /v3/models | Get the models available for analysis.


# **get_config**
> BaseResponseConfigResponse get_config()

Get Config

General configuration endpoint

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_config_response import BaseResponseConfigResponse
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
    api_instance = revengai.ConfigApi(api_client)

    try:
        # Get Config
        api_response = api_instance.get_config()
        print("The response of ConfigApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BaseResponseConfigResponse**](BaseResponseConfigResponse.md)

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

# **v3_get_config**
> GetConfigOutputBody v3_get_config()

Get client configuration.

Returns the settings a client needs to configure itself: where to send users to view results, the largest binary the calling user may submit, and what AI decompilation supports. The size limit reflects the caller's own role and tier.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_config_output_body import GetConfigOutputBody
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
    api_instance = revengai.ConfigApi(api_client)

    try:
        # Get client configuration.
        api_response = api_instance.v3_get_config()
        print("The response of ConfigApi->v3_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->v3_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetConfigOutputBody**](GetConfigOutputBody.md)

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

# **v3_get_models**
> GetModelsOutputBody v3_get_models()

Get the models available for analysis.

Returns the models a new analysis can be run on, by base name — the architecture and platform variants a model is built for are collapsed into one entry, and models no longer offered are omitted.

**Error codes:**
- `500` [`INTERNAL_ERROR`](/errors/INTERNAL_ERROR) — Internal Server Error

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_models_output_body import GetModelsOutputBody
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
    api_instance = revengai.ConfigApi(api_client)

    try:
        # Get the models available for analysis.
        api_response = api_instance.v3_get_models()
        print("The response of ConfigApi->v3_get_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->v3_get_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetModelsOutputBody**](GetModelsOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

