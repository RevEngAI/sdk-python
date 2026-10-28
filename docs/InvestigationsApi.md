# revengai.InvestigationsApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_create_investigation**](InvestigationsApi.md#v3_create_investigation) | **POST** /v3/investigations | Create an investigation.
[**v3_create_investigation_conversation**](InvestigationsApi.md#v3_create_investigation_conversation) | **POST** /v3/investigations/{investigation_id}/conversations | Start a conversation in an investigation.
[**v3_delete_investigation**](InvestigationsApi.md#v3_delete_investigation) | **DELETE** /v3/investigations/{investigation_id} | Delete an investigation.
[**v3_get_investigation**](InvestigationsApi.md#v3_get_investigation) | **GET** /v3/investigations/{investigation_id} | Get an investigation.
[**v3_get_investigation_finding**](InvestigationsApi.md#v3_get_investigation_finding) | **GET** /v3/investigations/{investigation_id}/findings/{finding_id} | Get a finding of an investigation.
[**v3_list_investigation_agent_runs**](InvestigationsApi.md#v3_list_investigation_agent_runs) | **GET** /v3/investigations/agent-runs | List agent runs on investigations.
[**v3_list_investigation_conversations**](InvestigationsApi.md#v3_list_investigation_conversations) | **GET** /v3/investigations/{investigation_id}/conversations | List the conversations of an investigation.
[**v3_list_investigation_findings**](InvestigationsApi.md#v3_list_investigation_findings) | **GET** /v3/investigations/{investigation_id}/findings | List the findings of an investigation.
[**v3_list_investigation_spend**](InvestigationsApi.md#v3_list_investigation_spend) | **GET** /v3/investigations/{investigation_id}/spend | List what an investigation spent.
[**v3_list_investigations**](InvestigationsApi.md#v3_list_investigations) | **GET** /v3/investigations | List investigations.
[**v3_patch_investigation**](InvestigationsApi.md#v3_patch_investigation) | **PATCH** /v3/investigations/{investigation_id} | Update an investigation.
[**v3_set_investigation_budget**](InvestigationsApi.md#v3_set_investigation_budget) | **PUT** /v3/investigations/{investigation_id}/budget | Set the budget of an investigation.


# **v3_create_investigation**
> InvestigationBody v3_create_investigation(create_investigation_input_body)

Create an investigation.

Creates an investigation owned by the caller, initially open and empty.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.create_investigation_input_body import CreateInvestigationInputBody
from revengai.models.investigation_body import InvestigationBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    create_investigation_input_body = revengai.CreateInvestigationInputBody() # CreateInvestigationInputBody | 

    try:
        # Create an investigation.
        api_response = api_instance.v3_create_investigation(create_investigation_input_body)
        print("The response of InvestigationsApi->v3_create_investigation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_create_investigation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_investigation_input_body** | [**CreateInvestigationInputBody**](CreateInvestigationInputBody.md)|  | 

### Return type

[**InvestigationBody**](InvestigationBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_investigation_conversation**
> ConversationBody v3_create_investigation_conversation(investigation_id, create_conversation_input_body)

Start a conversation in an investigation.

Starts a chat conversation held by the investigation, about the whole investigation or about one of its analyses. Anyone who can see the investigation can start one. Read it, stream it and send messages in it with the /v2/conversations endpoints; only the user who started it can send messages in it. Deleting the investigation deletes its conversations.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.conversation_body import ConversationBody
from revengai.models.create_conversation_input_body import CreateConversationInputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    create_conversation_input_body = revengai.CreateConversationInputBody() # CreateConversationInputBody | 

    try:
        # Start a conversation in an investigation.
        api_response = api_instance.v3_create_investigation_conversation(investigation_id, create_conversation_input_body)
        print("The response of InvestigationsApi->v3_create_investigation_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_create_investigation_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **create_conversation_input_body** | [**CreateConversationInputBody**](CreateConversationInputBody.md)|  | 

### Return type

[**ConversationBody**](ConversationBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_delete_investigation**
> v3_delete_investigation(investigation_id)

Delete an investigation.

Deletes an investigation and its links to analyses. The analyses themselves are not deleted. Only the owner can delete an investigation.

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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 

    try:
        # Delete an investigation.
        api_instance.v3_delete_investigation(investigation_id)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_delete_investigation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_get_investigation**
> GetInvestigationOutputBody v3_get_investigation(investigation_id)

Get an investigation.

Gets a single investigation, including the IDs of the analyses in it that the caller may see.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_investigation_output_body import GetInvestigationOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 

    try:
        # Get an investigation.
        api_response = api_instance.v3_get_investigation(investigation_id)
        print("The response of InvestigationsApi->v3_get_investigation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_get_investigation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 

### Return type

[**GetInvestigationOutputBody**](GetInvestigationOutputBody.md)

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

# **v3_get_investigation_finding**
> GetFindingOutputBody v3_get_investigation_finding(investigation_id, finding_id)

Get a finding of an investigation.

Gets a single finding, including the IDs of the analyses it was derived from that the caller may see.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.get_finding_output_body import GetFindingOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    finding_id = 56 # int | 

    try:
        # Get a finding of an investigation.
        api_response = api_instance.v3_get_investigation_finding(investigation_id, finding_id)
        print("The response of InvestigationsApi->v3_get_investigation_finding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_get_investigation_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **finding_id** | **int**|  | 

### Return type

[**GetFindingOutputBody**](GetFindingOutputBody.md)

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

# **v3_list_investigation_agent_runs**
> ListAgentRunsOutputBody v3_list_investigation_agent_runs(investigation_id=investigation_id, owner_id=owner_id, status=status, severity=severity, search=search, limit=limit, offset=offset)

List agent runs on investigations.

Lists the runs of agents on the files of the investigations you can see, most recently updated first, each with a summary of its result once it is done. A run on a file held by several investigations is listed once for each. Only files you may see are included. Supports narrowing to one investigation, filtering by the investigations' owner, status, severity and name, and pagination.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_agent_runs_output_body import ListAgentRunsOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 0 # int | Only return runs on the files of this investigation. 0 returns runs across every investigation you can see. (optional) (default to 0)
    owner_id = [56] # List[int] | Only return runs in investigations owned by one of these user IDs. (optional)
    status = ['status_example'] # List[str] | Only return runs in investigations in one of these statuses. (optional)
    severity = ['severity_example'] # List[str] | Only return runs in investigations with one of these severities. (optional)
    search = 'search_example' # str | Only return runs in investigations whose name contains this text, ignoring case. (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List agent runs on investigations.
        api_response = api_instance.v3_list_investigation_agent_runs(investigation_id=investigation_id, owner_id=owner_id, status=status, severity=severity, search=search, limit=limit, offset=offset)
        print("The response of InvestigationsApi->v3_list_investigation_agent_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_list_investigation_agent_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**| Only return runs on the files of this investigation. 0 returns runs across every investigation you can see. | [optional] [default to 0]
 **owner_id** | [**List[int]**](int.md)| Only return runs in investigations owned by one of these user IDs. | [optional] 
 **status** | [**List[str]**](str.md)| Only return runs in investigations in one of these statuses. | [optional] 
 **severity** | [**List[str]**](str.md)| Only return runs in investigations with one of these severities. | [optional] 
 **search** | **str**| Only return runs in investigations whose name contains this text, ignoring case. | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListAgentRunsOutputBody**](ListAgentRunsOutputBody.md)

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

# **v3_list_investigation_conversations**
> ListConversationsOutputBody v3_list_investigation_conversations(investigation_id, limit=limit, offset=offset)

List the conversations of an investigation.

Lists the chat conversations held by the investigation, whoever started them, most recently active first. Visible to anyone who can see the investigation. Supports pagination.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_conversations_output_body import ListConversationsOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List the conversations of an investigation.
        api_response = api_instance.v3_list_investigation_conversations(investigation_id, limit=limit, offset=offset)
        print("The response of InvestigationsApi->v3_list_investigation_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_list_investigation_conversations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListConversationsOutputBody**](ListConversationsOutputBody.md)

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

# **v3_list_investigation_findings**
> ListFindingsOutputBody v3_list_investigation_findings(investigation_id, finding_type=finding_type, severity=severity, limit=limit, offset=offset)

List the findings of an investigation.

Lists what the investigation has found, most severe first and then most recent first. Visible to anyone who can see the investigation. Supports filtering by finding type and severity, and pagination.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_findings_output_body import ListFindingsOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    finding_type = ['finding_type_example'] # List[str] | Only return findings of one of these types. (optional)
    severity = ['severity_example'] # List[str] | Only return findings with one of these severities. (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List the findings of an investigation.
        api_response = api_instance.v3_list_investigation_findings(investigation_id, finding_type=finding_type, severity=severity, limit=limit, offset=offset)
        print("The response of InvestigationsApi->v3_list_investigation_findings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_list_investigation_findings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **finding_type** | [**List[str]**](str.md)| Only return findings of one of these types. | [optional] 
 **severity** | [**List[str]**](str.md)| Only return findings with one of these severities. | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListFindingsOutputBody**](ListFindingsOutputBody.md)

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

# **v3_list_investigation_spend**
> ListSpendOutputBody v3_list_investigation_spend(investigation_id, limit=limit, offset=offset)

List what an investigation spent.

Lists the credits charged for the investigation's conversation turns and the agents run from it, newest first. Visible to anyone who can see the investigation. Supports pagination.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_spend_output_body import ListSpendOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List what an investigation spent.
        api_response = api_instance.v3_list_investigation_spend(investigation_id, limit=limit, offset=offset)
        print("The response of InvestigationsApi->v3_list_investigation_spend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_list_investigation_spend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListSpendOutputBody**](ListSpendOutputBody.md)

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

# **v3_list_investigations**
> ListInvestigationsOutputBody v3_list_investigations(status=status, severity=severity, case_type=case_type, owner_id=owner_id, search=search, order_by=order_by, order=order, limit=limit, offset=offset)

List investigations.

Lists the investigations the caller owns or that are shared with the caller's team, most recently updated first by default. Supports filtering by status, severity, case type and owner, a name search, and pagination.

**Error codes:**
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.list_investigations_output_body import ListInvestigationsOutputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    status = ['status_example'] # List[str] | Only return investigations in one of these statuses. (optional)
    severity = ['severity_example'] # List[str] | Only return investigations with one of these severities. (optional)
    case_type = ['case_type_example'] # List[str] | Only return investigations of one of these case types. (optional)
    owner_id = [56] # List[int] | Only return investigations owned by one of these user IDs. (optional)
    search = 'search_example' # str | Only return investigations whose name contains this text, ignoring case. (optional)
    order_by = updated # str |  (optional) (default to updated)
    order = DESC # str |  (optional) (default to DESC)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List investigations.
        api_response = api_instance.v3_list_investigations(status=status, severity=severity, case_type=case_type, owner_id=owner_id, search=search, order_by=order_by, order=order, limit=limit, offset=offset)
        print("The response of InvestigationsApi->v3_list_investigations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_list_investigations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| Only return investigations in one of these statuses. | [optional] 
 **severity** | [**List[str]**](str.md)| Only return investigations with one of these severities. | [optional] 
 **case_type** | [**List[str]**](str.md)| Only return investigations of one of these case types. | [optional] 
 **owner_id** | [**List[int]**](int.md)| Only return investigations owned by one of these user IDs. | [optional] 
 **search** | **str**| Only return investigations whose name contains this text, ignoring case. | [optional] 
 **order_by** | **str**|  | [optional] [default to updated]
 **order** | **str**|  | [optional] [default to DESC]
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ListInvestigationsOutputBody**](ListInvestigationsOutputBody.md)

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

# **v3_patch_investigation**
> InvestigationBody v3_patch_investigation(investigation_id, patch_investigation_input_body)

Update an investigation.

Updates an investigation's name, case type, severity, status and/or scope. Omitted fields keep their existing values. Only the owner can update an investigation.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.investigation_body import InvestigationBody
from revengai.models.patch_investigation_input_body import PatchInvestigationInputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    patch_investigation_input_body = revengai.PatchInvestigationInputBody() # PatchInvestigationInputBody | 

    try:
        # Update an investigation.
        api_response = api_instance.v3_patch_investigation(investigation_id, patch_investigation_input_body)
        print("The response of InvestigationsApi->v3_patch_investigation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_patch_investigation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **patch_investigation_input_body** | [**PatchInvestigationInputBody**](PatchInvestigationInputBody.md)|  | 

### Return type

[**InvestigationBody**](InvestigationBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **v3_set_investigation_budget**
> BudgetBody v3_set_investigation_budget(investigation_id, set_budget_input_body)

Set the budget of an investigation.

Sets the most credits the investigation may spend on its conversations and the agents run from it, or removes the limit with null. Once the budget is spent, no new message or agent run is started from the investigation; work already under way finishes, so spend can go a little past the budget. Only the owner can set the budget.

**Error codes:**
- `404` [`NOT_FOUND`](/errors/NOT_FOUND) — Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `422` [`VALIDATION_FAILED`](/errors/VALIDATION_FAILED) — Validation Failed

### Example

* Api Key Authentication (APIKey):
* Bearer Authentication (bearerAuth):

```python
import revengai
from revengai.models.budget_body import BudgetBody
from revengai.models.set_budget_input_body import SetBudgetInputBody
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
    api_instance = revengai.InvestigationsApi(api_client)
    investigation_id = 56 # int | 
    set_budget_input_body = revengai.SetBudgetInputBody() # SetBudgetInputBody | 

    try:
        # Set the budget of an investigation.
        api_response = api_instance.v3_set_investigation_budget(investigation_id, set_budget_input_body)
        print("The response of InvestigationsApi->v3_set_investigation_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestigationsApi->v3_set_investigation_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **int**|  | 
 **set_budget_input_body** | [**SetBudgetInputBody**](SetBudgetInputBody.md)|  | 

### Return type

[**BudgetBody**](BudgetBody.md)

### Authorization

[APIKey](../README.md#APIKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

