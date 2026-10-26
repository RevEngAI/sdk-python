# OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**RenameUnnamedFunctionsMetadata**](RenameUnnamedFunctionsMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**RenameUnnamedFunctionsResult**](RenameUnnamedFunctionsResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_rename_unnamed_functions_metadata_rename_unnamed_functions_result import OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult from a JSON string
operation_rename_unnamed_functions_metadata_rename_unnamed_functions_result_instance = OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult.from_json(json)
# print the JSON string representation of the object
print(OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult.to_json())

# convert the object into a dict
operation_rename_unnamed_functions_metadata_rename_unnamed_functions_result_dict = operation_rename_unnamed_functions_metadata_rename_unnamed_functions_result_instance.to_dict()
# create an instance of OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult from a dict
operation_rename_unnamed_functions_metadata_rename_unnamed_functions_result_from_dict = OperationRenameUnnamedFunctionsMetadataRenameUnnamedFunctionsResult.from_dict(operation_rename_unnamed_functions_metadata_rename_unnamed_functions_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


