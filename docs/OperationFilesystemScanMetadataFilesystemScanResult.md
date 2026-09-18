# OperationFilesystemScanMetadataFilesystemScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**FilesystemScanMetadata**](FilesystemScanMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**FilesystemScanResult**](FilesystemScanResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_filesystem_scan_metadata_filesystem_scan_result import OperationFilesystemScanMetadataFilesystemScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationFilesystemScanMetadataFilesystemScanResult from a JSON string
operation_filesystem_scan_metadata_filesystem_scan_result_instance = OperationFilesystemScanMetadataFilesystemScanResult.from_json(json)
# print the JSON string representation of the object
print(OperationFilesystemScanMetadataFilesystemScanResult.to_json())

# convert the object into a dict
operation_filesystem_scan_metadata_filesystem_scan_result_dict = operation_filesystem_scan_metadata_filesystem_scan_result_instance.to_dict()
# create an instance of OperationFilesystemScanMetadataFilesystemScanResult from a dict
operation_filesystem_scan_metadata_filesystem_scan_result_from_dict = OperationFilesystemScanMetadataFilesystemScanResult.from_dict(operation_filesystem_scan_metadata_filesystem_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


