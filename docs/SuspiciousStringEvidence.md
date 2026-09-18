# SuspiciousStringEvidence

Suspicious strings without demonstrated semantic use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'suspicious_string']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'indirect']
**strings** | [**List[SuspiciousString]**](SuspiciousString.md) |  | 

## Example

```python
from revengai.models.suspicious_string_evidence import SuspiciousStringEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of SuspiciousStringEvidence from a JSON string
suspicious_string_evidence_instance = SuspiciousStringEvidence.from_json(json)
# print the JSON string representation of the object
print(SuspiciousStringEvidence.to_json())

# convert the object into a dict
suspicious_string_evidence_dict = suspicious_string_evidence_instance.to_dict()
# create an instance of SuspiciousStringEvidence from a dict
suspicious_string_evidence_from_dict = SuspiciousStringEvidence.from_dict(suspicious_string_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


