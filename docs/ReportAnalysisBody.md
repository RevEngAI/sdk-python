# ReportAnalysisBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **int** | REPORT_ANALYSIS agent tasks completed that day | 
**software_types** | [**SoftwareTypeCountsBody**](SoftwareTypeCountsBody.md) | Breakdown of completed reports by the software type the agent classified | 

## Example

```python
from revengai.models.report_analysis_body import ReportAnalysisBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAnalysisBody from a JSON string
report_analysis_body_instance = ReportAnalysisBody.from_json(json)
# print the JSON string representation of the object
print(ReportAnalysisBody.to_json())

# convert the object into a dict
report_analysis_body_dict = report_analysis_body_instance.to_dict()
# create an instance of ReportAnalysisBody from a dict
report_analysis_body_from_dict = ReportAnalysisBody.from_dict(report_analysis_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


