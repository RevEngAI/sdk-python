# OperationMetadataThreatReportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**ThreatReportResult**](ThreatReportResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_metadata_threat_report_result import OperationMetadataThreatReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationMetadataThreatReportResult from a JSON string
operation_metadata_threat_report_result_instance = OperationMetadataThreatReportResult.from_json(json)
# print the JSON string representation of the object
print(OperationMetadataThreatReportResult.to_json())

# convert the object into a dict
operation_metadata_threat_report_result_dict = operation_metadata_threat_report_result_instance.to_dict()
# create an instance of OperationMetadataThreatReportResult from a dict
operation_metadata_threat_report_result_from_dict = OperationMetadataThreatReportResult.from_dict(operation_metadata_threat_report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


