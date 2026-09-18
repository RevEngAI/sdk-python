# ReferencedConstantEvidence

Constants and the instructions that reference them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'referenced_constant']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'direct']
**constants** | [**List[ReferencedConstant]**](ReferencedConstant.md) |  | 

## Example

```python
from revengai.models.referenced_constant_evidence import ReferencedConstantEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedConstantEvidence from a JSON string
referenced_constant_evidence_instance = ReferencedConstantEvidence.from_json(json)
# print the JSON string representation of the object
print(ReferencedConstantEvidence.to_json())

# convert the object into a dict
referenced_constant_evidence_dict = referenced_constant_evidence_instance.to_dict()
# create an instance of ReferencedConstantEvidence from a dict
referenced_constant_evidence_from_dict = ReferencedConstantEvidence.from_dict(referenced_constant_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


