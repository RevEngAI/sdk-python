# OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**DynamicExecutionSummaryMetadata**](DynamicExecutionSummaryMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | **object** |  | [optional] 

## Example

```python
from revengai.models.operation_dynamic_execution_summary_metadata_dynamic_execution_summary_result import OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult from a JSON string
operation_dynamic_execution_summary_metadata_dynamic_execution_summary_result_instance = OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult.from_json(json)
# print the JSON string representation of the object
print(OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult.to_json())

# convert the object into a dict
operation_dynamic_execution_summary_metadata_dynamic_execution_summary_result_dict = operation_dynamic_execution_summary_metadata_dynamic_execution_summary_result_instance.to_dict()
# create an instance of OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult from a dict
operation_dynamic_execution_summary_metadata_dynamic_execution_summary_result_from_dict = OperationDynamicExecutionSummaryMetadataDynamicExecutionSummaryResult.from_dict(operation_dynamic_execution_summary_metadata_dynamic_execution_summary_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


