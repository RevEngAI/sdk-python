# revengai.AnalysesResultsMetadataApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analysis_functions_paginated**](AnalysesResultsMetadataApi.md#get_analysis_functions_paginated) | **GET** /v2/analyses/{analysis_id}/functions | Get functions from analysis
[**get_capabilities**](AnalysesResultsMetadataApi.md#get_capabilities) | **GET** /v2/analyses/{analysis_id}/capabilities | Gets the capabilities from the analysis
[**get_functions_list**](AnalysesResultsMetadataApi.md#get_functions_list) | **GET** /v2/analyses/{analysis_id}/functions/list | Gets functions from analysis
[**get_tags**](AnalysesResultsMetadataApi.md#get_tags) | **GET** /v2/analyses/{analysis_id}/tags | Get function tags with maliciousness score
[**v3_get_analysis_xref**](AnalysesResultsMetadataApi.md#v3_get_analysis_xref) | **GET** /v3/analyses/{analysis_id}/xrefs/{vaddr} | Look up xrefs by virtual address.
[**v3_list_analysis_capabilities**](AnalysesResultsMetadataApi.md#v3_list_analysis_capabilities) | **GET** /v3/analyses/{analysis_id}/capabilities | List the capabilities found in an analysis.
[**v3_list_analysis_tags**](AnalysesResultsMetadataApi.md#v3_list_analysis_tags) | **GET** /v3/analyses/{analysis_id}/tags | List the tags on an analysis.


# **get_analysis_functions_paginated**
> BaseResponseAnalysisFunctionsList get_analysis_functions_paginated(analysis_id, page=page, page_size=page_size)

Get functions from analysis

Returns a paginated list of functions identified during analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_analysis_functions_list import BaseResponseAnalysisFunctionsList
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | 
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 1000 # int | Number of items per page. (optional) (default to 1000)

    try:
        # Get functions from analysis
        api_response = api_instance.get_analysis_functions_paginated(analysis_id, page=page, page_size=page_size)
        print("The response of AnalysesResultsMetadataApi->get_analysis_functions_paginated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->get_analysis_functions_paginated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page. | [optional] [default to 1000]

### Return type

[**BaseResponseAnalysisFunctionsList**](BaseResponseAnalysisFunctionsList.md)

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

# **get_capabilities**
> BaseResponseCapabilities get_capabilities(analysis_id)

Gets the capabilities from the analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_capabilities import BaseResponseCapabilities
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Gets the capabilities from the analysis
        api_response = api_instance.get_capabilities(analysis_id)
        print("The response of AnalysesResultsMetadataApi->get_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->get_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseCapabilities**](BaseResponseCapabilities.md)

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

# **get_functions_list**
> BaseResponseAnalysisFunctions get_functions_list(analysis_id, search_term=search_term, min_v_addr=min_v_addr, max_v_addr=max_v_addr, include_embeddings=include_embeddings, page=page, page_size=page_size)

Gets functions from analysis

Gets the functions identified during analysis

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_analysis_functions import BaseResponseAnalysisFunctions
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | 
    search_term = 'search_term_example' # str |  (optional)
    min_v_addr = 56 # int |  (optional)
    max_v_addr = 56 # int |  (optional)
    include_embeddings = True # bool |  (optional) (default to True)
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 1000 # int | Number of items per page. (optional) (default to 1000)

    try:
        # Gets functions from analysis
        api_response = api_instance.get_functions_list(analysis_id, search_term=search_term, min_v_addr=min_v_addr, max_v_addr=max_v_addr, include_embeddings=include_embeddings, page=page, page_size=page_size)
        print("The response of AnalysesResultsMetadataApi->get_functions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->get_functions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 
 **search_term** | **str**|  | [optional] 
 **min_v_addr** | **int**|  | [optional] 
 **max_v_addr** | **int**|  | [optional] 
 **include_embeddings** | **bool**|  | [optional] [default to True]
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page. | [optional] [default to 1000]

### Return type

[**BaseResponseAnalysisFunctions**](BaseResponseAnalysisFunctions.md)

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

# **get_tags**
> BaseResponseAnalysisTags get_tags(analysis_id)

Get function tags with maliciousness score

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.base_response_analysis_tags import BaseResponseAnalysisTags
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get function tags with maliciousness score
        api_response = api_instance.get_tags(analysis_id)
        print("The response of AnalysesResultsMetadataApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->get_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseAnalysisTags**](BaseResponseAnalysisTags.md)

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

# **v3_get_analysis_xref**
> AnalysisXrefOutputBody v3_get_analysis_xref(analysis_id, vaddr)

Look up xrefs by virtual address.

Returns every cross-reference into and out of a virtual address, read from the analysis' cache.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_xref_output_body import AnalysisXrefOutputBody
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | Analysis ID
    vaddr = 56 # int | Virtual address to match against xrefs

    try:
        # Look up xrefs by virtual address.
        api_response = api_instance.v3_get_analysis_xref(analysis_id, vaddr)
        print("The response of AnalysesResultsMetadataApi->v3_get_analysis_xref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->v3_get_analysis_xref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **vaddr** | **int**| Virtual address to match against xrefs | 

### Return type

[**AnalysisXrefOutputBody**](AnalysisXrefOutputBody.md)

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

# **v3_list_analysis_capabilities**
> AnalysisCapabilitiesOutputBody v3_list_analysis_capabilities(analysis_id)

List the capabilities found in an analysis.

Returns the capabilities the binary-analysis pipeline attributed to the analysis' functions, ordered by function address. This is the static capability set recorded against the binary, not the AI capabilities agent's findings, which are triggered by `/v3/analyses/{analysis_id}/capabilities:run`.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_capabilities_output_body import AnalysisCapabilitiesOutputBody
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # List the capabilities found in an analysis.
        api_response = api_instance.v3_list_analysis_capabilities(analysis_id)
        print("The response of AnalysesResultsMetadataApi->v3_list_analysis_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->v3_list_analysis_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**AnalysisCapabilitiesOutputBody**](AnalysisCapabilitiesOutputBody.md)

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

# **v3_list_analysis_tags**
> AnalysisTagsOutputBody v3_list_analysis_tags(analysis_id)

List the tags on an analysis.

Returns every tag on the analysis' binary, of any origin.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.analysis_tags_output_body import AnalysisTagsOutputBody
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
    api_instance = revengai.AnalysesResultsMetadataApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # List the tags on an analysis.
        api_response = api_instance.v3_list_analysis_tags(analysis_id)
        print("The response of AnalysesResultsMetadataApi->v3_list_analysis_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesResultsMetadataApi->v3_list_analysis_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**AnalysisTagsOutputBody**](AnalysisTagsOutputBody.md)

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

