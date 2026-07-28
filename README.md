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
*AnalysesCoreApi* | [**add_user_string_to_analysis**](docs/AnalysesCoreApi.md#add_user_string_to_analysis) | **POST** /v3/analyses/{analysis_id}/user-provided-strings | Add a user-provided string to an analysis.
*AnalysesCoreApi* | [**get_analysis_basic_info**](docs/AnalysesCoreApi.md#get_analysis_basic_info) | **GET** /v3/analyses/{analysis_id}/basic | Get basic analysis information
*AnalysesCoreApi* | [**get_analysis_bytes**](docs/AnalysesCoreApi.md#get_analysis_bytes) | **GET** /v3/analyses/{analysis_id}/bytes | Get the bytes of a binary
*AnalysesCoreApi* | [**get_analysis_function_matches**](docs/AnalysesCoreApi.md#get_analysis_function_matches) | **GET** /v3/analyses/{analysis_id}/functions/matches | Get function-matching results for an analysis
*AnalysesCoreApi* | [**get_analysis_function_matching_status**](docs/AnalysesCoreApi.md#get_analysis_function_matching_status) | **GET** /v3/analyses/{analysis_id}/functions/matches/status | Get function-matching status for an analysis
*AnalysesCoreApi* | [**get_dynamic_execution_report**](docs/AnalysesCoreApi.md#get_dynamic_execution_report) | **GET** /v2/analyses/{analysis_id}/dynamic-execution/report | Get dynamic execution report
*AnalysesCoreApi* | [**get_dynamic_execution_status**](docs/AnalysesCoreApi.md#get_dynamic_execution_status) | **GET** /v2/analyses/{analysis_id}/dynamic-execution/status | Get dynamic execution status
*AnalysesCoreApi* | [**start_analysis_function_matching**](docs/AnalysesCoreApi.md#start_analysis_function_matching) | **POST** /v3/analyses/{analysis_id}/functions/matches | Start function matching for an analysis
*AnalysesCoreApi* | [**v3_get_analysis_auto_unstrip_status**](docs/AnalysesCoreApi.md#v3_get_analysis_auto_unstrip_status) | **GET** /v3/analyses/{analysis_id}/auto-unstrip/status | Get the auto-unstrip status for an analysis.
*AnalysesCoreApi* | [**v3_get_analysis_strings**](docs/AnalysesCoreApi.md#v3_get_analysis_strings) | **GET** /v3/analyses/{analysis_id}/functions/strings | List strings for an analysis.
*AnalysesCoreApi* | [**v3_get_analysis_strings_status**](docs/AnalysesCoreApi.md#v3_get_analysis_strings_status) | **GET** /v3/analyses/{analysis_id}/functions/strings/status | Get the string-extraction status for an analysis.
*AnalysesCoreApi* | [**v3_list_analyses**](docs/AnalysesCoreApi.md#v3_list_analyses) | **GET** /v3/analyses | List analyses
*AnalysesCoreApi* | [**v3_list_example_analyses**](docs/AnalysesCoreApi.md#v3_list_example_analyses) | **GET** /v3/analyses/examples | List example analyses
*BinariesApi* | [**get_binary_additional_details**](docs/BinariesApi.md#get_binary_additional_details) | **GET** /v3/binaries/{binary_id}/additional-details | Get additional details for a binary.
*BinariesApi* | [**get_binary_additional_details_status**](docs/BinariesApi.md#get_binary_additional_details_status) | **GET** /v3/binaries/{binary_id}/additional-details/status | Get the additional-details extraction status for a binary.
*CollectionsApi* | [**v3_create_collection**](docs/CollectionsApi.md#v3_create_collection) | **POST** /v3/collections | Create a collection.
*CollectionsApi* | [**v3_delete_collection**](docs/CollectionsApi.md#v3_delete_collection) | **DELETE** /v3/collections/{collection_id} | Delete a collection.
*CollectionsApi* | [**v3_get_collection**](docs/CollectionsApi.md#v3_get_collection) | **GET** /v3/collections/{collection_id} | Get a collection.
*CollectionsApi* | [**v3_list_collections**](docs/CollectionsApi.md#v3_list_collections) | **GET** /v3/collections | List collections.
*CollectionsApi* | [**v3_patch_collection**](docs/CollectionsApi.md#v3_patch_collection) | **PATCH** /v3/collections/{collection_id} | Update a collection.
*CollectionsApi* | [**v3_patch_collection_binaries**](docs/CollectionsApi.md#v3_patch_collection_binaries) | **PATCH** /v3/collections/{collection_id}/binaries | Replace the binaries in a collection.
*CollectionsApi* | [**v3_patch_collection_tags**](docs/CollectionsApi.md#v3_patch_collection_tags) | **PATCH** /v3/collections/{collection_id}/tags | Replace the tags on a collection.
*ConversationsApi* | [**cancel_run**](docs/ConversationsApi.md#cancel_run) | **POST** /v2/conversations/{id}/cancel | Cancel an active run
*ConversationsApi* | [**confirm_tool**](docs/ConversationsApi.md#confirm_tool) | **POST** /v2/conversations/{id}/confirm | Approve or reject a pending tool confirmation
*ConversationsApi* | [**create_conversation**](docs/ConversationsApi.md#create_conversation) | **POST** /v2/conversations | Create a new conversation
*ConversationsApi* | [**get_conversation**](docs/ConversationsApi.md#get_conversation) | **GET** /v2/conversations/{id} | Get a conversation with its events
*ConversationsApi* | [**list_conversations**](docs/ConversationsApi.md#list_conversations) | **GET** /v2/conversations | List conversations for the authenticated user
*ConversationsApi* | [**send_message**](docs/ConversationsApi.md#send_message) | **POST** /v2/conversations/{id}/messages | Send a message and start an agentic run
*ConversationsApi* | [**stream_events**](docs/ConversationsApi.md#stream_events) | **GET** /v2/conversations/{id}/events | Stream conversation events (SSE)
*FunctionsAIDecompilationApi* | [**create_ai_decompilation**](docs/FunctionsAIDecompilationApi.md#create_ai_decompilation) | **POST** /v3/functions/{function_id}/ai-decompilation | Start AI decompilation
*FunctionsAIDecompilationApi* | [**delete_ai_decompilation_inline_comment**](docs/FunctionsAIDecompilationApi.md#delete_ai_decompilation_inline_comment) | **DELETE** /v3/functions/{function_id}/ai-decompilation/inline-comments/{line} | Delete a single inline comment
*FunctionsAIDecompilationApi* | [**get_ai_decompilation**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation) | **GET** /v3/functions/{function_id}/ai-decompilation | Get AI decompilation result
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_inline_comments**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_inline_comments) | **GET** /v3/functions/{function_id}/ai-decompilation/inline-comments | Get AI decompilation inline comments
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_inline_comments_status**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_inline_comments_status) | **GET** /v3/functions/{function_id}/ai-decompilation/inline-comments/status | Get inline comments generation workflow status
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_status**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_status) | **GET** /v3/functions/{function_id}/ai-decompilation/status | Get AI decompilation workflow status
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_summary**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_summary) | **GET** /v3/functions/{function_id}/ai-decompilation/summary | Get AI decompilation summary
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_summary_status**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_summary_status) | **GET** /v3/functions/{function_id}/ai-decompilation/summary/status | Get summary generation workflow status
*FunctionsAIDecompilationApi* | [**get_ai_decompilation_tokenised**](docs/FunctionsAIDecompilationApi.md#get_ai_decompilation_tokenised) | **GET** /v3/functions/{function_id}/ai-decompilation/tokenised | Get tokenised AI decompilation with function mapping
*FunctionsAIDecompilationApi* | [**patch_ai_decompilation_inline_comment**](docs/FunctionsAIDecompilationApi.md#patch_ai_decompilation_inline_comment) | **PATCH** /v3/functions/{function_id}/ai-decompilation/inline-comments | Update a single inline comment
*FunctionsAIDecompilationApi* | [**regenerate_ai_decompilation_inline_comments**](docs/FunctionsAIDecompilationApi.md#regenerate_ai_decompilation_inline_comments) | **POST** /v3/functions/{function_id}/ai-decompilation/inline-comments | Regenerate AI decompilation inline comments
*FunctionsAIDecompilationApi* | [**regenerate_ai_decompilation_summary**](docs/FunctionsAIDecompilationApi.md#regenerate_ai_decompilation_summary) | **POST** /v3/functions/{function_id}/ai-decompilation/summary | Regenerate AI decompilation summary
*FunctionsAIDecompilationApi* | [**stream_ai_decompilation**](docs/FunctionsAIDecompilationApi.md#stream_ai_decompilation) | **GET** /v3/functions/{function_id}/ai-decompilation/events | Stream live AI decompilation output (SSE)
*FunctionsAIDecompilationApi* | [**upsert_ai_decompilation_overrides**](docs/FunctionsAIDecompilationApi.md#upsert_ai_decompilation_overrides) | **PATCH** /v3/functions/{function_id}/ai-decompilation/overrides | Upsert variable/function name overrides
*FunctionsCoreApi* | [**add_function_callee**](docs/FunctionsCoreApi.md#add_function_callee) | **POST** /v3/functions/{function_id}/callees | Add a callee to a function
*FunctionsCoreApi* | [**add_user_string_to_function**](docs/FunctionsCoreApi.md#add_user_string_to_function) | **POST** /v3/functions/{function_id}/user-provided-strings | Add a user-provided string to a function.
*FunctionsCoreApi* | [**get_function_blocks**](docs/FunctionsCoreApi.md#get_function_blocks) | **GET** /v3/functions/{function_id}/blocks | Get function disassembly
*FunctionsCoreApi* | [**get_function_callees_callers**](docs/FunctionsCoreApi.md#get_function_callees_callers) | **GET** /v3/functions/{function_id}/callees-callers | Get callees and callers for a function
*FunctionsCoreApi* | [**get_function_capabilities**](docs/FunctionsCoreApi.md#get_function_capabilities) | **GET** /v3/functions/{function_id}/capabilities | Get capabilities for a function
*FunctionsCoreApi* | [**get_function_details**](docs/FunctionsCoreApi.md#get_function_details) | **GET** /v3/functions/{function_id} | Get function details
*FunctionsCoreApi* | [**get_function_indirect_call_sites**](docs/FunctionsCoreApi.md#get_function_indirect_call_sites) | **GET** /v3/functions/{function_id}/indirect-call-sites | Get indirect call sites for a function
*FunctionsCoreApi* | [**get_function_strings**](docs/FunctionsCoreApi.md#get_function_strings) | **GET** /v3/functions/{function_id}/strings | List strings for a function.
*FunctionsCoreApi* | [**get_functions_callees_callers**](docs/FunctionsCoreApi.md#get_functions_callees_callers) | **GET** /v3/functions/callees-callers | Get callees and callers for many functions
*FunctionsCoreApi* | [**get_functions_matches**](docs/FunctionsCoreApi.md#get_functions_matches) | **GET** /v3/functions/matches | Get function-matching results for an explicit set of functions
*FunctionsCoreApi* | [**get_functions_matching_status**](docs/FunctionsCoreApi.md#get_functions_matching_status) | **GET** /v3/functions/matches/status | Get function-matching status for an explicit set of functions
*FunctionsCoreApi* | [**get_imported_function**](docs/FunctionsCoreApi.md#get_imported_function) | **GET** /v3/analyses/{analysis_id}/imported-functions/{imported_function_id} | Get an imported function with its callers
*FunctionsCoreApi* | [**list_analysis_functions**](docs/FunctionsCoreApi.md#list_analysis_functions) | **GET** /v3/analyses/{analysis_id}/functions | List functions in an analysis
*FunctionsCoreApi* | [**list_imported_functions**](docs/FunctionsCoreApi.md#list_imported_functions) | **GET** /v3/analyses/{analysis_id}/imported-functions | List imported functions in an analysis
*FunctionsCoreApi* | [**start_functions_matching**](docs/FunctionsCoreApi.md#start_functions_matching) | **POST** /v3/functions/matches | Start function matching for an explicit set of functions
*FunctionsCoreApi* | [**v3_canonicalize_function_names**](docs/FunctionsCoreApi.md#v3_canonicalize_function_names) | **POST** /v3/functions/canonical-names | Canonicalize a batch of function names
*FunctionsDataTypesApi* | [**batch_update_function_data_types**](docs/FunctionsDataTypesApi.md#batch_update_function_data_types) | **PUT** /v3/analyses/{analysis_id}/functions/data-types | Batch update function data types
*FunctionsDataTypesApi* | [**get_function_data_types**](docs/FunctionsDataTypesApi.md#get_function_data_types) | **GET** /v3/analyses/{analysis_id}/functions/{function_id}/data-types | Get data types for a single function
*FunctionsDataTypesApi* | [**list_analysis_functions_data_types**](docs/FunctionsDataTypesApi.md#list_analysis_functions_data_types) | **GET** /v3/analyses/{analysis_id}/functions/data-types | List data types for all functions in an analysis
*FunctionsDataTypesApi* | [**list_functions_data_types**](docs/FunctionsDataTypesApi.md#list_functions_data_types) | **GET** /v3/functions/data-types | Get data types for many functions
*FunctionsDataTypesApi* | [**update_function_data_types**](docs/FunctionsDataTypesApi.md#update_function_data_types) | **PUT** /v2/analyses/{analysis_id}/functions/{function_id}/data_types | Update function data types
*FunctionsRenamingHistoryApi* | [**batch_rename_functions**](docs/FunctionsRenamingHistoryApi.md#batch_rename_functions) | **POST** /v3/functions/rename | Batch rename functions
*FunctionsRenamingHistoryApi* | [**get_function_history**](docs/FunctionsRenamingHistoryApi.md#get_function_history) | **GET** /v3/functions/{function_id}/history | Get function name history
*FunctionsRenamingHistoryApi* | [**rename_function**](docs/FunctionsRenamingHistoryApi.md#rename_function) | **POST** /v3/functions/{function_id}/rename | Rename a function
*FunctionsRenamingHistoryApi* | [**revert_function_name**](docs/FunctionsRenamingHistoryApi.md#revert_function_name) | **POST** /v3/functions/{function_id}/history/{history_id}/revert | Revert function name
*IAMUsersApi* | [**get_me**](docs/IAMUsersApi.md#get_me) | **GET** /v2/iam/me | Get current user
*IAMUsersApi* | [**get_my_permissions**](docs/IAMUsersApi.md#get_my_permissions) | **GET** /v2/iam/me/permissions | Get current user permissions
*ReportsApi* | [**create_pdf_report**](docs/ReportsApi.md#create_pdf_report) | **POST** /v3/analyses/{analysis_id}/pdf | Start PDF report generation
*ReportsApi* | [**download_pdf_report**](docs/ReportsApi.md#download_pdf_report) | **GET** /v3/analyses/{analysis_id}/pdf | Download generated PDF report
*ReportsApi* | [**get_pdf_report_status**](docs/ReportsApi.md#get_pdf_report_status) | **GET** /v3/analyses/{analysis_id}/pdf/status | Get PDF report workflow status


## Documentation For Models

 - [AIDecompFunctionMapping](docs/AIDecompFunctionMapping.md)
 - [AIDecompInverseFunctionMapItem](docs/AIDecompInverseFunctionMapItem.md)
 - [AIDecompInverseStringMapItem](docs/AIDecompInverseStringMapItem.md)
 - [APIError](docs/APIError.md)
 - [AddCalleeInputBody](docs/AddCalleeInputBody.md)
 - [AddIssuerDomainInputBody](docs/AddIssuerDomainInputBody.md)
 - [AddOwnerInputBody](docs/AddOwnerInputBody.md)
 - [AddTeamMemberInputBody](docs/AddTeamMemberInputBody.md)
 - [AddUserStringInputBody](docs/AddUserStringInputBody.md)
 - [AddUserStringToFunctionInputBody](docs/AddUserStringToFunctionInputBody.md)
 - [AnalysisBasicInfoOutputBody](docs/AnalysisBasicInfoOutputBody.md)
 - [AnalysisFunctionEntry](docs/AnalysisFunctionEntry.md)
 - [AnalysisLogMessage](docs/AnalysisLogMessage.md)
 - [AnalysisLogs](docs/AnalysisLogs.md)
 - [AnalysisRecordBody](docs/AnalysisRecordBody.md)
 - [AnalysisReport](docs/AnalysisReport.md)
 - [AnalysisStringFunction](docs/AnalysisStringFunction.md)
 - [AnalysisStringItem](docs/AnalysisStringItem.md)
 - [AnalysisTagBody](docs/AnalysisTagBody.md)
 - [ApiCall](docs/ApiCall.md)
 - [ArchiveContentEntry](docs/ArchiveContentEntry.md)
 - [Artifact](docs/Artifact.md)
 - [AttemptFailedEvent](docs/AttemptFailedEvent.md)
 - [AttemptStartedEvent](docs/AttemptStartedEvent.md)
 - [AutoUnstripStatusOutputBody](docs/AutoUnstripStatusOutputBody.md)
 - [BatchBinaryMatchResult](docs/BatchBinaryMatchResult.md)
 - [BatchMatchingOutputBody](docs/BatchMatchingOutputBody.md)
 - [BatchRenameInputBody](docs/BatchRenameInputBody.md)
 - [BatchRenameItem](docs/BatchRenameItem.md)
 - [BatchRenameOutputBody](docs/BatchRenameOutputBody.md)
 - [BatchUpdateDataTypesInputBody](docs/BatchUpdateDataTypesInputBody.md)
 - [BatchUpdateDataTypesItem](docs/BatchUpdateDataTypesItem.md)
 - [BatchUpdateDataTypesOutputBody](docs/BatchUpdateDataTypesOutputBody.md)
 - [BatchUpdateDataTypesResult](docs/BatchUpdateDataTypesResult.md)
 - [Binary](docs/Binary.md)
 - [BulkCreateUserResult](docs/BulkCreateUserResult.md)
 - [BulkCreateUsersOutputBody](docs/BulkCreateUsersOutputBody.md)
 - [CallEdge](docs/CallEdge.md)
 - [CallEdgesOutputBody](docs/CallEdgesOutputBody.md)
 - [CanonicalName](docs/CanonicalName.md)
 - [CanonicalizeNamesInputBody](docs/CanonicalizeNamesInputBody.md)
 - [CanonicalizeNamesOutputBody](docs/CanonicalizeNamesOutputBody.md)
 - [CapabilitiesOutputBody](docs/CapabilitiesOutputBody.md)
 - [CapabilityEntry](docs/CapabilityEntry.md)
 - [CollectionListItemBody](docs/CollectionListItemBody.md)
 - [CommentsData](docs/CommentsData.md)
 - [ConfirmToolInputBody](docs/ConfirmToolInputBody.md)
 - [Connection](docs/Connection.md)
 - [ConsoleOutputEntry](docs/ConsoleOutputEntry.md)
 - [Conversation](docs/Conversation.md)
 - [ConversationContext](docs/ConversationContext.md)
 - [ConversationWithEvents](docs/ConversationWithEvents.md)
 - [CreateAIDecompOutputBody](docs/CreateAIDecompOutputBody.md)
 - [CreateCheckoutSessionInputBody](docs/CreateCheckoutSessionInputBody.md)
 - [CreateCollectionInputBody](docs/CreateCollectionInputBody.md)
 - [CreateCollectionOutputBody](docs/CreateCollectionOutputBody.md)
 - [CreateConversationRequest](docs/CreateConversationRequest.md)
 - [CreateGroupInputBody](docs/CreateGroupInputBody.md)
 - [CreateIdentityInputBody](docs/CreateIdentityInputBody.md)
 - [CreateIssuerInputBody](docs/CreateIssuerInputBody.md)
 - [CreateOrganisationInputBody](docs/CreateOrganisationInputBody.md)
 - [CreatePortalSessionInputBody](docs/CreatePortalSessionInputBody.md)
 - [CreateTeamInputBody](docs/CreateTeamInputBody.md)
 - [CreateUserInputBody](docs/CreateUserInputBody.md)
 - [DataTypesEntry](docs/DataTypesEntry.md)
 - [DecompFailedEvent](docs/DecompFailedEvent.md)
 - [DecompFinishedEvent](docs/DecompFinishedEvent.md)
 - [DecompilationData](docs/DecompilationData.md)
 - [DisassemblyOutputBody](docs/DisassemblyOutputBody.md)
 - [DnsQuery](docs/DnsQuery.md)
 - [DrakvufFileMetadata](docs/DrakvufFileMetadata.md)
 - [DynamicExecutionStatusResponse](docs/DynamicExecutionStatusResponse.md)
 - [ErrorBody](docs/ErrorBody.md)
 - [Event](docs/Event.md)
 - [EventAttemptFailed](docs/EventAttemptFailed.md)
 - [EventAttemptStarted](docs/EventAttemptStarted.md)
 - [EventCONTEXTCOMPACTED](docs/EventCONTEXTCOMPACTED.md)
 - [EventDecompFailed](docs/EventDecompFailed.md)
 - [EventDecompFinished](docs/EventDecompFinished.md)
 - [EventProse](docs/EventProse.md)
 - [EventRUNCANCELLED](docs/EventRUNCANCELLED.md)
 - [EventRUNERROR](docs/EventRUNERROR.md)
 - [EventRUNFINISHED](docs/EventRUNFINISHED.md)
 - [EventRUNSTARTED](docs/EventRUNSTARTED.md)
 - [EventRenameApplied](docs/EventRenameApplied.md)
 - [EventSTEPFINISHED](docs/EventSTEPFINISHED.md)
 - [EventSTEPSTARTED](docs/EventSTEPSTARTED.md)
 - [EventSourceDelta](docs/EventSourceDelta.md)
 - [EventSourceReset](docs/EventSourceReset.md)
 - [EventTEXTMESSAGECONTENT](docs/EventTEXTMESSAGECONTENT.md)
 - [EventTEXTMESSAGEEND](docs/EventTEXTMESSAGEEND.md)
 - [EventTEXTMESSAGESTART](docs/EventTEXTMESSAGESTART.md)
 - [EventTITLEUPDATED](docs/EventTITLEUPDATED.md)
 - [EventTOOLCALLARGSDELTA](docs/EventTOOLCALLARGSDELTA.md)
 - [EventTOOLCALLEND](docs/EventTOOLCALLEND.md)
 - [EventTOOLCALLPROGRESS](docs/EventTOOLCALLPROGRESS.md)
 - [EventTOOLCALLRESULT](docs/EventTOOLCALLRESULT.md)
 - [EventTOOLCALLSTART](docs/EventTOOLCALLSTART.md)
 - [EventTOOLCONFIRMATIONREQUIRED](docs/EventTOOLCONFIRMATIONREQUIRED.md)
 - [EventWarning](docs/EventWarning.md)
 - [Example](docs/Example.md)
 - [ExtractedURL](docs/ExtractedURL.md)
 - [FileActivityEntry](docs/FileActivityEntry.md)
 - [FormFile](docs/FormFile.md)
 - [FunctionArgument](docs/FunctionArgument.md)
 - [FunctionCallEdges](docs/FunctionCallEdges.md)
 - [FunctionDependency](docs/FunctionDependency.md)
 - [FunctionDetailsOutputBody](docs/FunctionDetailsOutputBody.md)
 - [FunctionHeader](docs/FunctionHeader.md)
 - [FunctionInfo](docs/FunctionInfo.md)
 - [FunctionMatch](docs/FunctionMatch.md)
 - [FunctionStackVariable](docs/FunctionStackVariable.md)
 - [FunctionStringItem](docs/FunctionStringItem.md)
 - [FunctionType](docs/FunctionType.md)
 - [GeneratePDFOutputBody](docs/GeneratePDFOutputBody.md)
 - [GetAdditionalDetailsOutputBody](docs/GetAdditionalDetailsOutputBody.md)
 - [GetAdditionalDetailsStatusOutputBody](docs/GetAdditionalDetailsStatusOutputBody.md)
 - [GetAnalysisStringsStatusOutputBody](docs/GetAnalysisStringsStatusOutputBody.md)
 - [GetCollectionOutputBody](docs/GetCollectionOutputBody.md)
 - [GetMatchesOutputBody](docs/GetMatchesOutputBody.md)
 - [GetMatchesStatusOutputBody](docs/GetMatchesStatusOutputBody.md)
 - [GetProductsOutputBody](docs/GetProductsOutputBody.md)
 - [GetSubscriptionOutputBody](docs/GetSubscriptionOutputBody.md)
 - [HistoryEntry](docs/HistoryEntry.md)
 - [HttpRequest](docs/HttpRequest.md)
 - [ImportedFunctionCallerEntry](docs/ImportedFunctionCallerEntry.md)
 - [ImportedFunctionDetailOutputBody](docs/ImportedFunctionDetailOutputBody.md)
 - [ImportedFunctionEntry](docs/ImportedFunctionEntry.md)
 - [IndirectCallSite](docs/IndirectCallSite.md)
 - [IndirectCallSitesOutputBody](docs/IndirectCallSitesOutputBody.md)
 - [InlineComment](docs/InlineComment.md)
 - [InviteUserInputBody](docs/InviteUserInputBody.md)
 - [IssuerAllowedDomain](docs/IssuerAllowedDomain.md)
 - [ListAnalysesOutputBody](docs/ListAnalysesOutputBody.md)
 - [ListAnalysisFunctionsDataTypesOutputBody](docs/ListAnalysisFunctionsDataTypesOutputBody.md)
 - [ListAnalysisFunctionsOutputBody](docs/ListAnalysisFunctionsOutputBody.md)
 - [ListAnalysisStringsOutputBody](docs/ListAnalysisStringsOutputBody.md)
 - [ListArchiveContentsOutputBody](docs/ListArchiveContentsOutputBody.md)
 - [ListCollectionsOutputBody](docs/ListCollectionsOutputBody.md)
 - [ListExampleAnalysesOutputBody](docs/ListExampleAnalysesOutputBody.md)
 - [ListFunctionStringsOutputBody](docs/ListFunctionStringsOutputBody.md)
 - [ListFunctionsDataTypesOutputBody](docs/ListFunctionsDataTypesOutputBody.md)
 - [ListImportedFunctionsOutputBody](docs/ListImportedFunctionsOutputBody.md)
 - [ListTeamsOutputBody](docs/ListTeamsOutputBody.md)
 - [ListUsersOutputBody](docs/ListUsersOutputBody.md)
 - [LocationOutputBody](docs/LocationOutputBody.md)
 - [MatchFilters](docs/MatchFilters.md)
 - [MatchedFunction](docs/MatchedFunction.md)
 - [MemdumpEntry](docs/MemdumpEntry.md)
 - [MessageBody](docs/MessageBody.md)
 - [ModuleLoadEntry](docs/ModuleLoadEntry.md)
 - [MutexEntry](docs/MutexEntry.md)
 - [NameConfidence](docs/NameConfidence.md)
 - [NetworkActivity](docs/NetworkActivity.md)
 - [OIDCCallbackInputBody](docs/OIDCCallbackInputBody.md)
 - [Organisation](docs/Organisation.md)
 - [OrganisationGroup](docs/OrganisationGroup.md)
 - [OrganisationIssuer](docs/OrganisationIssuer.md)
 - [OrganisationOwner](docs/OrganisationOwner.md)
 - [PasswordResetInputBody](docs/PasswordResetInputBody.md)
 - [PatchCollectionBinariesInputBody](docs/PatchCollectionBinariesInputBody.md)
 - [PatchCollectionBinariesOutputBody](docs/PatchCollectionBinariesOutputBody.md)
 - [PatchCollectionInputBody](docs/PatchCollectionInputBody.md)
 - [PatchCollectionOutputBody](docs/PatchCollectionOutputBody.md)
 - [PatchCollectionTagsInputBody](docs/PatchCollectionTagsInputBody.md)
 - [PatchCollectionTagsOutputBody](docs/PatchCollectionTagsOutputBody.md)
 - [PatchCommentBody](docs/PatchCommentBody.md)
 - [PcapBodyInfo](docs/PcapBodyInfo.md)
 - [Permissions](docs/Permissions.md)
 - [PriceOutput](docs/PriceOutput.md)
 - [PriceSummary](docs/PriceSummary.md)
 - [ProcessActivityEntry](docs/ProcessActivityEntry.md)
 - [ProcessMemdumps](docs/ProcessMemdumps.md)
 - [ProcessNode](docs/ProcessNode.md)
 - [ProcessTree](docs/ProcessTree.md)
 - [ProductOutput](docs/ProductOutput.md)
 - [ProductSummary](docs/ProductSummary.md)
 - [ProgressMessage](docs/ProgressMessage.md)
 - [ProseEvent](docs/ProseEvent.md)
 - [RefreshBody](docs/RefreshBody.md)
 - [RegenerateOutputBody](docs/RegenerateOutputBody.md)
 - [RegisterUserInputBody](docs/RegisterUserInputBody.md)
 - [RegistryOperation](docs/RegistryOperation.md)
 - [RenameAppliedEvent](docs/RenameAppliedEvent.md)
 - [RenameInputBody](docs/RenameInputBody.md)
 - [RenameOutputBody](docs/RenameOutputBody.md)
 - [ReplacementValue](docs/ReplacementValue.md)
 - [ReportEvent](docs/ReportEvent.md)
 - [ReportInfo](docs/ReportInfo.md)
 - [ReportOptions](docs/ReportOptions.md)
 - [RevokeBody](docs/RevokeBody.md)
 - [SSOProvider](docs/SSOProvider.md)
 - [SSOProvidersOutputBody](docs/SSOProvidersOutputBody.md)
 - [ScheduledTaskEntry](docs/ScheduledTaskEntry.md)
 - [SendMessageRequest](docs/SendMessageRequest.md)
 - [ServiceEntry](docs/ServiceEntry.md)
 - [SessionOutputBody](docs/SessionOutputBody.md)
 - [SourceDeltaEvent](docs/SourceDeltaEvent.md)
 - [SourceResetEvent](docs/SourceResetEvent.md)
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
 - [SseEventToolCallProgressData](docs/SseEventToolCallProgressData.md)
 - [SseEventToolCallResultData](docs/SseEventToolCallResultData.md)
 - [SseEventToolCallStartData](docs/SseEventToolCallStartData.md)
 - [SseEventToolConfirmationRequiredData](docs/SseEventToolConfirmationRequiredData.md)
 - [StartBatchMatchingInputBody](docs/StartBatchMatchingInputBody.md)
 - [StartMatchingForAnalysisInputBody](docs/StartMatchingForAnalysisInputBody.md)
 - [StartMatchingForFunctionsInputBody](docs/StartMatchingForFunctionsInputBody.md)
 - [StartMatchingOutputBody](docs/StartMatchingOutputBody.md)
 - [StartupInfo](docs/StartupInfo.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [StreamAiDecompilation200ResponseInner](docs/StreamAiDecompilation200ResponseInner.md)
 - [StreamEvents200ResponseInner](docs/StreamEvents200ResponseInner.md)
 - [SummaryData](docs/SummaryData.md)
 - [TcpCarvedFile](docs/TcpCarvedFile.md)
 - [Team](docs/Team.md)
 - [TeamMember](docs/TeamMember.md)
 - [TokenInputBody](docs/TokenInputBody.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [TokenisedData](docs/TokenisedData.md)
 - [TriggerDynamicExecutionInputBody](docs/TriggerDynamicExecutionInputBody.md)
 - [Ttp](docs/Ttp.md)
 - [UpdateDataTypesInputBody](docs/UpdateDataTypesInputBody.md)
 - [UpdateDataTypesOutputBody](docs/UpdateDataTypesOutputBody.md)
 - [UpdateIssuerInputBody](docs/UpdateIssuerInputBody.md)
 - [UpdateOrganisationInputBody](docs/UpdateOrganisationInputBody.md)
 - [UpdatePasswordInputBody](docs/UpdatePasswordInputBody.md)
 - [UpdateProfileInputBody](docs/UpdateProfileInputBody.md)
 - [UpdateTeamInputBody](docs/UpdateTeamInputBody.md)
 - [UpdateUserCreditsInputBody](docs/UpdateUserCreditsInputBody.md)
 - [UpdateUserInputBody](docs/UpdateUserInputBody.md)
 - [UpdateUserPasswordInputBody](docs/UpdateUserPasswordInputBody.md)
 - [UpsertOverridesData](docs/UpsertOverridesData.md)
 - [UpsertOverridesInputBody](docs/UpsertOverridesInputBody.md)
 - [User](docs/User.md)
 - [UserCredits](docs/UserCredits.md)
 - [UserIdentity](docs/UserIdentity.md)
 - [UserProfile](docs/UserProfile.md)
 - [WarningEvent](docs/WarningEvent.md)
 - [WorkflowProgress](docs/WorkflowProgress.md)
