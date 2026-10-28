# revengai.ExternalSourcesApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_get_virustotal_scan_operation**](ExternalSourcesApi.md#v3_get_virustotal_scan_operation) | **GET** /v3/operations/virustotal-scan/{binary_id} | Get a VirusTotal scan operation.
[**v3_run_virustotal_scan**](ExternalSourcesApi.md#v3_run_virustotal_scan) | **POST** /v3/binaries/{binary_id}/virustotal-scan:run | Trigger a VirusTotal lookup for a binary.


# **v3_get_virustotal_scan_operation**
> OperationVirusTotalScanMetadataVirusTotalScanResult v3_get_virustotal_scan_operation(binary_id)

Get a VirusTotal scan operation.

Returns the current state of the most recently triggered VirusTotal lookup for this binary.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_virus_total_scan_metadata_virus_total_scan_result import OperationVirusTotalScanMetadataVirusTotalScanResult
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
    api_instance = revengai.ExternalSourcesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Get a VirusTotal scan operation.
        api_response = api_instance.v3_get_virustotal_scan_operation(binary_id)
        print("The response of ExternalSourcesApi->v3_get_virustotal_scan_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSourcesApi->v3_get_virustotal_scan_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**OperationVirusTotalScanMetadataVirusTotalScanResult**](OperationVirusTotalScanMetadataVirusTotalScanResult.md)

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

# **v3_run_virustotal_scan**
> OperationVirusTotalScanMetadataVirusTotalScanResult v3_run_virustotal_scan(binary_id)

Trigger a VirusTotal lookup for a binary.

Starts a lookup of the binary's content hash against VirusTotal, using the team's registered API key, and returns the operation to poll for its outcome. Returns 403 if the team has no valid key registered, and 409 while a lookup is already in progress for this binary.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict
- `403` [`NO_VIRUSTOTAL_KEY`](/errors/NO_VIRUSTOTAL_KEY) — No VirusTotal Key

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.operation_virus_total_scan_metadata_virus_total_scan_result import OperationVirusTotalScanMetadataVirusTotalScanResult
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
    api_instance = revengai.ExternalSourcesApi(api_client)
    binary_id = 56 # int | Binary ID

    try:
        # Trigger a VirusTotal lookup for a binary.
        api_response = api_instance.v3_run_virustotal_scan(binary_id)
        print("The response of ExternalSourcesApi->v3_run_virustotal_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSourcesApi->v3_run_virustotal_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binary_id** | **int**| Binary ID | 

### Return type

[**OperationVirusTotalScanMetadataVirusTotalScanResult**](OperationVirusTotalScanMetadataVirusTotalScanResult.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

