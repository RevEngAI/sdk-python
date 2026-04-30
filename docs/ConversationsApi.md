# revengai.ConversationsApi

All URIs are relative to *https://api.reveng.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_run**](ConversationsApi.md#cancel_run) | **POST** /v2/conversations/{id}/cancel | Cancel an active run
[**confirm_tool**](ConversationsApi.md#confirm_tool) | **POST** /v2/conversations/{id}/confirm | Approve or reject a pending tool confirmation
[**create_conversation**](ConversationsApi.md#create_conversation) | **POST** /v2/conversations | Create a new conversation
[**get_conversation**](ConversationsApi.md#get_conversation) | **GET** /v2/conversations/{id} | Get a conversation with its events
[**list_conversations**](ConversationsApi.md#list_conversations) | **GET** /v2/conversations | List conversations for the authenticated user
[**send_message**](ConversationsApi.md#send_message) | **POST** /v2/conversations/{id}/messages | Send a message and start an agentic run
[**stream_events**](ConversationsApi.md#stream_events) | **GET** /v2/conversations/{id}/events | Stream conversation events (SSE)


# **cancel_run**
> StatusResponse cancel_run(id)

Cancel an active run

Cancels the currently active agentic run for the given conversation. Returns 404 if no run is in progress.

**Error codes:**
- `400` [`INVALID_CONVERSATION_ID`](/errors/INVALID_CONVERSATION_ID) — Invalid Conversation ID
- `404` [`CONVERSATION_NOT_FOUND`](/errors/CONVERSATION_NOT_FOUND) — Conversation Not Found
- `404` [`NO_ACTIVE_RUN`](/errors/NO_ACTIVE_RUN) — No Active Run

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.status_response import StatusResponse
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
    api_instance = revengai.ConversationsApi(api_client)
    id = 'id_example' # str | Conversation UUID

    try:
        # Cancel an active run
        api_response = api_instance.cancel_run(id)
        print("The response of ConversationsApi->cancel_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->cancel_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Conversation UUID | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **confirm_tool**
> StatusResponse confirm_tool(id, confirm_tool_input_body)

Approve or reject a pending tool confirmation

Responds to a pending tool confirmation request. The agent pauses before executing certain tools and emits a `TOOL_CONFIRMATION_REQUIRED` event. Use this endpoint to approve or reject the tool call. Returns 404 if no confirmation is pending.

**Error codes:**
- `400` [`INVALID_CONVERSATION_ID`](/errors/INVALID_CONVERSATION_ID) — Invalid Conversation ID
- `404` [`CONVERSATION_NOT_FOUND`](/errors/CONVERSATION_NOT_FOUND) — Conversation Not Found
- `404` [`NO_PENDING_CONFIRMATION`](/errors/NO_PENDING_CONFIRMATION) — No Pending Confirmation

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.confirm_tool_input_body import ConfirmToolInputBody
from revengai.models.status_response import StatusResponse
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
    api_instance = revengai.ConversationsApi(api_client)
    id = 'id_example' # str | Conversation UUID
    confirm_tool_input_body = revengai.ConfirmToolInputBody() # ConfirmToolInputBody | 

    try:
        # Approve or reject a pending tool confirmation
        api_response = api_instance.confirm_tool(id, confirm_tool_input_body)
        print("The response of ConversationsApi->confirm_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->confirm_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Conversation UUID | 
 **confirm_tool_input_body** | [**ConfirmToolInputBody**](ConfirmToolInputBody.md)|  | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

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

# **create_conversation**
> Conversation create_conversation(create_conversation_request)

Create a new conversation

Creates a new conversation for the authenticated user. Optionally include a binary analysis context to scope the assistant to a specific analysis.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.conversation import Conversation
from revengai.models.create_conversation_request import CreateConversationRequest
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
    api_instance = revengai.ConversationsApi(api_client)
    create_conversation_request = revengai.CreateConversationRequest() # CreateConversationRequest | 

    try:
        # Create a new conversation
        api_response = api_instance.create_conversation(create_conversation_request)
        print("The response of ConversationsApi->create_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->create_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_conversation_request** | [**CreateConversationRequest**](CreateConversationRequest.md)|  | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> ConversationWithEvents get_conversation(id)

Get a conversation with its events

Returns the conversation metadata along with all persisted events. Useful for reconstructing the full conversation history on page load.

**Error codes:**
- `400` [`INVALID_CONVERSATION_ID`](/errors/INVALID_CONVERSATION_ID) — Invalid Conversation ID
- `404` [`CONVERSATION_NOT_FOUND`](/errors/CONVERSATION_NOT_FOUND) — Conversation Not Found

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.conversation_with_events import ConversationWithEvents
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
    api_instance = revengai.ConversationsApi(api_client)
    id = 'id_example' # str | Conversation UUID

    try:
        # Get a conversation with its events
        api_response = api_instance.get_conversation(id)
        print("The response of ConversationsApi->get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Conversation UUID | 

### Return type

[**ConversationWithEvents**](ConversationWithEvents.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **list_conversations**
> List[Conversation] list_conversations()

List conversations for the authenticated user

Returns all conversations owned by the authenticated user, ordered by most recently updated.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.conversation import Conversation
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
    api_instance = revengai.ConversationsApi(api_client)

    try:
        # List conversations for the authenticated user
        api_response = api_instance.list_conversations()
        print("The response of ConversationsApi->list_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->list_conversations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Conversation]**](Conversation.md)

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

# **send_message**
> StatusResponse send_message(id, send_message_request)

Send a message and start an agentic run

Sends a user message to the conversation and kicks off an agentic processing loop in the background. Returns immediately with 202 Accepted. Subscribe to `/v2/conversations/{id}/events` via SSE to receive real-time updates including text deltas, tool calls, and run lifecycle events.

**Error codes:**
- `400` [`BAD_REQUEST`](/errors/BAD_REQUEST) — Bad Request
- `400` [`INVALID_CONVERSATION_ID`](/errors/INVALID_CONVERSATION_ID) — Invalid Conversation ID
- `404` [`CONVERSATION_NOT_FOUND`](/errors/CONVERSATION_NOT_FOUND) — Conversation Not Found
- `403` [`ACCESS_DENIED`](/errors/ACCESS_DENIED) — Access Denied
- `402` [`INSUFFICIENT_CREDITS`](/errors/INSUFFICIENT_CREDITS) — Insufficient Credits
- `409` [`RUN_ALREADY_ACTIVE`](/errors/RUN_ALREADY_ACTIVE) — Run Already Active

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.send_message_request import SendMessageRequest
from revengai.models.status_response import StatusResponse
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
    api_instance = revengai.ConversationsApi(api_client)
    id = 'id_example' # str | Conversation UUID
    send_message_request = revengai.SendMessageRequest() # SendMessageRequest | 

    try:
        # Send a message and start an agentic run
        api_response = api_instance.send_message(id, send_message_request)
        print("The response of ConversationsApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Conversation UUID | 
 **send_message_request** | [**SendMessageRequest**](SendMessageRequest.md)|  | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_events**
> List[StreamEvents200ResponseInner] stream_events(id, last_event_id=last_event_id)

Stream conversation events (SSE)

Opens a Server-Sent Events stream for the given conversation. Events include run lifecycle updates, streaming text deltas, tool call progress, and more. Use the `last_event_id` query parameter to replay missed events after a reconnection.

### Example

* Api Key Authentication (APIKey):

```python
import revengai
from revengai.models.stream_events200_response_inner import StreamEvents200ResponseInner
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
    api_instance = revengai.ConversationsApi(api_client)
    id = 'id_example' # str | Conversation UUID
    last_event_id = 56 # int | Replay events after this ID (optional)

    try:
        # Stream conversation events (SSE)
        api_response = api_instance.stream_events(id, last_event_id=last_event_id)
        print("The response of ConversationsApi->stream_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->stream_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Conversation UUID | 
 **last_event_id** | **int**| Replay events after this ID | [optional] 

### Return type

[**List[StreamEvents200ResponseInner]**](StreamEvents200ResponseInner.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

