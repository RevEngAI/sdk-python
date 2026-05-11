# revengai.AnalysesBulkActionsApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_add_analysis_tags**](AnalysesBulkActionsApi.md#bulk_add_analysis_tags) | **PATCH** /v2/analyses/tags/add | Bulk Add Analysis Tags
[**bulk_delete_analyses**](AnalysesBulkActionsApi.md#bulk_delete_analyses) | **PATCH** /v2/analyses/delete | Bulk Delete Analyses


# **bulk_add_analysis_tags**
> BaseResponseAnalysisBulkAddTagsResponse bulk_add_analysis_tags(analysis_bulk_add_tags_request)

Bulk Add Analysis Tags

Updates analysis tags for multiple analyses. User must be the owner.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.analysis_bulk_add_tags_request import AnalysisBulkAddTagsRequest
from revengai.models.base_response_analysis_bulk_add_tags_response import BaseResponseAnalysisBulkAddTagsResponse
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
    api_instance = revengai.AnalysesBulkActionsApi(api_client)
    analysis_bulk_add_tags_request = revengai.AnalysisBulkAddTagsRequest() # AnalysisBulkAddTagsRequest | 

    try:
        # Bulk Add Analysis Tags
        api_response = api_instance.bulk_add_analysis_tags(analysis_bulk_add_tags_request)
        print("The response of AnalysesBulkActionsApi->bulk_add_analysis_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesBulkActionsApi->bulk_add_analysis_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_bulk_add_tags_request** | [**AnalysisBulkAddTagsRequest**](AnalysisBulkAddTagsRequest.md)|  | 

### Return type

[**BaseResponseAnalysisBulkAddTagsResponse**](BaseResponseAnalysisBulkAddTagsResponse.md)

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

# **bulk_delete_analyses**
> BaseResponseDict bulk_delete_analyses(bulk_delete_analyses_request)

Bulk Delete Analyses

Deletes multiple analyses. User must be the owner of all analyses.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_dict import BaseResponseDict
from revengai.models.bulk_delete_analyses_request import BulkDeleteAnalysesRequest
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
    api_instance = revengai.AnalysesBulkActionsApi(api_client)
    bulk_delete_analyses_request = revengai.BulkDeleteAnalysesRequest() # BulkDeleteAnalysesRequest | 

    try:
        # Bulk Delete Analyses
        api_response = api_instance.bulk_delete_analyses(bulk_delete_analyses_request)
        print("The response of AnalysesBulkActionsApi->bulk_delete_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesBulkActionsApi->bulk_delete_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_analyses_request** | [**BulkDeleteAnalysesRequest**](BulkDeleteAnalysesRequest.md)|  | 

### Return type

[**BaseResponseDict**](BaseResponseDict.md)

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
**404** | Not Found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

