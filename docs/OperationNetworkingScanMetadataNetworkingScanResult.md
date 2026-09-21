# OperationNetworkingScanMetadataNetworkingScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**NetworkingScanMetadata**](NetworkingScanMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**NetworkingScanResult**](NetworkingScanResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_networking_scan_metadata_networking_scan_result import OperationNetworkingScanMetadataNetworkingScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationNetworkingScanMetadataNetworkingScanResult from a JSON string
operation_networking_scan_metadata_networking_scan_result_instance = OperationNetworkingScanMetadataNetworkingScanResult.from_json(json)
# print the JSON string representation of the object
print(OperationNetworkingScanMetadataNetworkingScanResult.to_json())

# convert the object into a dict
operation_networking_scan_metadata_networking_scan_result_dict = operation_networking_scan_metadata_networking_scan_result_instance.to_dict()
# create an instance of OperationNetworkingScanMetadataNetworkingScanResult from a dict
operation_networking_scan_metadata_networking_scan_result_from_dict = OperationNetworkingScanMetadataNetworkingScanResult.from_dict(operation_networking_scan_metadata_networking_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


