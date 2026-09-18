# OperationMetadataReportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**ReportResult**](ReportResult.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_metadata_report_result import OperationMetadataReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationMetadataReportResult from a JSON string
operation_metadata_report_result_instance = OperationMetadataReportResult.from_json(json)
# print the JSON string representation of the object
print(OperationMetadataReportResult.to_json())

# convert the object into a dict
operation_metadata_report_result_dict = operation_metadata_report_result_instance.to_dict()
# create an instance of OperationMetadataReportResult from a dict
operation_metadata_report_result_from_dict = OperationMetadataReportResult.from_dict(operation_metadata_report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


