# revengai.AnalysisStagesApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analysis_stages**](AnalysisStagesApi.md#get_analysis_stages) | **GET** /v2/analysis-stages/{analysis_id} | Get Analysis Stages
[**get_pipeline_status**](AnalysisStagesApi.md#get_pipeline_status) | **GET** /v2/analysis-stages/{analysis_id}/pipeline-status | Get Pipeline Status


# **get_analysis_stages**
> BaseResponseAnalysisStagesResponse get_analysis_stages(analysis_id)

Get Analysis Stages

Returns all stage events for an analysis ordered by timestamp.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_analysis_stages_response import BaseResponseAnalysisStagesResponse
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
    api_instance = revengai.AnalysisStagesApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Analysis Stages
        api_response = api_instance.get_analysis_stages(analysis_id)
        print("The response of AnalysisStagesApi->get_analysis_stages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisStagesApi->get_analysis_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponseAnalysisStagesResponse**](BaseResponseAnalysisStagesResponse.md)

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

# **get_pipeline_status**
> BaseResponsePipelineStatusResponse get_pipeline_status(analysis_id)

Get Pipeline Status

Returns the latest status for each core pipeline stage with the number of analyses ahead in the queue.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.base_response_pipeline_status_response import BaseResponsePipelineStatusResponse
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
    api_instance = revengai.AnalysisStagesApi(api_client)
    analysis_id = 56 # int | 

    try:
        # Get Pipeline Status
        api_response = api_instance.get_pipeline_status(analysis_id)
        print("The response of AnalysisStagesApi->get_pipeline_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisStagesApi->get_pipeline_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**|  | 

### Return type

[**BaseResponsePipelineStatusResponse**](BaseResponsePipelineStatusResponse.md)

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

