# KnownConstantEvidence

A known constant whose semantic use has not been demonstrated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'known_constant']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'indirect']
**values** | [**List[BytesConstant]**](BytesConstant.md) |  | 

## Example

```python
from revengai.models.known_constant_evidence import KnownConstantEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of KnownConstantEvidence from a JSON string
known_constant_evidence_instance = KnownConstantEvidence.from_json(json)
# print the JSON string representation of the object
print(KnownConstantEvidence.to_json())

# convert the object into a dict
known_constant_evidence_dict = known_constant_evidence_instance.to_dict()
# create an instance of KnownConstantEvidence from a dict
known_constant_evidence_from_dict = KnownConstantEvidence.from_dict(known_constant_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


