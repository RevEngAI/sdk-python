# HardcodedSecretEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What the rule detects. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**entropy** | **float** | Shannon entropy of the secret, in bits per byte. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**references** | **List[int]** | Address of the secret in the binary&#39;s data. | 
**rule_id** | **str** | Identifier of the secret-scanning rule that matched. | 
**secret** | **str** | The secret as it appears in the binary. | 
**secret_kind** | **str** | Category of the secret. | 
**size** | **int** | Size of the secret in bytes. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

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


