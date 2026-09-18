# OperationExecutionScanMetadataExecutionScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**ExecutionScanMetadata**](ExecutionScanMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**ExecutionScanResult**](ExecutionScanResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_execution_scan_metadata_execution_scan_result import OperationExecutionScanMetadataExecutionScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationExecutionScanMetadataExecutionScanResult from a JSON string
operation_execution_scan_metadata_execution_scan_result_instance = OperationExecutionScanMetadataExecutionScanResult.from_json(json)
# print the JSON string representation of the object
print(OperationExecutionScanMetadataExecutionScanResult.to_json())

# convert the object into a dict
operation_execution_scan_metadata_execution_scan_result_dict = operation_execution_scan_metadata_execution_scan_result_instance.to_dict()
# create an instance of OperationExecutionScanMetadataExecutionScanResult from a dict
operation_execution_scan_metadata_execution_scan_result_from_dict = OperationExecutionScanMetadataExecutionScanResult.from_dict(operation_execution_scan_metadata_execution_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


