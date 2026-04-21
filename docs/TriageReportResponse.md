# TriageReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_score** | **float** | Overall triage score for the software | 
**summary** | **str** | Summary of the triage analysis | 
**functions** | [**List[TriageFunctionResponse]**](TriageFunctionResponse.md) | List of triaged functions | 

## Example

```python
from revengai.models.triage_report_response import TriageReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriageReportResponse from a JSON string
triage_report_response_instance = TriageReportResponse.from_json(json)
# print the JSON string representation of the object
print(TriageReportResponse.to_json())

# convert the object into a dict
triage_report_response_dict = triage_report_response_instance.to_dict()
# create an instance of TriageReportResponse from a dict
triage_report_response_from_dict = TriageReportResponse.from_dict(triage_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


