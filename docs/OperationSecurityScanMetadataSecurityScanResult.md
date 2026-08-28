# OperationSecurityScanMetadataSecurityScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**SecurityScanMetadata**](SecurityScanMetadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**SecurityScanResult**](SecurityScanResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_security_scan_metadata_security_scan_result import OperationSecurityScanMetadataSecurityScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationSecurityScanMetadataSecurityScanResult from a JSON string
operation_security_scan_metadata_security_scan_result_instance = OperationSecurityScanMetadataSecurityScanResult.from_json(json)
# print the JSON string representation of the object
print(OperationSecurityScanMetadataSecurityScanResult.to_json())

# convert the object into a dict
operation_security_scan_metadata_security_scan_result_dict = operation_security_scan_metadata_security_scan_result_instance.to_dict()
# create an instance of OperationSecurityScanMetadataSecurityScanResult from a dict
operation_security_scan_metadata_security_scan_result_from_dict = OperationSecurityScanMetadataSecurityScanResult.from_dict(operation_security_scan_metadata_security_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


