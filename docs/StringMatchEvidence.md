# StringMatchEvidence

String matches without demonstrated semantic use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'string_match']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'indirect']
**strings** | [**List[StringMatch]**](StringMatch.md) |  | 

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


