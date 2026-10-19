# CallChainEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_chain** | **List[int]** | Addresses along the call chain. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

## Example

```python
from revengai.models.call_chain_evidence import CallChainEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of CallChainEvidence from a JSON string
call_chain_evidence_instance = CallChainEvidence.from_json(json)
# print the JSON string representation of the object
print(CallChainEvidence.to_json())

# convert the object into a dict
call_chain_evidence_dict = call_chain_evidence_instance.to_dict()
# create an instance of CallChainEvidence from a dict
call_chain_evidence_from_dict = CallChainEvidence.from_dict(call_chain_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


