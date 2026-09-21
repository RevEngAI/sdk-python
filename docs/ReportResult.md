# ReportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**findings** | **object** |  | 
**meta** | **object** |  | 

## Example

```python
from revengai.models.report_result import ReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResult from a JSON string
report_result_instance = ReportResult.from_json(json)
# print the JSON string representation of the object
print(ReportResult.to_json())

# convert the object into a dict
report_result_dict = report_result_instance.to_dict()
# create an instance of ReportResult from a dict
report_result_from_dict = ReportResult.from_dict(report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


