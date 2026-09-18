# OperationNetworkingExplainMetadataNetworkingExplainResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**NetworkingExplainMetadata**](NetworkingExplainMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**NetworkingExplainResult**](NetworkingExplainResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_networking_explain_metadata_networking_explain_result import OperationNetworkingExplainMetadataNetworkingExplainResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationNetworkingExplainMetadataNetworkingExplainResult from a JSON string
operation_networking_explain_metadata_networking_explain_result_instance = OperationNetworkingExplainMetadataNetworkingExplainResult.from_json(json)
# print the JSON string representation of the object
print(OperationNetworkingExplainMetadataNetworkingExplainResult.to_json())

# convert the object into a dict
operation_networking_explain_metadata_networking_explain_result_dict = operation_networking_explain_metadata_networking_explain_result_instance.to_dict()
# create an instance of OperationNetworkingExplainMetadataNetworkingExplainResult from a dict
operation_networking_explain_metadata_networking_explain_result_from_dict = OperationNetworkingExplainMetadataNetworkingExplainResult.from_dict(operation_networking_explain_metadata_networking_explain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


