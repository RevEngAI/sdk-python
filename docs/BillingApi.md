# revengai.BillingApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_get_credit_estimates**](BillingApi.md#v3_get_credit_estimates) | **GET** /v3/credit-estimates | Get credit estimates.


# **v3_get_credit_estimates**
> GetCreditEstimatesOutputBody v3_get_credit_estimates()

Get credit estimates.

Returns the table for estimating, before a binary is analysed, the credits creating an analysis of it will use. Find the size bucket the binary's size in bytes falls in; each requested operation, plus `binary-analysis`, is estimated to cost `base_credits + credits_per_function × functions`. The estimate is calibrated to come in at or above most real runs, but it is not a quote: what is charged depends on the binary.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_credit_estimates_output_body import GetCreditEstimatesOutputBody
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
    api_instance = revengai.BillingApi(api_client)

    try:
        # Get credit estimates.
        api_response = api_instance.v3_get_credit_estimates()
        print("The response of BillingApi->v3_get_credit_estimates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->v3_get_credit_estimates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCreditEstimatesOutputBody**](GetCreditEstimatesOutputBody.md)

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

