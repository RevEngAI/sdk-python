# OperationBinaryExportMetadataBinaryExportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**BinaryExportMetadata**](BinaryExportMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**BinaryExportResult**](BinaryExportResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_binary_export_metadata_binary_export_result import OperationBinaryExportMetadataBinaryExportResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationBinaryExportMetadataBinaryExportResult from a JSON string
operation_binary_export_metadata_binary_export_result_instance = OperationBinaryExportMetadataBinaryExportResult.from_json(json)
# print the JSON string representation of the object
print(OperationBinaryExportMetadataBinaryExportResult.to_json())

# convert the object into a dict
operation_binary_export_metadata_binary_export_result_dict = operation_binary_export_metadata_binary_export_result_instance.to_dict()
# create an instance of OperationBinaryExportMetadataBinaryExportResult from a dict
operation_binary_export_metadata_binary_export_result_from_dict = OperationBinaryExportMetadataBinaryExportResult.from_dict(operation_binary_export_metadata_binary_export_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


