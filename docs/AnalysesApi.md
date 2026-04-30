# revengai.AnalysesApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analysis_queue_position**](AnalysesApi.md#get_analysis_queue_position) | **GET** /v2/analyses/{analysis_id}/queue-position | Get the queue position of an analysis


# **get_analysis_queue_position**
> QueuePositionResponse get_analysis_queue_position(analysis_id)

Get the queue position of an analysis

Returns the number of Processing analyses with a lower analysis_id than the given one. Useful for showing the user where they sit in the processing queue while waiting for their analysis to start.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.queue_position_response import QueuePositionResponse
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
    api_instance = revengai.AnalysesApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Get the queue position of an analysis
        api_response = api_instance.get_analysis_queue_position(analysis_id)
        print("The response of AnalysesApi->get_analysis_queue_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->get_analysis_queue_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**QueuePositionResponse**](QueuePositionResponse.md)

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

