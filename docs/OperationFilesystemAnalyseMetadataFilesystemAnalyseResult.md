# OperationFilesystemAnalyseMetadataFilesystemAnalyseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**FilesystemAnalyseMetadata**](FilesystemAnalyseMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**FilesystemAnalyseResult**](FilesystemAnalyseResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_filesystem_analyse_metadata_filesystem_analyse_result import OperationFilesystemAnalyseMetadataFilesystemAnalyseResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationFilesystemAnalyseMetadataFilesystemAnalyseResult from a JSON string
operation_filesystem_analyse_metadata_filesystem_analyse_result_instance = OperationFilesystemAnalyseMetadataFilesystemAnalyseResult.from_json(json)
# print the JSON string representation of the object
print(OperationFilesystemAnalyseMetadataFilesystemAnalyseResult.to_json())

# convert the object into a dict
operation_filesystem_analyse_metadata_filesystem_analyse_result_dict = operation_filesystem_analyse_metadata_filesystem_analyse_result_instance.to_dict()
# create an instance of OperationFilesystemAnalyseMetadataFilesystemAnalyseResult from a dict
operation_filesystem_analyse_metadata_filesystem_analyse_result_from_dict = OperationFilesystemAnalyseMetadataFilesystemAnalyseResult.from_dict(operation_filesystem_analyse_metadata_filesystem_analyse_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


