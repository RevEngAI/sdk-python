# HardcodedSecretEvidence

A hard-coded secret identified in the binary's data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'hardcoded_secret']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | **str** |  | [optional] [default to 'supports']
**strength** | [**EvidenceStrength**](EvidenceStrength.md) |  | 
**rule_id** | **str** |  | 
**description** | **str** |  | 
**secret_kind** | [**RuleKind**](RuleKind.md) |  | 
**secret** | **str** |  | 
**entropy** | **float** |  | 
**size** | **int** |  | 
**references** | **List[int]** |  | 

## Example

```python
from revengai.models.hardcoded_secret_evidence import HardcodedSecretEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of HardcodedSecretEvidence from a JSON string
hardcoded_secret_evidence_instance = HardcodedSecretEvidence.from_json(json)
# print the JSON string representation of the object
print(HardcodedSecretEvidence.to_json())

# convert the object into a dict
hardcoded_secret_evidence_dict = hardcoded_secret_evidence_instance.to_dict()
# create an instance of HardcodedSecretEvidence from a dict
hardcoded_secret_evidence_from_dict = HardcodedSecretEvidence.from_dict(hardcoded_secret_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


