# revengai.BinariesApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_zipped_binary**](BinariesApi.md#download_zipped_binary) | **GET** /v2/binaries/{binary_id}/download-zipped | Downloads a zipped binary with password protection
[**get_binary_additional_details**](BinariesApi.md#get_binary_additional_details) | **GET** /v2/binaries/{binary_id}/additional-details | Gets the additional details of a binary
[**get_binary_additional_details_0**](BinariesApi.md#get_binary_additional_details_0) | **GET** /v3/binaries/{binary_id}/additional-details | Get additional details for a binary.
[**get_binary_additional_details_status**](BinariesApi.md#get_binary_additional_details_status) | **GET** /v2/binaries/{binary_id}/additional-details/status | Gets the status of the additional details task for a binary
[**get_binary_additional_details_status_0**](BinariesApi.md#get_binary_additional_details_status_0) | **GET** /v3/binaries/{binary_id}/additional-details/status | Get the additional-details extraction status for a binary.
[**get_binary_details**](BinariesApi.md#get_binary_details) | **GET** /v2/binaries/{binary_id}/details | Gets the details of a binary
[**get_binary_die_info**](BinariesApi.md#get_binary_die_info) | **GET** /v2/binaries/{binary_id}/die-info | Gets the die info of a binary
[**get_binary_externals**](BinariesApi.md#get_binary_externals) | **GET** /v2/binaries/{binary_id}/externals | Gets the external details of a binary
[**get_binary_related_status**](BinariesApi.md#get_binary_related_status) | **GET** /v2/binaries/{binary_id}/related/status | Gets the status of the unpack binary task for a binary
[**get_related_binaries**](BinariesApi.md#get_related_binaries) | **GET** /v2/binaries/{binary_id}/related | Gets the related binaries of a binary.
[**v3_download_binary_zipped**](BinariesApi.md#v3_download_binary_zipped) | **GET** /v3/binaries/{binary_id}/download-zipped | Download a binary as a password-protected zip.
[**v3_get_binary_die_info**](BinariesApi.md#v3_get_binary_die_info) | **GET** /v3/binaries/{binary_id}/die-info | Get Detect It Easy matches for a binary.
[**v3_get_binary_externals**](BinariesApi.md#v3_get_binary_externals) | **GET** /v3/binaries/{binary_id}/externals | Get third-party threat-intel lookups for a binary.
[**v3_get_binary_related**](BinariesApi.md#v3_get_binary_related) | **GET** /v3/binaries/{binary_id}/related | Get the binaries related to this one by unpacking.
[**v3_get_binary_related_status**](BinariesApi.md#v3_get_binary_related_status) | **GET** /v3/binaries/{binary_id}/related/status | Get the archive-unpacking status for a binary.
[**v3_search_binaries**](BinariesApi.md#v3_search_binaries) | **GET** /v3/binaries | Search binaries
[**v3_upload_file**](BinariesApi.md#v3_upload_file) | **POST** /v3/upload | Upload a file.


# **download_zipped_binary**
> bytearray download_zipped_binary(binary_id)

Downloads a zipped binary with password protection

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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Downloads a zipped binary with password protection
        api_response = api_instance.download_zipped_binary(binary_id)
        print("The response of BinariesApi->download_zipped_binary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->download_zipped_binary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

**bytearray**

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download file |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binary_additional_details**
> BaseResponseBinaryAdditionalResponse get_binary_additional_details(binary_id)

Gets the additional details of a binary

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_binary_additional_response import BaseResponseBinaryAdditionalResponse
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the additional details of a binary
        api_response = api_instance.get_binary_additional_details(binary_id)
        print("The response of BinariesApi->get_binary_additional_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_additional_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseBinaryAdditionalResponse**](BaseResponseBinaryAdditionalResponse.md)

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

# **get_binary_additional_details_0**
> GetAdditionalDetailsOutputBody get_binary_additional_details_0(binary_id)

Get additional details for a binary.

Returns structured metadata extracted by the additional-details pipeline for the given binary. Returns `null` for `details` when the pipeline has not yet run.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

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

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get additional details for a binary.
        api_response = api_instance.get_binary_additional_details_0(binary_id)
        print("The response of BinariesApi->get_binary_additional_details_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_additional_details_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetAdditionalDetailsOutputBody**](GetAdditionalDetailsOutputBody.md)

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

# **get_binary_additional_details_status**
> BaseResponseAdditionalDetailsStatusResponse get_binary_additional_details_status(binary_id)

Gets the status of the additional details task for a binary

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_additional_details_status_response import BaseResponseAdditionalDetailsStatusResponse
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the status of the additional details task for a binary
        api_response = api_instance.get_binary_additional_details_status(binary_id)
        print("The response of BinariesApi->get_binary_additional_details_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_additional_details_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseAdditionalDetailsStatusResponse**](BaseResponseAdditionalDetailsStatusResponse.md)

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

# **get_binary_additional_details_status_0**
> GetAdditionalDetailsStatusOutputBody get_binary_additional_details_status_0(binary_id)

Get the additional-details extraction status for a binary.

Returns the status of the additional-details extraction task. One of `UNINITIALISED`, `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

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

# Configure Bearer authorization: bearerAuth
configuration = revengai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get the additional-details extraction status for a binary.
        api_response = api_instance.get_binary_additional_details_status_0(binary_id)
        print("The response of BinariesApi->get_binary_additional_details_status_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_additional_details_status_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetAdditionalDetailsStatusOutputBody**](GetAdditionalDetailsStatusOutputBody.md)

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

# **get_binary_details**
> BaseResponseBinaryDetailsResponse get_binary_details(binary_id)

Gets the details of a binary

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_binary_details_response import BaseResponseBinaryDetailsResponse
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the details of a binary
        api_response = api_instance.get_binary_details(binary_id)
        print("The response of BinariesApi->get_binary_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseBinaryDetailsResponse**](BaseResponseBinaryDetailsResponse.md)

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

# **get_binary_die_info**
> BaseResponseListDieMatch get_binary_die_info(binary_id)

Gets the die info of a binary

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_list_die_match import BaseResponseListDieMatch
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the die info of a binary
        api_response = api_instance.get_binary_die_info(binary_id)
        print("The response of BinariesApi->get_binary_die_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_die_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseListDieMatch**](BaseResponseListDieMatch.md)

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

# **get_binary_externals**
> BaseResponseBinaryExternalsResponse get_binary_externals(binary_id)

Gets the external details of a binary

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_binary_externals_response import BaseResponseBinaryExternalsResponse
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the external details of a binary
        api_response = api_instance.get_binary_externals(binary_id)
        print("The response of BinariesApi->get_binary_externals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_externals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseBinaryExternalsResponse**](BaseResponseBinaryExternalsResponse.md)

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

# **get_binary_related_status**
> BaseResponseBinariesRelatedStatusResponse get_binary_related_status(binary_id)

Gets the status of the unpack binary task for a binary

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_binaries_related_status_response import BaseResponseBinariesRelatedStatusResponse
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the status of the unpack binary task for a binary
        api_response = api_instance.get_binary_related_status(binary_id)
        print("The response of BinariesApi->get_binary_related_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_binary_related_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseBinariesRelatedStatusResponse**](BaseResponseBinariesRelatedStatusResponse.md)

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

# **get_related_binaries**
> BaseResponseChildBinariesResponse get_related_binaries(binary_id)

Gets the related binaries of a binary.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_child_binaries_response import BaseResponseChildBinariesResponse
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | 

    try:
        # Gets the related binaries of a binary.
        api_response = api_instance.get_related_binaries(binary_id)
        print("The response of BinariesApi->get_related_binaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->get_related_binaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**|  | 

### Return type

[**BaseResponseChildBinariesResponse**](BaseResponseChildBinariesResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_download_binary_zipped**
> v3_download_binary_zipped(binary_id)

Download a binary as a password-protected zip.

Streams the binary's uploaded file back as a zip archive, encrypted with a fixed password (`infected`) that deters antivirus scanning in transit rather than protecting confidentiality. Only the binary's owner, or an admin/superadmin, may download it; an internally-managed account's binary can only be downloaded by a superadmin.

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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Download a binary as a password-protected zip.
        api_instance.v3_download_binary_zipped(binary_id)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_download_binary_zipped: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

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

# **v3_get_binary_die_info**
> GetDieInfoOutputBody v3_get_binary_die_info(binary_id)

Get Detect It Easy matches for a binary.

Returns the signatures Detect It Easy recognised in the binary — packers, compilers and file types — with the version it could extract. Empty when detection has not run or recognised nothing.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_die_info_output_body import GetDieInfoOutputBody
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get Detect It Easy matches for a binary.
        api_response = api_instance.v3_get_binary_die_info(binary_id)
        print("The response of BinariesApi->v3_get_binary_die_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_get_binary_die_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetDieInfoOutputBody**](GetDieInfoOutputBody.md)

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

# **v3_get_binary_externals**
> GetBinaryExternalsOutputBody v3_get_binary_externals(binary_id)

Get third-party threat-intel lookups for a binary.

Returns VirusTotal and MalwareBazaar lookup results for the binary's content hash. `externals` is null until at least one lookup has run.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_binary_externals_output_body import GetBinaryExternalsOutputBody
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get third-party threat-intel lookups for a binary.
        api_response = api_instance.v3_get_binary_externals(binary_id)
        print("The response of BinariesApi->v3_get_binary_externals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_get_binary_externals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetBinaryExternalsOutputBody**](GetBinaryExternalsOutputBody.md)

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

# **v3_get_binary_related**
> GetRelatedBinariesOutputBody v3_get_binary_related(binary_id)

Get the binaries related to this one by unpacking.

Returns the binaries unpacked out of this one, and the archive it came out of when it was not uploaded directly. A related binary that has never been analysed carries a null `analysis_id`.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_related_binaries_output_body import GetRelatedBinariesOutputBody
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get the binaries related to this one by unpacking.
        api_response = api_instance.v3_get_binary_related(binary_id)
        print("The response of BinariesApi->v3_get_binary_related:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_get_binary_related: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetRelatedBinariesOutputBody**](GetRelatedBinariesOutputBody.md)

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

# **v3_get_binary_related_status**
> GetRelatedStatusOutputBody v3_get_binary_related_status(binary_id)

Get the archive-unpacking status for a binary.

Returns the status of the task that unpacks an archive into its contents, which is what decides whether the related-binary list is still filling up. One of `UNINITIALISED`, `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_related_status_output_body import GetRelatedStatusOutputBody
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
    api_instance = revengai.BinariesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get the archive-unpacking status for a binary.
        api_response = api_instance.v3_get_binary_related_status(binary_id)
        print("The response of BinariesApi->v3_get_binary_related_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_get_binary_related_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**GetRelatedStatusOutputBody**](GetRelatedStatusOutputBody.md)

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

# **v3_search_binaries**
> SearchBinariesOutputBody v3_search_binaries(partial_name=partial_name, partial_sha256=partial_sha256, tags=tags, model_name=model_name, user_files_only=user_files_only, exclude_binary_id=exclude_binary_id, user_ids=user_ids, limit=limit, offset=offset)

Search binaries

Searches for binaries visible to the caller. At least one of partial_name, partial_sha256, tags, or model_name must be provided.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.search_binaries_output_body import SearchBinariesOutputBody
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
    api_instance = revengai.BinariesApi(api_client)
    partial_name = 'partial_name_example' # str | Partial or full binary name to search for (optional)
    partial_sha256 = 'partial_sha256_example' # str | Partial or full SHA-256 hash to search for (optional)
    tags = ['tags_example'] # List[Optional[str]] | Restrict results to binaries carrying at least one of these tags (optional)
    model_name = 'model_name_example' # str | Restrict results to binaries analysed with this model (optional)
    user_files_only = False # bool | Restrict results to files the caller uploaded themself (optional) (default to False)
    exclude_binary_id = 56 # int | A binary ID to exclude from the results (optional)
    user_ids = [56] # List[int] | Restrict results to binaries owned by one of these user IDs (optional)
    limit = 10 # int | Maximum results to return (optional) (default to 10)
    offset = 0 # int | Number of results to skip (optional) (default to 0)

    try:
        # Search binaries
        api_response = api_instance.v3_search_binaries(partial_name=partial_name, partial_sha256=partial_sha256, tags=tags, model_name=model_name, user_files_only=user_files_only, exclude_binary_id=exclude_binary_id, user_ids=user_ids, limit=limit, offset=offset)
        print("The response of BinariesApi->v3_search_binaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_search_binaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partial_name** | **str**| Partial or full binary name to search for | [optional] 
 **partial_sha256** | **str**| Partial or full SHA-256 hash to search for | [optional] 
 **tags** | [**List[Optional[str]]**](str.md)| Restrict results to binaries carrying at least one of these tags | [optional] 
 **model_name** | **str**| Restrict results to binaries analysed with this model | [optional] 
 **user_files_only** | **bool**| Restrict results to files the caller uploaded themself | [optional] [default to False]
 **exclude_binary_id** | **int**| A binary ID to exclude from the results | [optional] 
 **user_ids** | [**List[int]**](int.md)| Restrict results to binaries owned by one of these user IDs | [optional] 
 **limit** | **int**| Maximum results to return | [optional] [default to 10]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**SearchBinariesOutputBody**](SearchBinariesOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_upload_file**
> UploadOutputBody v3_upload_file(file, upload_file_type, force_overwrite=force_overwrite)

Upload a file.

Uploads a binary, debug symbol, packed sample, or firmware image, keyed by its SHA-256 hash. A BINARY upload from a non-system caller also detects the file's architecture and OS so POST /v3/analyses knows whether it can run static analysis.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `413` [`REQUEST_ENTITY_TOO_LARGE`](/errors/REQUEST_ENTITY_TOO_LARGE) — Request Entity Too Large

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.upload_output_body import UploadOutputBody
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
    api_instance = revengai.BinariesApi(api_client)
    file = None # bytearray | The file's raw bytes.
    upload_file_type = 'upload_file_type_example' # str | The kind of file being uploaded.
    force_overwrite = True # bool | Re-upload and overwrite even if a file with this hash already exists. (optional)

    try:
        # Upload a file.
        api_response = api_instance.v3_upload_file(file, upload_file_type, force_overwrite=force_overwrite)
        print("The response of BinariesApi->v3_upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinariesApi->v3_upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The file&#39;s raw bytes. | 
 **upload_file_type** | **str**| The kind of file being uploaded. | 
 **force_overwrite** | **bool**| Re-upload and overwrite even if a file with this hash already exists. | [optional] 

### Return type

[**UploadOutputBody**](UploadOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**413** | Request Entity Too Large |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

