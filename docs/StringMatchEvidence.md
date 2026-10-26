# StringMatchEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 
**strings** | [**List[ReportStringMatch]**](ReportStringMatch.md) | The matched strings. | 

## Example

```python
from revengai.models.string_match_evidence import StringMatchEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of StringMatchEvidence from a JSON string
string_match_evidence_instance = StringMatchEvidence.from_json(json)
# print the JSON string representation of the object
print(StringMatchEvidence.to_json())

# convert the object into a dict
string_match_evidence_dict = string_match_evidence_instance.to_dict()
# create an instance of StringMatchEvidence from a dict
string_match_evidence_from_dict = StringMatchEvidence.from_dict(string_match_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


