# OperationDynamicExecutionMetadataDynamicExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**DynamicExecutionMetadata**](DynamicExecutionMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | **object** |  | [optional] 

## Example

```python
from revengai.models.operation_dynamic_execution_metadata_dynamic_execution_result import OperationDynamicExecutionMetadataDynamicExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDynamicExecutionMetadataDynamicExecutionResult from a JSON string
operation_dynamic_execution_metadata_dynamic_execution_result_instance = OperationDynamicExecutionMetadataDynamicExecutionResult.from_json(json)
# print the JSON string representation of the object
print(OperationDynamicExecutionMetadataDynamicExecutionResult.to_json())

# convert the object into a dict
operation_dynamic_execution_metadata_dynamic_execution_result_dict = operation_dynamic_execution_metadata_dynamic_execution_result_instance.to_dict()
# create an instance of OperationDynamicExecutionMetadataDynamicExecutionResult from a dict
operation_dynamic_execution_metadata_dynamic_execution_result_from_dict = OperationDynamicExecutionMetadataDynamicExecutionResult.from_dict(operation_dynamic_execution_metadata_dynamic_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


