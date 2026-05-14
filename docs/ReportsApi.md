# revengai.ReportsApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pdf_report**](ReportsApi.md#create_pdf_report) | **POST** /v3/analysis/{analysis_id}/pdf | Start PDF report generation
[**download_pdf_report**](ReportsApi.md#download_pdf_report) | **GET** /v3/analysis/{analysis_id}/pdf/{task_id} | Download generated PDF report
[**get_pdf_report_status**](ReportsApi.md#get_pdf_report_status) | **GET** /v3/analysis/{analysis_id}/pdf/{task_id}/status | Get PDF report workflow status


# **create_pdf_report**
> GeneratePDFOutputBody create_pdf_report(analysis_id)

Start PDF report generation

Starts an asynchronous PDF report generation workflow for the given analysis. Returns a deterministic task_id used to poll status and download the resulting PDF. Idempotent: if a workflow is already running for this analysis and user, the same task_id is returned with `already_running: true` so the caller can rejoin the in-flight workflow.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.generate_pdf_output_body import GeneratePDFOutputBody
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
    api_instance = revengai.ReportsApi(api_client)
    analysis_id = 56 # int | Analysis ID

    try:
        # Start PDF report generation
        api_response = api_instance.create_pdf_report(analysis_id)
        print("The response of ReportsApi->create_pdf_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->create_pdf_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 

### Return type

[**GeneratePDFOutputBody**](GeneratePDFOutputBody.md)

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

# **download_pdf_report**
> download_pdf_report(analysis_id, task_id)

Download generated PDF report

Streams the rendered PDF report. Returns 409 when the workflow is still running and 404 when the task does not exist or the caller is not authorised to see it.

**Error codes:**
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `409` [`ANALYSIS_NOT_READY`](/errors/ANALYSIS_NOT_READY) — Analysis Not Ready
- `500` [`REPORT_RENDER_FAILED`](/errors/REPORT_RENDER_FAILED) — Report Render Failed

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.ReportsApi(api_client)
    analysis_id = 56 # int | Analysis ID
    task_id = 'task_id_example' # str | Task ID returned by the create endpoint

    try:
        # Download generated PDF report
        api_instance.download_pdf_report(analysis_id, task_id)
    except Exception as e:
        print("Exception when calling ReportsApi->download_pdf_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **task_id** | **str**| Task ID returned by the create endpoint | 

### Return type

void (empty response body)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_report_status**
> WorkflowProgress get_pdf_report_status(analysis_id, task_id)

Get PDF report workflow status

Returns live workflow progress for the given task. Returns 404 when the task does not exist or the caller is not authorised to see it.

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
    api_instance = revengai.ReportsApi(api_client)
    analysis_id = 56 # int | Analysis ID
    task_id = 'task_id_example' # str | Task ID returned by the create endpoint

    try:
        # Get PDF report workflow status
        api_response = api_instance.get_pdf_report_status(analysis_id, task_id)
        print("The response of ReportsApi->get_pdf_report_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_pdf_report_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| Analysis ID | 
 **task_id** | **str**| Task ID returned by the create endpoint | 

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

