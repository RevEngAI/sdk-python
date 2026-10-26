# ReportAPICombinationEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apis** | [**List[ReportImportedAPI]**](ReportImportedAPI.md) | The APIs in the combination. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

## Example

```python
from revengai.models.report_api_combination_evidence import ReportAPICombinationEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAPICombinationEvidence from a JSON string
report_api_combination_evidence_instance = ReportAPICombinationEvidence.from_json(json)
# print the JSON string representation of the object
print(ReportAPICombinationEvidence.to_json())

# convert the object into a dict
report_api_combination_evidence_dict = report_api_combination_evidence_instance.to_dict()
# create an instance of ReportAPICombinationEvidence from a dict
report_api_combination_evidence_from_dict = ReportAPICombinationEvidence.from_dict(report_api_combination_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


