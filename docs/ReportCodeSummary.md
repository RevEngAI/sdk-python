# ReportCodeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reachability** | [**ReportCallChain**](ReportCallChain.md) | A call chain reaching the entity, absent when none was found. | [optional] 
**subject** | [**ReportSubject**](ReportSubject.md) | The program location whose code is summarised. | 
**summary** | **str** | What the code does. | 

## Example

```python
from revengai.models.report_code_summary import ReportCodeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCodeSummary from a JSON string
report_code_summary_instance = ReportCodeSummary.from_json(json)
# print the JSON string representation of the object
print(ReportCodeSummary.to_json())

# convert the object into a dict
report_code_summary_dict = report_code_summary_instance.to_dict()
# create an instance of ReportCodeSummary from a dict
report_code_summary_from_dict = ReportCodeSummary.from_dict(report_code_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


