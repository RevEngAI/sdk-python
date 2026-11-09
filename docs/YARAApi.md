# revengai.YARAApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_add_yara_collection_rule**](YARAApi.md#v3_add_yara_collection_rule) | **POST** /v3/yara/collections/{id}/rules | Add a rule to a collection
[**v3_cancel_yara_scan**](YARAApi.md#v3_cancel_yara_scan) | **POST** /v3/yara/scans/{id}/cancel | Cancel a scan
[**v3_create_yara_collection**](YARAApi.md#v3_create_yara_collection) | **POST** /v3/yara/collections | Create a collection
[**v3_create_yara_rule**](YARAApi.md#v3_create_yara_rule) | **POST** /v3/yara/rules | Create a YARA rule
[**v3_create_yara_scan**](YARAApi.md#v3_create_yara_scan) | **POST** /v3/yara/scans | Run a scan
[**v3_delete_yara_collection**](YARAApi.md#v3_delete_yara_collection) | **DELETE** /v3/yara/collections/{id} | Delete a collection
[**v3_delete_yara_rule**](YARAApi.md#v3_delete_yara_rule) | **DELETE** /v3/yara/rules/{id} | Delete a YARA rule
[**v3_get_yara_collection**](YARAApi.md#v3_get_yara_collection) | **GET** /v3/yara/collections/{id} | Get a collection
[**v3_get_yara_rule**](YARAApi.md#v3_get_yara_rule) | **GET** /v3/yara/rules/{id} | Get a YARA rule
[**v3_get_yara_rule_versions**](YARAApi.md#v3_get_yara_rule_versions) | **GET** /v3/yara/rules/{id}/versions | Get a YARA rule&#39;s version history
[**v3_get_yara_scan**](YARAApi.md#v3_get_yara_scan) | **GET** /v3/yara/scans/{id} | Get scan status
[**v3_list_yara_collections**](YARAApi.md#v3_list_yara_collections) | **GET** /v3/yara/collections | List collections
[**v3_list_yara_datasets**](YARAApi.md#v3_list_yara_datasets) | **GET** /v3/yara/datasets | List scan datasets
[**v3_list_yara_rules**](YARAApi.md#v3_list_yara_rules) | **GET** /v3/yara/rules | List YARA rules
[**v3_list_yara_scan_matches**](YARAApi.md#v3_list_yara_scan_matches) | **GET** /v3/yara/scans/{id}/matches | List scan matches
[**v3_list_yara_scans**](YARAApi.md#v3_list_yara_scans) | **GET** /v3/yara/scans | List scans
[**v3_remove_yara_collection_rule**](YARAApi.md#v3_remove_yara_collection_rule) | **DELETE** /v3/yara/collections/{id}/rules/{rule_id} | Remove a rule from a collection
[**v3_update_yara_rule**](YARAApi.md#v3_update_yara_rule) | **PUT** /v3/yara/rules/{id} | Update a YARA rule
[**v3_validate_yara_rules**](YARAApi.md#v3_validate_yara_rules) | **POST** /v3/yara/rules/validate | Validate YARA rules


# **v3_add_yara_collection_rule**
> DeleteOutputBody v3_add_yara_collection_rule(id, add_rule_input_body)

Add a rule to a collection

Adds a library rule to the collection (or updates its pinned version). Omit version to follow the rule's current version.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.add_rule_input_body import AddRuleInputBody
from revengai.models.delete_output_body import DeleteOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 
    add_rule_input_body = revengai.AddRuleInputBody() # AddRuleInputBody | 

    try:
        # Add a rule to a collection
        api_response = api_instance.v3_add_yara_collection_rule(id, add_rule_input_body)
        print("The response of YARAApi->v3_add_yara_collection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_add_yara_collection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **add_rule_input_body** | [**AddRuleInputBody**](AddRuleInputBody.md)|  | 

### Return type

[**DeleteOutputBody**](DeleteOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_cancel_yara_scan**
> CancelScanOutputBody v3_cancel_yara_scan(id)

Cancel a scan

Requests cancellation of a running asynchronous scan. Already-finished or synchronous scans return a conflict.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.cancel_scan_output_body import CancelScanOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 

    try:
        # Cancel a scan
        api_response = api_instance.v3_cancel_yara_scan(id)
        print("The response of YARAApi->v3_cancel_yara_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_cancel_yara_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CancelScanOutputBody**](CancelScanOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_yara_collection**
> Collection v3_create_yara_collection(create_collection_input_body)

Create a collection

Creates a named, shared collection of library rules that a scan can run as a unit.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed
- `409` [`CONFLICT`](/errors/CONFLICT) — Conflict

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.collection import Collection
from revengai.models.create_collection_input_body import CreateCollectionInputBody
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
    api_instance = revengai.YARAApi(api_client)
    create_collection_input_body = revengai.CreateCollectionInputBody() # CreateCollectionInputBody | 

    try:
        # Create a collection
        api_response = api_instance.v3_create_yara_collection(create_collection_input_body)
        print("The response of YARAApi->v3_create_yara_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_create_yara_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_input_body** | [**CreateCollectionInputBody**](CreateCollectionInputBody.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_yara_rule**
> Rule v3_create_yara_rule(create_rule_input_body)

Create a YARA rule

Saves a rule to the shared library under a unique name. The source is validated first; an uncompilable source is rejected.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed
- `409` [`ALREADY_EXISTS`](/errors/ALREADY_EXISTS) — Already Exists

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.create_rule_input_body import CreateRuleInputBody
from revengai.models.rule import Rule
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
    api_instance = revengai.YARAApi(api_client)
    create_rule_input_body = revengai.CreateRuleInputBody() # CreateRuleInputBody | 

    try:
        # Create a YARA rule
        api_response = api_instance.v3_create_yara_rule(create_rule_input_body)
        print("The response of YARAApi->v3_create_yara_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_create_yara_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rule_input_body** | [**CreateRuleInputBody**](CreateRuleInputBody.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_yara_scan**
> CreateScanResponse v3_create_yara_scan(create_scan_input_body)

Run a scan

Runs a set of rules (inline or by library reference) over a dataset. Small datasets scan synchronously and return the per-file matches inline; datasets over the synchronous limit are dispatched asynchronously and return a scan id to poll. The run mode can be forced with `mode`.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.create_scan_input_body import CreateScanInputBody
from revengai.models.create_scan_response import CreateScanResponse
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
    api_instance = revengai.YARAApi(api_client)
    create_scan_input_body = revengai.CreateScanInputBody() # CreateScanInputBody | 

    try:
        # Run a scan
        api_response = api_instance.v3_create_yara_scan(create_scan_input_body)
        print("The response of YARAApi->v3_create_yara_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_create_yara_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_scan_input_body** | [**CreateScanInputBody**](CreateScanInputBody.md)|  | 

### Return type

[**CreateScanResponse**](CreateScanResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_delete_yara_collection**
> DeleteOutputBody v3_delete_yara_collection(id)

Delete a collection

Deletes a collection. The underlying rules and past scan results are untouched.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.delete_output_body import DeleteOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 

    try:
        # Delete a collection
        api_response = api_instance.v3_delete_yara_collection(id)
        print("The response of YARAApi->v3_delete_yara_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_delete_yara_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DeleteOutputBody**](DeleteOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_delete_yara_rule**
> v3_delete_yara_rule(id)

Delete a YARA rule

Removes a rule. Results of past scans that referenced it are untouched.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 

    try:
        # Delete a YARA rule
        api_instance.v3_delete_yara_rule(id)
    except Exception as e:
        print("Exception when calling YARAApi->v3_delete_yara_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**204** | No Content |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_yara_collection**
> GetCollectionOutputBody v3_get_yara_collection(id)

Get a collection

Returns a collection with its member rules (name, effective version, and whether the version is pinned).

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_collection_output_body import GetCollectionOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 

    try:
        # Get a collection
        api_response = api_instance.v3_get_yara_collection(id)
        print("The response of YARAApi->v3_get_yara_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_get_yara_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetCollectionOutputBody**](GetCollectionOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_yara_rule**
> Rule v3_get_yara_rule(id, version=version)

Get a YARA rule

Returns a rule with its current source, or a specific version's source when `version` is set.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.rule import Rule
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 
    version = 0 # int | Version to fetch; 0 (default) is the current version (optional) (default to 0)

    try:
        # Get a YARA rule
        api_response = api_instance.v3_get_yara_rule(id, version=version)
        print("The response of YARAApi->v3_get_yara_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_get_yara_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **version** | **int**| Version to fetch; 0 (default) is the current version | [optional] [default to 0]

### Return type

[**Rule**](Rule.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_yara_rule_versions**
> VersionsOutputBody v3_get_yara_rule_versions(id)

Get a YARA rule's version history

Returns a rule's versions, newest first.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.versions_output_body import VersionsOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 

    try:
        # Get a YARA rule's version history
        api_response = api_instance.v3_get_yara_rule_versions(id)
        print("The response of YARAApi->v3_get_yara_rule_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_get_yara_rule_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**VersionsOutputBody**](VersionsOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_yara_scan**
> ScanStatusResponse v3_get_yara_scan(id)

Get scan status

Returns a scan's status and progress. For a running asynchronous scan the live workflow progress is included.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.scan_status_response import ScanStatusResponse
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 

    try:
        # Get scan status
        api_response = api_instance.v3_get_yara_scan(id)
        print("The response of YARAApi->v3_get_yara_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_get_yara_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ScanStatusResponse**](ScanStatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_list_yara_collections**
> ListCollectionsOutputBody v3_list_yara_collections()

List collections

Lists the rule collections, each with its rule count.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_collections_output_body import ListCollectionsOutputBody
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
    api_instance = revengai.YARAApi(api_client)

    try:
        # List collections
        api_response = api_instance.v3_list_yara_collections()
        print("The response of YARAApi->v3_list_yara_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_list_yara_collections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListCollectionsOutputBody**](ListCollectionsOutputBody.md)

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

# **v3_list_yara_datasets**
> ListDatasetsOutputBody v3_list_yara_datasets()

List scan datasets

Lists the datasets available to scan, each with its file count.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_datasets_output_body import ListDatasetsOutputBody
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
    api_instance = revengai.YARAApi(api_client)

    try:
        # List scan datasets
        api_response = api_instance.v3_list_yara_datasets()
        print("The response of YARAApi->v3_list_yara_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_list_yara_datasets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDatasetsOutputBody**](ListDatasetsOutputBody.md)

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

# **v3_list_yara_rules**
> ListRulesOutputBody v3_list_yara_rules()

List YARA rules

Returns every rule in the shared library with its current source.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_rules_output_body import ListRulesOutputBody
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
    api_instance = revengai.YARAApi(api_client)

    try:
        # List YARA rules
        api_response = api_instance.v3_list_yara_rules()
        print("The response of YARAApi->v3_list_yara_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_list_yara_rules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListRulesOutputBody**](ListRulesOutputBody.md)

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

# **v3_list_yara_scan_matches**
> ScanMatchesResponse v3_list_yara_scan_matches(id, rule=rule, file=file, sort=sort, limit=limit, offset=offset)

List scan matches

Returns a scan's matches, optionally filtered by rule name and/or file key, paginated.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.scan_matches_response import ScanMatchesResponse
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 
    rule = 'rule_example' # str | Filter to a single rule name (optional)
    file = 'file_example' # str | Filter to a single file key (optional)
    sort = file # str | Match ordering (optional) (default to file)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List scan matches
        api_response = api_instance.v3_list_yara_scan_matches(id, rule=rule, file=file, sort=sort, limit=limit, offset=offset)
        print("The response of YARAApi->v3_list_yara_scan_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_list_yara_scan_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **rule** | **str**| Filter to a single rule name | [optional] 
 **file** | **str**| Filter to a single file key | [optional] 
 **sort** | **str**| Match ordering | [optional] [default to file]
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ScanMatchesResponse**](ScanMatchesResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_list_yara_scans**
> ListScansOutputBody v3_list_yara_scans(status=status, limit=limit, offset=offset)

List scans

Lists past scans, most recent first, optionally filtered by status. Paginated.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_scans_output_body import ListScansOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    status = 'status_example' # str | Filter to a single status (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List scans
        api_response = api_instance.v3_list_yara_scans(status=status, limit=limit, offset=offset)
        print("The response of YARAApi->v3_list_yara_scans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_list_yara_scans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter to a single status | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListScansOutputBody**](ListScansOutputBody.md)

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

# **v3_remove_yara_collection_rule**
> DeleteOutputBody v3_remove_yara_collection_rule(id, rule_id)

Remove a rule from a collection

Removes a library rule from the collection.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.delete_output_body import DeleteOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 
    rule_id = 56 # int | 

    try:
        # Remove a rule from a collection
        api_response = api_instance.v3_remove_yara_collection_rule(id, rule_id)
        print("The response of YARAApi->v3_remove_yara_collection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_remove_yara_collection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **rule_id** | **int**|  | 

### Return type

[**DeleteOutputBody**](DeleteOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_update_yara_rule**
> Rule v3_update_yara_rule(id, update_rule_input_body)

Update a YARA rule

Validates the source and appends a new version, bumping the rule's current version.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.rule import Rule
from revengai.models.update_rule_input_body import UpdateRuleInputBody
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
    api_instance = revengai.YARAApi(api_client)
    id = 56 # int | 
    update_rule_input_body = revengai.UpdateRuleInputBody() # UpdateRuleInputBody | 

    try:
        # Update a YARA rule
        api_response = api_instance.v3_update_yara_rule(id, update_rule_input_body)
        print("The response of YARAApi->v3_update_yara_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_update_yara_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_rule_input_body** | [**UpdateRuleInputBody**](UpdateRuleInputBody.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_validate_yara_rules**
> ValidateOutputBody v3_validate_yara_rules(validate_input_body)

Validate YARA rules

Compiles each submitted rule and reports, per rule, whether it compiled together with any errors and warnings. A rule that fails to compile is reported in the response, not as an HTTP error.

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.validate_input_body import ValidateInputBody
from revengai.models.validate_output_body import ValidateOutputBody
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
    api_instance = revengai.YARAApi(api_client)
    validate_input_body = revengai.ValidateInputBody() # ValidateInputBody | 

    try:
        # Validate YARA rules
        api_response = api_instance.v3_validate_yara_rules(validate_input_body)
        print("The response of YARAApi->v3_validate_yara_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YARAApi->v3_validate_yara_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_input_body** | [**ValidateInputBody**](ValidateInputBody.md)|  | 

### Return type

[**ValidateOutputBody**](ValidateOutputBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

