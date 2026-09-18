# OperationExecutionExplainMetadataExecutionExplainResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**ExecutionExplainMetadata**](ExecutionExplainMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**ExecutionExplainResult**](ExecutionExplainResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_execution_explain_metadata_execution_explain_result import OperationExecutionExplainMetadataExecutionExplainResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationExecutionExplainMetadataExecutionExplainResult from a JSON string
operation_execution_explain_metadata_execution_explain_result_instance = OperationExecutionExplainMetadataExecutionExplainResult.from_json(json)
# print the JSON string representation of the object
print(OperationExecutionExplainMetadataExecutionExplainResult.to_json())

# convert the object into a dict
operation_execution_explain_metadata_execution_explain_result_dict = operation_execution_explain_metadata_execution_explain_result_instance.to_dict()
# create an instance of OperationExecutionExplainMetadataExecutionExplainResult from a dict
operation_execution_explain_metadata_execution_explain_result_from_dict = OperationExecutionExplainMetadataExecutionExplainResult.from_dict(operation_execution_explain_metadata_execution_explain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


