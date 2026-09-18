# OperationCreateMetadataCreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**CreateMetadata**](CreateMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**CreateResult**](CreateResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_create_metadata_create_result import OperationCreateMetadataCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCreateMetadataCreateResult from a JSON string
operation_create_metadata_create_result_instance = OperationCreateMetadataCreateResult.from_json(json)
# print the JSON string representation of the object
print(OperationCreateMetadataCreateResult.to_json())

# convert the object into a dict
operation_create_metadata_create_result_dict = operation_create_metadata_create_result_instance.to_dict()
# create an instance of OperationCreateMetadataCreateResult from a dict
operation_create_metadata_create_result_from_dict = OperationCreateMetadataCreateResult.from_dict(operation_create_metadata_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


