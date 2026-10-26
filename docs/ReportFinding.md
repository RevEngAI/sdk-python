# ReportFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence** | [**List[ReportFindingEvidenceInner]**](ReportFindingEvidenceInner.md) | The evidence for or against the finding. | 
**property_id** | **str** | Identifier of the property the finding asserts. | 
**reachability** | **str** | Whether the code behind the finding is reachable from an entry point. | 

## Example

```python
from revengai.models.report_finding import ReportFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ReportFinding from a JSON string
report_finding_instance = ReportFinding.from_json(json)
# print the JSON string representation of the object
print(ReportFinding.to_json())

# convert the object into a dict
report_finding_dict = report_finding_instance.to_dict()
# create an instance of ReportFinding from a dict
report_finding_from_dict = ReportFinding.from_dict(report_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


