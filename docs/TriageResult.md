# TriageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[TriageFunction]**](TriageFunction.md) | Per-function assessments. A function whose address no longer resolves within the analysis is omitted. | 
**software_score** | **float** | Maliciousness score for the binary, 0 to 1 | 
**summary** | **str** | Summary of the triage assessment | 

## Example

```python
from revengai.models.triage_result import TriageResult

# TODO update the JSON string below
json = "{}"
# create an instance of TriageResult from a JSON string
triage_result_instance = TriageResult.from_json(json)
# print the JSON string representation of the object
print(TriageResult.to_json())

# convert the object into a dict
triage_result_dict = triage_result_instance.to_dict()
# create an instance of TriageResult from a dict
triage_result_from_dict = TriageResult.from_dict(triage_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


