# RevEng.AI Python SDK

This is the Python SDK for the RevEng.AI API.

To use the SDK you will first need to obtain an API key from [https://reveng.ai](https://reveng.ai/register).

## Installation
Once you have the API key you can install the SDK via pip:
```bash
pip install revengai
```

## Usage

The following is an example of how to use the SDK to get the logs of an analysis:

```python
import os
import revengai

configuration = revengai.Configuration(api_key={'APIKey': os.environ["API_KEY"]})

# Enter a context with an instance of the API client
with revengai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = revengai.AnalysesCoreApi(api_client)
    analysis_id = 715320

    try:
        # Gets the logs of an analysis
        api_response = api_instance.get_analysis_logs(analysis_id)
        print("The response of AnalysesCoreApi->get_analysis_logs:\n")
        print(api_response)
    except Exception as e:
        print("Exception when calling AnalysesCoreApi->get_analysis_logs: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.reveng.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentApi* | [**check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get**](docs/AgentApi.md#check_capabilities_task_status_v2_analyses_analysis_id_agent_capabilities_status_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities/status | Check the status of a capabilities analysis workflow
*AgentApi* | [**check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get**](docs/AgentApi.md#check_report_analysis_task_status_v2_analyses_analysis_id_agent_report_analysis_status_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis/status | Check the status of a report analysis workflow
*AgentApi* | [**check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get**](docs/AgentApi.md#check_triage_task_status_v2_analyses_analysis_id_agent_triage_status_get) | **GET** /v2/analyses/{analysis_id}/agent/triage/status | Check the status of a triage analysis workflow
*AgentApi* | [**create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post**](docs/AgentApi.md#create_capabilities_task_v2_analyses_analysis_id_agent_capabilities_post) | **POST** /v2/analyses/{analysis_id}/agent/capabilities | Queues a capabilities analysis workflow process
*AgentApi* | [**create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post**](docs/AgentApi.md#create_report_analysis_task_v2_analyses_analysis_id_agent_report_analysis_post) | **POST** /v2/analyses/{analysis_id}/agent/report-analysis | Queues a combined report analysis workflow process
*AgentApi* | [**create_triage_task_v2_analyses_analysis_id_agent_triage_post**](docs/AgentApi.md#create_triage_task_v2_analyses_analysis_id_agent_triage_post) | **POST** /v2/analyses/{analysis_id}/agent/triage | Queues a triage analysis workflow process
*AgentApi* | [**get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get**](docs/AgentApi.md#get_capabilities_result_v2_analyses_analysis_id_agent_capabilities_get) | **GET** /v2/analyses/{analysis_id}/agent/capabilities | Get Capabilities Result
*AgentApi* | [**get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get**](docs/AgentApi.md#get_report_analysis_result_v2_analyses_analysis_id_agent_report_analysis_get) | **GET** /v2/analyses/{analysis_id}/agent/report-analysis | Get Report Analysis Result
*AgentApi* | [**get_triage_result_v2_analyses_analysis_id_agent_triage_get**](docs/AgentApi.md#get_triage_result_v2_analyses_analysis_id_agent_triage_get) | **GET** /v2/analyses/{analysis_id}/agent/triage | Get Triage Result
*AnalysesBulkActionsApi* | [**bulk_add_analysis_tags**](docs/AnalysesBulkActionsApi.md#bulk_add_analysis_tags) | **PATCH** /v2/analyses/tags/add | Bulk Add Analysis Tags
*AnalysesBulkActionsApi* | [**bulk_delete_analyses**](docs/AnalysesBulkActionsApi.md#bulk_delete_analyses) | **PATCH** /v2/analyses/delete | Bulk Delete Analyses
*AnalysesCommentsApi* | [**create_analysis_comment**](docs/AnalysesCommentsApi.md#create_analysis_comment) | **POST** /v2/analyses/{analysis_id}/comments | Create a comment for this analysis
*AnalysesCommentsApi* | [**delete_analysis_comment**](docs/AnalysesCommentsApi.md#delete_analysis_comment) | **DELETE** /v2/analyses/{analysis_id}/comments/{comment_id} | Delete a comment
*AnalysesCommentsApi* | [**get_analysis_comments**](docs/AnalysesCommentsApi.md#get_analysis_comments) | **GET** /v2/analyses/{analysis_id}/comments | Get comments for this analysis
*AnalysesCommentsApi* | [**update_analysis_comment**](docs/AnalysesCommentsApi.md#update_analysis_comment) | **PATCH** /v2/analyses/{analysis_id}/comments/{comment_id} | Update a comment
*AnalysesCoreApi* | [**create_analysis**](docs/AnalysesCoreApi.md#create_analysis) | **POST** /v2/analyses | Create Analysis
*AnalysesCoreApi* | [**delete_analysis**](docs/AnalysesCoreApi.md#delete_analysis) | **DELETE** /v2/analyses/{analysis_id} | Delete Analysis
*AnalysesCoreApi* | [**get_analysis_basic_info**](docs/AnalysesCoreApi.md#get_analysis_basic_info) | **GET** /v2/analyses/{analysis_id}/basic | Gets basic analysis information
*AnalysesCoreApi* | [**get_analysis_function_map**](docs/AnalysesCoreApi.md#get_analysis_function_map) | **GET** /v2/analyses/{analysis_id}/func_maps | Get Analysis Function Map
*AnalysesCoreApi* | [**get_analysis_logs**](docs/AnalysesCoreApi.md#get_analysis_logs) | **GET** /v2/analyses/{analysis_id}/logs | Gets the logs of an analysis
*AnalysesCoreApi* | [**get_analysis_params**](docs/AnalysesCoreApi.md#get_analysis_params) | **GET** /v2/analyses/{analysis_id}/params | Gets analysis param information
*AnalysesCoreApi* | [**get_analysis_queue_position**](docs/AnalysesCoreApi.md#get_analysis_queue_position) | **GET** /v2/analyses/{analysis_id}/queue-position | Get the queue position of an analysis
*AnalysesCoreApi* | [**get_analysis_status**](docs/AnalysesCoreApi.md#get_analysis_status) | **GET** /v2/analyses/{analysis_id}/status | Gets the status of an analysis
*AnalysesCoreApi* | [**insert_analysis_log**](docs/AnalysesCoreApi.md#insert_analysis_log) | **POST** /v2/analyses/{analysis_id}/logs | Insert a log entry for an analysis
*AnalysesCoreApi* | [**list_analyses**](docs/AnalysesCoreApi.md#list_analyses) | **GET** /v2/analyses/list | Gets the most recent analyses
*AnalysesCoreApi* | [**lookup_binary_id**](docs/AnalysesCoreApi.md#lookup_binary_id) | **GET** /v2/analyses/lookup/{binary_id} | Gets the analysis ID from binary ID
*AnalysesCoreApi* | [**put_analysis_strings**](docs/AnalysesCoreApi.md#put_analysis_strings) | **PUT** /v2/analyses/{analysis_id}/strings | Add strings to the analysis
*AnalysesCoreApi* | [**requeue_analysis**](docs/AnalysesCoreApi.md#requeue_analysis) | **POST** /v2/analyses/{analysis_id}/requeue | Requeue Analysis
*AnalysesCoreApi* | [**update_analysis**](docs/AnalysesCoreApi.md#update_analysis) | **PATCH** /v2/analyses/{analysis_id} | Update Analysis
*AnalysesCoreApi* | [**update_analysis_tags**](docs/AnalysesCoreApi.md#update_analysis_tags) | **PATCH** /v2/analyses/{analysis_id}/tags | Update Analysis Tags
*AnalysesCoreApi* | [**upload_file**](docs/AnalysesCoreApi.md#upload_file) | **POST** /v2/upload | Upload File
*AnalysesResultsMetadataApi* | [**get_analysis_functions_paginated**](docs/AnalysesResultsMetadataApi.md#get_analysis_functions_paginated) | **GET** /v2/analyses/{analysis_id}/functions | Get functions from analysis
*AnalysesResultsMetadataApi* | [**get_capabilities**](docs/AnalysesResultsMetadataApi.md#get_capabilities) | **GET** /v2/analyses/{analysis_id}/capabilities | Gets the capabilities from the analysis
*AnalysesResultsMetadataApi* | [**get_functions_list**](docs/AnalysesResultsMetadataApi.md#get_functions_list) | **GET** /v2/analyses/{analysis_id}/functions/list | Gets functions from analysis
*AnalysesResultsMetadataApi* | [**get_pdf**](docs/AnalysesResultsMetadataApi.md#get_pdf) | **GET** /v2/analyses/{analysis_id}/pdf | Gets the PDF found in the analysis
*AnalysesResultsMetadataApi* | [**get_sbom**](docs/AnalysesResultsMetadataApi.md#get_sbom) | **GET** /v2/analyses/{analysis_id}/sbom | Gets the software-bill-of-materials (SBOM) found in the analysis
*AnalysesResultsMetadataApi* | [**get_tags**](docs/AnalysesResultsMetadataApi.md#get_tags) | **GET** /v2/analyses/{analysis_id}/tags | Get function tags with maliciousness score
*AnalysesResultsMetadataApi* | [**get_vulnerabilities**](docs/AnalysesResultsMetadataApi.md#get_vulnerabilities) | **GET** /v2/analyses/{analysis_id}/vulnerabilities | Gets the vulnerabilities found in the analysis
*AnalysesXRefsApi* | [**get_xref_by_vaddr**](docs/AnalysesXRefsApi.md#get_xref_by_vaddr) | **GET** /v2/analyses/{analysis_id}/xrefs/{vaddr} | [Beta] Look up xrefs by virtual address
*AuthenticationUsersApi* | [**get_requester_user_info**](docs/AuthenticationUsersApi.md#get_requester_user_info) | **GET** /v2/users/me | Get the requesters user information
*AuthenticationUsersApi* | [**get_user**](docs/AuthenticationUsersApi.md#get_user) | **GET** /v2/users/{user_id} | Get a user&#39;s public information
*AuthenticationUsersApi* | [**get_user_activity**](docs/AuthenticationUsersApi.md#get_user_activity) | **GET** /v2/users/activity | Get auth user activity
*AuthenticationUsersApi* | [**get_user_comments**](docs/AuthenticationUsersApi.md#get_user_comments) | **GET** /v2/users/me/comments | Get comments by user
*AuthenticationUsersApi* | [**submit_user_feedback**](docs/AuthenticationUsersApi.md#submit_user_feedback) | **POST** /v2/users/feedback | Submit feedback about the application
*BinariesApi* | [**download_zipped_binary**](docs/BinariesApi.md#download_zipped_binary) | **GET** /v2/binaries/{binary_id}/download-zipped | Downloads a zipped binary with password protection
*BinariesApi* | [**get_binary_additional_details**](docs/BinariesApi.md#get_binary_additional_details) | **GET** /v2/binaries/{binary_id}/additional-details | Gets the additional details of a binary
*BinariesApi* | [**get_binary_additional_details_status**](docs/BinariesApi.md#get_binary_additional_details_status) | **GET** /v2/binaries/{binary_id}/additional-details/status | Gets the status of the additional details task for a binary
*BinariesApi* | [**get_binary_details**](docs/BinariesApi.md#get_binary_details) | **GET** /v2/binaries/{binary_id}/details | Gets the details of a binary
*BinariesApi* | [**get_binary_die_info**](docs/BinariesApi.md#get_binary_die_info) | **GET** /v2/binaries/{binary_id}/die-info | Gets the die info of a binary
*BinariesApi* | [**get_binary_externals**](docs/BinariesApi.md#get_binary_externals) | **GET** /v2/binaries/{binary_id}/externals | Gets the external details of a binary
*BinariesApi* | [**get_binary_related_status**](docs/BinariesApi.md#get_binary_related_status) | **GET** /v2/binaries/{binary_id}/related/status | Gets the status of the unpack binary task for a binary
*BinariesApi* | [**get_related_binaries**](docs/BinariesApi.md#get_related_binaries) | **GET** /v2/binaries/{binary_id}/related | Gets the related binaries of a binary.
*CollectionsApi* | [**create_collection**](docs/CollectionsApi.md#create_collection) | **POST** /v2/collections | Creates new collection information
*CollectionsApi* | [**delete_collection**](docs/CollectionsApi.md#delete_collection) | **DELETE** /v2/collections/{collection_id} | Deletes a collection
*CollectionsApi* | [**get_collection**](docs/CollectionsApi.md#get_collection) | **GET** /v2/collections/{collection_id} | Returns a collection
*CollectionsApi* | [**list_collections**](docs/CollectionsApi.md#list_collections) | **GET** /v2/collections | Gets basic collections information
*CollectionsApi* | [**update_collection**](docs/CollectionsApi.md#update_collection) | **PATCH** /v2/collections/{collection_id} | Updates a collection
*CollectionsApi* | [**update_collection_binaries**](docs/CollectionsApi.md#update_collection_binaries) | **PATCH** /v2/collections/{collection_id}/binaries | Updates a collection binaries
*CollectionsApi* | [**update_collection_tags**](docs/CollectionsApi.md#update_collection_tags) | **PATCH** /v2/collections/{collection_id}/tags | Updates a collection tags
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /v2/config | Get Config
*ConversationsApi* | [**cancel_run**](docs/ConversationsApi.md#cancel_run) | **POST** /v2/conversations/{id}/cancel | Cancel an active run
*ConversationsApi* | [**confirm_tool**](docs/ConversationsApi.md#confirm_tool) | **POST** /v2/conversations/{id}/confirm | Approve or reject a pending tool confirmation
*ConversationsApi* | [**create_conversation**](docs/ConversationsApi.md#create_conversation) | **POST** /v2/conversations | Create a new conversation
*ConversationsApi* | [**get_conversation**](docs/ConversationsApi.md#get_conversation) | **GET** /v2/conversations/{id} | Get a conversation with its events
*ConversationsApi* | [**list_conversations**](docs/ConversationsApi.md#list_conversations) | **GET** /v2/conversations | List conversations for the authenticated user
*ConversationsApi* | [**send_message**](docs/ConversationsApi.md#send_message) | **POST** /v2/conversations/{id}/messages | Send a message and start an agentic run
*ConversationsApi* | [**stream_events**](docs/ConversationsApi.md#stream_events) | **GET** /v2/conversations/{id}/events | Stream conversation events (SSE)
*ExternalSourcesApi* | [**create_external_task_vt**](docs/ExternalSourcesApi.md#create_external_task_vt) | **POST** /v2/analysis/{analysis_id}/external/vt | Pulls data from VirusTotal
*ExternalSourcesApi* | [**get_vt_data**](docs/ExternalSourcesApi.md#get_vt_data) | **GET** /v2/analysis/{analysis_id}/external/vt | Get VirusTotal data
*ExternalSourcesApi* | [**get_vt_task_status**](docs/ExternalSourcesApi.md#get_vt_task_status) | **GET** /v2/analysis/{analysis_id}/external/vt/status | Check the status of VirusTotal data retrieval
*FirmwareApi* | [**get_binaries_for_firmware_task**](docs/FirmwareApi.md#get_binaries_for_firmware_task) | **GET** /v2/firmware/get-binaries/{task_id} | Upload firmware for unpacking
*FirmwareApi* | [**upload_firmware**](docs/FirmwareApi.md#upload_firmware) | **POST** /v2/firmware | Upload firmware for unpacking
*FunctionsAIDecompilationApi* | [**create_ai_decompilation_comment**](docs/FunctionsAIDecompilationApi.md#create_ai_decompilation_comment) | **POST** /v2/functions/{function_id}/ai-decompilation/comments | Create a comment for this function
*FunctionsAIDecompilationApi* | [**create_ai_decompilation_task**](docs/FunctionsAIDecompilationApi.md#create_ai_decompilation_task) | **POST** /v2/functions/{function_id}/ai-decompilation | Begins AI Decompilation Process
*FunctionsAIDecompilationApi* | [**delete_ai_decompilation_comment**](docs/FunctionsAIDecompilationApi.md#delete_ai_decompilation_comment) | **DELETE** /v2/functions/{function_id}/ai-decompilation/comments/{comment_id} | Delete a comment
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_comments**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_comments) | **GET** /v2/functions/{function_id}/ai-decompilation/comments | Get comments for this function
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_rating**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_rating) | **GET** /v2/functions/{function_id}/ai-decompilation/rating | Get rating for AI decompilation
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_task_result**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_task_result) | **GET** /v2/functions/{function_id}/ai-decompilation | Polls AI Decompilation Process
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_task_status**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_task_status) | **GET** /v2/functions/{function_id}/ai-decompilation/status | Check the status of a function ai decompilation
*FunctionsAIDecompilationApi* | [**update_ai_decompilation_comment**](docs/FunctionsAIDecompilationApi.md#update_ai_decompilation_comment) | **PATCH** /v2/functions/{function_id}/ai-decompilation/comments/{comment_id} | Update a comment
*FunctionsAIDecompilationApi* | [**upsert_ai_decompilation_rating**](docs/FunctionsAIDecompilationApi.md#upsert_ai_decompilation_rating) | **PATCH** /v2/functions/{function_id}/ai-decompilation/rating | Upsert rating for AI decompilation
*FunctionsCoreApi* | [**ai_unstrip**](docs/FunctionsCoreApi.md#ai_unstrip) | **POST** /v2/analyses/{analysis_id}/functions/ai-unstrip | Performs matching and auto-unstrip for an analysis and its functions
*FunctionsCoreApi* | [**analysis_function_matching**](docs/FunctionsCoreApi.md#analysis_function_matching) | **POST** /v2/analyses/{analysis_id}/functions/matches | Perform matching for the functions of an analysis
*FunctionsCoreApi* | [**auto_unstrip**](docs/FunctionsCoreApi.md#auto_unstrip) | **POST** /v2/analyses/{analysis_id}/functions/auto-unstrip | Performs matching and auto-unstrip for an analysis and its functions
*FunctionsCoreApi* | [**batch_function_matching**](docs/FunctionsCoreApi.md#batch_function_matching) | **POST** /v2/functions/matches | Perform function matching for an arbitrary batch of functions, binaries or collections
*FunctionsCoreApi* | [**cancel_ai_unstrip**](docs/FunctionsCoreApi.md#cancel_ai_unstrip) | **DELETE** /v2/analyses/{analysis_id}/functions/ai-unstrip/cancel | Cancels a running ai-unstrip
*FunctionsCoreApi* | [**cancel_auto_unstrip**](docs/FunctionsCoreApi.md#cancel_auto_unstrip) | **DELETE** /v2/analyses/{analysis_id}/functions/unstrip/cancel | Cancels a running auto-unstrip
*FunctionsCoreApi* | [**get_analysis_strings**](docs/FunctionsCoreApi.md#get_analysis_strings) | **GET** /v2/analyses/{analysis_id}/functions/strings | Get string information found in the Analysis
*FunctionsCoreApi* | [**get_analysis_strings_status**](docs/FunctionsCoreApi.md#get_analysis_strings_status) | **GET** /v2/analyses/{analysis_id}/functions/strings/status | Get string processing state for the Analysis
*FunctionsCoreApi* | [**get_function_blocks**](docs/FunctionsCoreApi.md#get_function_blocks) | **GET** /v2/functions/{function_id}/blocks | Get disassembly blocks related to the function
*FunctionsCoreApi* | [**get_function_callees_callers**](docs/FunctionsCoreApi.md#get_function_callees_callers) | **GET** /v2/functions/{function_id}/callees_callers | Get list of functions that call or are called by the specified function
*FunctionsCoreApi* | [**get_function_callees_callers_bulk**](docs/FunctionsCoreApi.md#get_function_callees_callers_bulk) | **GET** /v2/functions/callees_callers | Get list of functions that call or are called for a list of functions
*FunctionsCoreApi* | [**get_function_capabilities**](docs/FunctionsCoreApi.md#get_function_capabilities) | **GET** /v2/functions/{function_id}/capabilities | Retrieve a functions capabilities
*FunctionsCoreApi* | [**get_function_details**](docs/FunctionsCoreApi.md#get_function_details) | **GET** /v2/functions/{function_id} | Get function details
*FunctionsCoreApi* | [**get_function_strings**](docs/FunctionsCoreApi.md#get_function_strings) | **GET** /v2/functions/{function_id}/strings | Get string information found in the function
*FunctionsDataTypesApi* | [**generate_function_data_types_for_analysis**](docs/FunctionsDataTypesApi.md#generate_function_data_types_for_analysis) | **POST** /v2/analyses/{analysis_id}/functions/data_types | Generate Function Data Types
*FunctionsDataTypesApi* | [**generate_function_data_types_for_functions**](docs/FunctionsDataTypesApi.md#generate_function_data_types_for_functions) | **POST** /v2/functions/data_types | Generate Function Data Types for an arbitrary list of functions
*FunctionsDataTypesApi* | [**get_function_data_types**](docs/FunctionsDataTypesApi.md#get_function_data_types) | **GET** /v2/analyses/{analysis_id}/functions/{function_id}/data_types | Get Function Data Types
*FunctionsDataTypesApi* | [**list_function_data_types_for_analysis**](docs/FunctionsDataTypesApi.md#list_function_data_types_for_analysis) | **GET** /v2/analyses/{analysis_id}/functions/data_types | List Function Data Types
*FunctionsDataTypesApi* | [**list_function_data_types_for_functions**](docs/FunctionsDataTypesApi.md#list_function_data_types_for_functions) | **GET** /v2/functions/data_types | List Function Data Types
*FunctionsDataTypesApi* | [**update_function_data_types**](docs/FunctionsDataTypesApi.md#update_function_data_types) | **PUT** /v2/analyses/{analysis_id}/functions/{function_id}/data_types | Update Function Data Types
*FunctionsRenamingHistoryApi* | [**batch_rename_function**](docs/FunctionsRenamingHistoryApi.md#batch_rename_function) | **POST** /v2/functions/rename/batch | Batch Rename Functions
*FunctionsRenamingHistoryApi* | [**get_function_name_history**](docs/FunctionsRenamingHistoryApi.md#get_function_name_history) | **GET** /v2/functions/history/{function_id} | Get Function Name History
*FunctionsRenamingHistoryApi* | [**rename_function_id**](docs/FunctionsRenamingHistoryApi.md#rename_function_id) | **POST** /v2/functions/rename/{function_id} | Rename Function
*FunctionsRenamingHistoryApi* | [**revert_function_name**](docs/FunctionsRenamingHistoryApi.md#revert_function_name) | **POST** /v2/functions/history/{function_id}/{history_id} | Revert the function name
*ModelsApi* | [**get_models**](docs/ModelsApi.md#get_models) | **GET** /v2/models | Gets models
*SearchApi* | [**search_binaries**](docs/SearchApi.md#search_binaries) | **GET** /v2/search/binaries | Binaries search
*SearchApi* | [**search_collections**](docs/SearchApi.md#search_collections) | **GET** /v2/search/collections | Collections search
*SearchApi* | [**search_functions**](docs/SearchApi.md#search_functions) | **GET** /v2/search/functions | Functions search
*SearchApi* | [**search_tags**](docs/SearchApi.md#search_tags) | **GET** /v2/search/tags | Tags search


## Documentation For Models

 - [APIError](docs/APIError.md)
 - [AdditionalDetailsStatusResponse](docs/AdditionalDetailsStatusResponse.md)
 - [Addr](docs/Addr.md)
 - [AiDecompilationRating](docs/AiDecompilationRating.md)
 - [AiDecompilationTaskStatus](docs/AiDecompilationTaskStatus.md)
 - [AiUnstripRequest](docs/AiUnstripRequest.md)
 - [AnalysisAccessInfo](docs/AnalysisAccessInfo.md)
 - [AnalysisBulkAddTagsRequest](docs/AnalysisBulkAddTagsRequest.md)
 - [AnalysisBulkAddTagsResponse](docs/AnalysisBulkAddTagsResponse.md)
 - [AnalysisBulkAddTagsResponseItem](docs/AnalysisBulkAddTagsResponseItem.md)
 - [AnalysisConfig](docs/AnalysisConfig.md)
 - [AnalysisCreateRequest](docs/AnalysisCreateRequest.md)
 - [AnalysisCreateResponse](docs/AnalysisCreateResponse.md)
 - [AnalysisDetailResponse](docs/AnalysisDetailResponse.md)
 - [AnalysisFunctionMapping](docs/AnalysisFunctionMapping.md)
 - [AnalysisFunctionMatchingRequest](docs/AnalysisFunctionMatchingRequest.md)
 - [AnalysisFunctions](docs/AnalysisFunctions.md)
 - [AnalysisFunctionsList](docs/AnalysisFunctionsList.md)
 - [AnalysisRecord](docs/AnalysisRecord.md)
 - [AnalysisReport](docs/AnalysisReport.md)
 - [AnalysisScope](docs/AnalysisScope.md)
 - [AnalysisStringInput](docs/AnalysisStringInput.md)
 - [AnalysisStringsResponse](docs/AnalysisStringsResponse.md)
 - [AnalysisStringsStatusResponse](docs/AnalysisStringsStatusResponse.md)
 - [AnalysisTags](docs/AnalysisTags.md)
 - [AnalysisUpdateRequest](docs/AnalysisUpdateRequest.md)
 - [AnalysisUpdateTagsRequest](docs/AnalysisUpdateTagsRequest.md)
 - [AnalysisUpdateTagsResponse](docs/AnalysisUpdateTagsResponse.md)
 - [ApiCall](docs/ApiCall.md)
 - [AppApiRestV2AgentSchemaCapability](docs/AppApiRestV2AgentSchemaCapability.md)
 - [AppApiRestV2AnalysesEnumsOrderBy](docs/AppApiRestV2AnalysesEnumsOrderBy.md)
 - [AppApiRestV2CollectionsEnumsOrderBy](docs/AppApiRestV2CollectionsEnumsOrderBy.md)
 - [AppApiRestV2FunctionsResponsesFunction](docs/AppApiRestV2FunctionsResponsesFunction.md)
 - [AppApiRestV2FunctionsTypesFunction](docs/AppApiRestV2FunctionsTypesFunction.md)
 - [AppApiRestV2InfoTypesCapability](docs/AppApiRestV2InfoTypesCapability.md)
 - [Argument](docs/Argument.md)
 - [AutoRunAgents](docs/AutoRunAgents.md)
 - [AutoUnstripRequest](docs/AutoUnstripRequest.md)
 - [AutoUnstripResponse](docs/AutoUnstripResponse.md)
 - [BaseResponse](docs/BaseResponse.md)
 - [BaseResponseAdditionalDetailsStatusResponse](docs/BaseResponseAdditionalDetailsStatusResponse.md)
 - [BaseResponseAnalysisBulkAddTagsResponse](docs/BaseResponseAnalysisBulkAddTagsResponse.md)
 - [BaseResponseAnalysisCreateResponse](docs/BaseResponseAnalysisCreateResponse.md)
 - [BaseResponseAnalysisDetailResponse](docs/BaseResponseAnalysisDetailResponse.md)
 - [BaseResponseAnalysisFunctionMapping](docs/BaseResponseAnalysisFunctionMapping.md)
 - [BaseResponseAnalysisFunctions](docs/BaseResponseAnalysisFunctions.md)
 - [BaseResponseAnalysisFunctionsList](docs/BaseResponseAnalysisFunctionsList.md)
 - [BaseResponseAnalysisStringsResponse](docs/BaseResponseAnalysisStringsResponse.md)
 - [BaseResponseAnalysisStringsStatusResponse](docs/BaseResponseAnalysisStringsStatusResponse.md)
 - [BaseResponseAnalysisTags](docs/BaseResponseAnalysisTags.md)
 - [BaseResponseAnalysisUpdateTagsResponse](docs/BaseResponseAnalysisUpdateTagsResponse.md)
 - [BaseResponseBasic](docs/BaseResponseBasic.md)
 - [BaseResponseBinariesRelatedStatusResponse](docs/BaseResponseBinariesRelatedStatusResponse.md)
 - [BaseResponseBinaryAdditionalResponse](docs/BaseResponseBinaryAdditionalResponse.md)
 - [BaseResponseBinaryDetailsResponse](docs/BaseResponseBinaryDetailsResponse.md)
 - [BaseResponseBinaryExternalsResponse](docs/BaseResponseBinaryExternalsResponse.md)
 - [BaseResponseBinarySearchResponse](docs/BaseResponseBinarySearchResponse.md)
 - [BaseResponseBool](docs/BaseResponseBool.md)
 - [BaseResponseCalleesCallerFunctionsResponse](docs/BaseResponseCalleesCallerFunctionsResponse.md)
 - [BaseResponseCapabilities](docs/BaseResponseCapabilities.md)
 - [BaseResponseCapabilitiesAgentResponse](docs/BaseResponseCapabilitiesAgentResponse.md)
 - [BaseResponseChildBinariesResponse](docs/BaseResponseChildBinariesResponse.md)
 - [BaseResponseCollectionBinariesUpdateResponse](docs/BaseResponseCollectionBinariesUpdateResponse.md)
 - [BaseResponseCollectionResponse](docs/BaseResponseCollectionResponse.md)
 - [BaseResponseCollectionSearchResponse](docs/BaseResponseCollectionSearchResponse.md)
 - [BaseResponseCollectionTagsUpdateResponse](docs/BaseResponseCollectionTagsUpdateResponse.md)
 - [BaseResponseCommentResponse](docs/BaseResponseCommentResponse.md)
 - [BaseResponseConfigResponse](docs/BaseResponseConfigResponse.md)
 - [BaseResponseCreated](docs/BaseResponseCreated.md)
 - [BaseResponseDict](docs/BaseResponseDict.md)
 - [BaseResponseExternalResponse](docs/BaseResponseExternalResponse.md)
 - [BaseResponseFunctionBlocksResponse](docs/BaseResponseFunctionBlocksResponse.md)
 - [BaseResponseFunctionCapabilityResponse](docs/BaseResponseFunctionCapabilityResponse.md)
 - [BaseResponseFunctionDataTypes](docs/BaseResponseFunctionDataTypes.md)
 - [BaseResponseFunctionDataTypesList](docs/BaseResponseFunctionDataTypesList.md)
 - [BaseResponseFunctionSearchResponse](docs/BaseResponseFunctionSearchResponse.md)
 - [BaseResponseFunctionStringsResponse](docs/BaseResponseFunctionStringsResponse.md)
 - [BaseResponseFunctionTaskResponse](docs/BaseResponseFunctionTaskResponse.md)
 - [BaseResponseFunctionsDetailResponse](docs/BaseResponseFunctionsDetailResponse.md)
 - [BaseResponseGenerateFunctionDataTypes](docs/BaseResponseGenerateFunctionDataTypes.md)
 - [BaseResponseGenerationStatusList](docs/BaseResponseGenerationStatusList.md)
 - [BaseResponseGetAiDecompilationTask](docs/BaseResponseGetAiDecompilationTask.md)
 - [BaseResponseGetMeResponse](docs/BaseResponseGetMeResponse.md)
 - [BaseResponseGetPublicUserResponse](docs/BaseResponseGetPublicUserResponse.md)
 - [BaseResponseListCalleesCallerFunctionsResponse](docs/BaseResponseListCalleesCallerFunctionsResponse.md)
 - [BaseResponseListCollectionResults](docs/BaseResponseListCollectionResults.md)
 - [BaseResponseListCommentResponse](docs/BaseResponseListCommentResponse.md)
 - [BaseResponseListDieMatch](docs/BaseResponseListDieMatch.md)
 - [BaseResponseListFunctionNameHistory](docs/BaseResponseListFunctionNameHistory.md)
 - [BaseResponseListSBOM](docs/BaseResponseListSBOM.md)
 - [BaseResponseListUserActivityResponse](docs/BaseResponseListUserActivityResponse.md)
 - [BaseResponseLogs](docs/BaseResponseLogs.md)
 - [BaseResponseModelsResponse](docs/BaseResponseModelsResponse.md)
 - [BaseResponseParams](docs/BaseResponseParams.md)
 - [BaseResponseQueuedWorkflowTaskResponse](docs/BaseResponseQueuedWorkflowTaskResponse.md)
 - [BaseResponseRecent](docs/BaseResponseRecent.md)
 - [BaseResponseReportAnalysisResponse](docs/BaseResponseReportAnalysisResponse.md)
 - [BaseResponseStatus](docs/BaseResponseStatus.md)
 - [BaseResponseStr](docs/BaseResponseStr.md)
 - [BaseResponseTagSearchResponse](docs/BaseResponseTagSearchResponse.md)
 - [BaseResponseTaskResponse](docs/BaseResponseTaskResponse.md)
 - [BaseResponseTaskStatusResponse](docs/BaseResponseTaskStatusResponse.md)
 - [BaseResponseTriageReportResponse](docs/BaseResponseTriageReportResponse.md)
 - [BaseResponseUnionGetAiDecompilationRatingResponseNoneType](docs/BaseResponseUnionGetAiDecompilationRatingResponseNoneType.md)
 - [BaseResponseUploadResponse](docs/BaseResponseUploadResponse.md)
 - [BaseResponseVulnerabilities](docs/BaseResponseVulnerabilities.md)
 - [BaseResponseXrefResponse](docs/BaseResponseXrefResponse.md)
 - [Basic](docs/Basic.md)
 - [BinariesRelatedStatusResponse](docs/BinariesRelatedStatusResponse.md)
 - [BinariesTaskStatus](docs/BinariesTaskStatus.md)
 - [BinaryAdditionalDetailsDataResponse](docs/BinaryAdditionalDetailsDataResponse.md)
 - [BinaryAdditionalResponse](docs/BinaryAdditionalResponse.md)
 - [BinaryConfig](docs/BinaryConfig.md)
 - [BinaryDetailsResponse](docs/BinaryDetailsResponse.md)
 - [BinaryExternalsResponse](docs/BinaryExternalsResponse.md)
 - [BinarySearchResponse](docs/BinarySearchResponse.md)
 - [BinarySearchResult](docs/BinarySearchResult.md)
 - [BinaryTaskStatus](docs/BinaryTaskStatus.md)
 - [BulkDeleteAnalysesRequest](docs/BulkDeleteAnalysesRequest.md)
 - [CalleeFunctionInfo](docs/CalleeFunctionInfo.md)
 - [CalleesCallerFunctionsResponse](docs/CalleesCallerFunctionsResponse.md)
 - [CallerFunctionInfo](docs/CallerFunctionInfo.md)
 - [Capabilities](docs/Capabilities.md)
 - [CapabilitiesAgentResponse](docs/CapabilitiesAgentResponse.md)
 - [ChildBinariesResponse](docs/ChildBinariesResponse.md)
 - [CodeSignatureModel](docs/CodeSignatureModel.md)
 - [CollectionBinariesUpdateRequest](docs/CollectionBinariesUpdateRequest.md)
 - [CollectionBinariesUpdateResponse](docs/CollectionBinariesUpdateResponse.md)
 - [CollectionBinaryResponse](docs/CollectionBinaryResponse.md)
 - [CollectionCreateRequest](docs/CollectionCreateRequest.md)
 - [CollectionListItem](docs/CollectionListItem.md)
 - [CollectionResponse](docs/CollectionResponse.md)
 - [CollectionResponseBinariesInner](docs/CollectionResponseBinariesInner.md)
 - [CollectionScope](docs/CollectionScope.md)
 - [CollectionSearchResponse](docs/CollectionSearchResponse.md)
 - [CollectionSearchResult](docs/CollectionSearchResult.md)
 - [CollectionTagsUpdateRequest](docs/CollectionTagsUpdateRequest.md)
 - [CollectionTagsUpdateResponse](docs/CollectionTagsUpdateResponse.md)
 - [CollectionUpdateRequest](docs/CollectionUpdateRequest.md)
 - [CommentBase](docs/CommentBase.md)
 - [CommentResponse](docs/CommentResponse.md)
 - [CommentUpdateRequest](docs/CommentUpdateRequest.md)
 - [ConfigResponse](docs/ConfigResponse.md)
 - [ConfirmToolInputBody](docs/ConfirmToolInputBody.md)
 - [Connection](docs/Connection.md)
 - [Context](docs/Context.md)
 - [Conversation](docs/Conversation.md)
 - [ConversationContext](docs/ConversationContext.md)
 - [ConversationWithEvents](docs/ConversationWithEvents.md)
 - [CreateConversationRequest](docs/CreateConversationRequest.md)
 - [Created](docs/Created.md)
 - [DecompilationCommentContext](docs/DecompilationCommentContext.md)
 - [DieMatch](docs/DieMatch.md)
 - [DnsQuery](docs/DnsQuery.md)
 - [DrakvufFileMetadata](docs/DrakvufFileMetadata.md)
 - [DynamicExecutionStatus](docs/DynamicExecutionStatus.md)
 - [DynamicExecutionStatusResponse](docs/DynamicExecutionStatusResponse.md)
 - [ELFImportModel](docs/ELFImportModel.md)
 - [ELFModel](docs/ELFModel.md)
 - [ELFRelocation](docs/ELFRelocation.md)
 - [ELFSection](docs/ELFSection.md)
 - [ELFSecurity](docs/ELFSecurity.md)
 - [ELFSegment](docs/ELFSegment.md)
 - [ELFSymbol](docs/ELFSymbol.md)
 - [ElfDynamicEntry](docs/ElfDynamicEntry.md)
 - [EntrypointModel](docs/EntrypointModel.md)
 - [Enumeration](docs/Enumeration.md)
 - [ErrorBody](docs/ErrorBody.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [Event](docs/Event.md)
 - [EventCONTEXTCOMPACTED](docs/EventCONTEXTCOMPACTED.md)
 - [EventRUNCANCELLED](docs/EventRUNCANCELLED.md)
 - [EventRUNERROR](docs/EventRUNERROR.md)
 - [EventRUNFINISHED](docs/EventRUNFINISHED.md)
 - [EventRUNSTARTED](docs/EventRUNSTARTED.md)
 - [EventSTEPFINISHED](docs/EventSTEPFINISHED.md)
 - [EventSTEPSTARTED](docs/EventSTEPSTARTED.md)
 - [EventTEXTMESSAGECONTENT](docs/EventTEXTMESSAGECONTENT.md)
 - [EventTEXTMESSAGEEND](docs/EventTEXTMESSAGEEND.md)
 - [EventTEXTMESSAGESTART](docs/EventTEXTMESSAGESTART.md)
 - [EventTITLEUPDATED](docs/EventTITLEUPDATED.md)
 - [EventTOOLCALLARGSDELTA](docs/EventTOOLCALLARGSDELTA.md)
 - [EventTOOLCALLEND](docs/EventTOOLCALLEND.md)
 - [EventTOOLCALLRESULT](docs/EventTOOLCALLRESULT.md)
 - [EventTOOLCALLSTART](docs/EventTOOLCALLSTART.md)
 - [EventTOOLCONFIRMATIONREQUIRED](docs/EventTOOLCONFIRMATIONREQUIRED.md)
 - [ExportModel](docs/ExportModel.md)
 - [ExternalResponse](docs/ExternalResponse.md)
 - [ExtractedURL](docs/ExtractedURL.md)
 - [FileActivityEntry](docs/FileActivityEntry.md)
 - [FileFormat](docs/FileFormat.md)
 - [FileHashes](docs/FileHashes.md)
 - [FileMetadata](docs/FileMetadata.md)
 - [Filters](docs/Filters.md)
 - [FunctionBlockDestinationResponse](docs/FunctionBlockDestinationResponse.md)
 - [FunctionBlockResponse](docs/FunctionBlockResponse.md)
 - [FunctionBlocksResponse](docs/FunctionBlocksResponse.md)
 - [FunctionBoundary](docs/FunctionBoundary.md)
 - [FunctionCapabilityResponse](docs/FunctionCapabilityResponse.md)
 - [FunctionCommentCreateRequest](docs/FunctionCommentCreateRequest.md)
 - [FunctionDataTypes](docs/FunctionDataTypes.md)
 - [FunctionDataTypesList](docs/FunctionDataTypesList.md)
 - [FunctionDataTypesListItem](docs/FunctionDataTypesListItem.md)
 - [FunctionDataTypesParams](docs/FunctionDataTypesParams.md)
 - [FunctionDataTypesStatus](docs/FunctionDataTypesStatus.md)
 - [FunctionHeader](docs/FunctionHeader.md)
 - [FunctionInfoInput](docs/FunctionInfoInput.md)
 - [FunctionInfoInputFuncDepsInner](docs/FunctionInfoInputFuncDepsInner.md)
 - [FunctionInfoOutput](docs/FunctionInfoOutput.md)
 - [FunctionListItem](docs/FunctionListItem.md)
 - [FunctionLocalVariableResponse](docs/FunctionLocalVariableResponse.md)
 - [FunctionMapping](docs/FunctionMapping.md)
 - [FunctionMappingFull](docs/FunctionMappingFull.md)
 - [FunctionMatch](docs/FunctionMatch.md)
 - [FunctionMatchingFilters](docs/FunctionMatchingFilters.md)
 - [FunctionMatchingRequest](docs/FunctionMatchingRequest.md)
 - [FunctionMatchingResponse](docs/FunctionMatchingResponse.md)
 - [FunctionNameHistory](docs/FunctionNameHistory.md)
 - [FunctionParamResponse](docs/FunctionParamResponse.md)
 - [FunctionRename](docs/FunctionRename.md)
 - [FunctionRenameMap](docs/FunctionRenameMap.md)
 - [FunctionSearchResponse](docs/FunctionSearchResponse.md)
 - [FunctionSearchResult](docs/FunctionSearchResult.md)
 - [FunctionSourceType](docs/FunctionSourceType.md)
 - [FunctionString](docs/FunctionString.md)
 - [FunctionStringsResponse](docs/FunctionStringsResponse.md)
 - [FunctionTaskResponse](docs/FunctionTaskResponse.md)
 - [FunctionTaskStatus](docs/FunctionTaskStatus.md)
 - [FunctionTypeInput](docs/FunctionTypeInput.md)
 - [FunctionTypeOutput](docs/FunctionTypeOutput.md)
 - [FunctionsDetailResponse](docs/FunctionsDetailResponse.md)
 - [FunctionsListRename](docs/FunctionsListRename.md)
 - [GenerateFunctionDataTypes](docs/GenerateFunctionDataTypes.md)
 - [GenerationStatusList](docs/GenerationStatusList.md)
 - [GetAiDecompilationRatingResponse](docs/GetAiDecompilationRatingResponse.md)
 - [GetAiDecompilationTask](docs/GetAiDecompilationTask.md)
 - [GetMeResponse](docs/GetMeResponse.md)
 - [GetPublicUserResponse](docs/GetPublicUserResponse.md)
 - [GlobalVariable](docs/GlobalVariable.md)
 - [HttpRequest](docs/HttpRequest.md)
 - [IOC](docs/IOC.md)
 - [ISA](docs/ISA.md)
 - [IconModel](docs/IconModel.md)
 - [ImportModel](docs/ImportModel.md)
 - [InsertAnalysisLogRequest](docs/InsertAnalysisLogRequest.md)
 - [InverseFunctionMapItem](docs/InverseFunctionMapItem.md)
 - [InverseStringMapItem](docs/InverseStringMapItem.md)
 - [InverseValue](docs/InverseValue.md)
 - [ListCollectionResults](docs/ListCollectionResults.md)
 - [Logs](docs/Logs.md)
 - [MITRETechnique](docs/MITRETechnique.md)
 - [MatchedFunction](docs/MatchedFunction.md)
 - [MatchedFunctionSuggestion](docs/MatchedFunctionSuggestion.md)
 - [MemdumpEntry](docs/MemdumpEntry.md)
 - [MetaModel](docs/MetaModel.md)
 - [ModelName](docs/ModelName.md)
 - [ModelsResponse](docs/ModelsResponse.md)
 - [ModuleLoadEntry](docs/ModuleLoadEntry.md)
 - [MutexEntry](docs/MutexEntry.md)
 - [NameConfidence](docs/NameConfidence.md)
 - [NameSourceType](docs/NameSourceType.md)
 - [NetworkActivity](docs/NetworkActivity.md)
 - [Order](docs/Order.md)
 - [PDBDebugModel](docs/PDBDebugModel.md)
 - [PEModel](docs/PEModel.md)
 - [PaginationModel](docs/PaginationModel.md)
 - [Params](docs/Params.md)
 - [Platform](docs/Platform.md)
 - [ProcessActivityEntry](docs/ProcessActivityEntry.md)
 - [ProcessMemdumps](docs/ProcessMemdumps.md)
 - [ProcessNode](docs/ProcessNode.md)
 - [ProcessTree](docs/ProcessTree.md)
 - [PutAnalysisStringsRequest](docs/PutAnalysisStringsRequest.md)
 - [QueuePositionResponse](docs/QueuePositionResponse.md)
 - [QueuedWorkflowTaskResponse](docs/QueuedWorkflowTaskResponse.md)
 - [ReAnalysisForm](docs/ReAnalysisForm.md)
 - [Recent](docs/Recent.md)
 - [RegenerateTarget](docs/RegenerateTarget.md)
 - [RegistryOperation](docs/RegistryOperation.md)
 - [RelativeBinaryResponse](docs/RelativeBinaryResponse.md)
 - [ReportAnalysisResponse](docs/ReportAnalysisResponse.md)
 - [ReportEvent](docs/ReportEvent.md)
 - [ReportInfo](docs/ReportInfo.md)
 - [ReportOptions](docs/ReportOptions.md)
 - [SBOM](docs/SBOM.md)
 - [SBOMPackage](docs/SBOMPackage.md)
 - [SandboxOptions](docs/SandboxOptions.md)
 - [SandboxStartMethod](docs/SandboxStartMethod.md)
 - [SandboxTimeout](docs/SandboxTimeout.md)
 - [ScheduledTaskEntry](docs/ScheduledTaskEntry.md)
 - [ScrapeThirdPartyConfig](docs/ScrapeThirdPartyConfig.md)
 - [SectionModel](docs/SectionModel.md)
 - [SecurityModel](docs/SecurityModel.md)
 - [SegmentInfo](docs/SegmentInfo.md)
 - [SendMessageRequest](docs/SendMessageRequest.md)
 - [ServiceEntry](docs/ServiceEntry.md)
 - [SingleCodeCertificateModel](docs/SingleCodeCertificateModel.md)
 - [SingleCodeSignatureModel](docs/SingleCodeSignatureModel.md)
 - [SinglePDBEntryModel](docs/SinglePDBEntryModel.md)
 - [SingleSectionModel](docs/SingleSectionModel.md)
 - [SseEventContextCompactedData](docs/SseEventContextCompactedData.md)
 - [SseEventRunCancelledData](docs/SseEventRunCancelledData.md)
 - [SseEventRunErrorData](docs/SseEventRunErrorData.md)
 - [SseEventRunFinishedData](docs/SseEventRunFinishedData.md)
 - [SseEventRunStartedData](docs/SseEventRunStartedData.md)
 - [SseEventStepFinishedData](docs/SseEventStepFinishedData.md)
 - [SseEventStepStartedData](docs/SseEventStepStartedData.md)
 - [SseEventTextMessageContentData](docs/SseEventTextMessageContentData.md)
 - [SseEventTextMessageEndData](docs/SseEventTextMessageEndData.md)
 - [SseEventTextMessageStartData](docs/SseEventTextMessageStartData.md)
 - [SseEventTitleUpdatedData](docs/SseEventTitleUpdatedData.md)
 - [SseEventToolCallArgsDeltaData](docs/SseEventToolCallArgsDeltaData.md)
 - [SseEventToolCallEndData](docs/SseEventToolCallEndData.md)
 - [SseEventToolCallResultData](docs/SseEventToolCallResultData.md)
 - [SseEventToolCallStartData](docs/SseEventToolCallStartData.md)
 - [SseEventToolConfirmationRequiredData](docs/SseEventToolConfirmationRequiredData.md)
 - [StackVariable](docs/StackVariable.md)
 - [StartupInfo](docs/StartupInfo.md)
 - [StatusInput](docs/StatusInput.md)
 - [StatusOutput](docs/StatusOutput.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [StreamEvents200ResponseInner](docs/StreamEvents200ResponseInner.md)
 - [StringFunctions](docs/StringFunctions.md)
 - [StringSource](docs/StringSource.md)
 - [Structure](docs/Structure.md)
 - [StructureMember](docs/StructureMember.md)
 - [SubmitUserFeedbackRequest](docs/SubmitUserFeedbackRequest.md)
 - [Symbols](docs/Symbols.md)
 - [Tag](docs/Tag.md)
 - [TagItem](docs/TagItem.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagSearchResponse](docs/TagSearchResponse.md)
 - [TagSearchResult](docs/TagSearchResult.md)
 - [TaskResponse](docs/TaskResponse.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [TaskStatusResponse](docs/TaskStatusResponse.md)
 - [TimestampModel](docs/TimestampModel.md)
 - [TriageFunctionResponse](docs/TriageFunctionResponse.md)
 - [TriageReportResponse](docs/TriageReportResponse.md)
 - [Ttp](docs/Ttp.md)
 - [TypeDefinition](docs/TypeDefinition.md)
 - [UpdateFunctionDataTypes](docs/UpdateFunctionDataTypes.md)
 - [UploadFileType](docs/UploadFileType.md)
 - [UploadResponse](docs/UploadResponse.md)
 - [UpsertAiDecomplationRatingRequest](docs/UpsertAiDecomplationRatingRequest.md)
 - [UserActivityResponse](docs/UserActivityResponse.md)
 - [Vulnerabilities](docs/Vulnerabilities.md)
 - [Vulnerability](docs/Vulnerability.md)
 - [Workspace](docs/Workspace.md)
 - [XrefFromResponse](docs/XrefFromResponse.md)
 - [XrefResponse](docs/XrefResponse.md)
 - [XrefToResponse](docs/XrefToResponse.md)
