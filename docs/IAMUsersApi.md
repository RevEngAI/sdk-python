# revengai.IAMUsersApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](IAMUsersApi.md#get_me) | **GET** /v2/iam/me | Get current user
[**get_my_permissions**](IAMUsersApi.md#get_my_permissions) | **GET** /v2/iam/me/permissions | Get current user permissions


# **get_me**
> User get_me()

Get current user

Returns the authenticated user's own information.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.user import User
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
    api_instance = revengai.IAMUsersApi(api_client)

    try:
        # Get current user
        api_response = api_instance.get_me()
        print("The response of IAMUsersApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_permissions**
> Permissions get_my_permissions()

Get current user permissions

Returns the feature permissions granted to the authenticated user based on their subscription tier. Use this as the single source of truth for feature gating across web, CLI, and plugin clients.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.permissions import Permissions
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
    api_instance = revengai.IAMUsersApi(api_client)

    try:
        # Get current user permissions
        api_response = api_instance.get_my_permissions()
        print("The response of IAMUsersApi->get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->get_my_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Permissions**](Permissions.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

