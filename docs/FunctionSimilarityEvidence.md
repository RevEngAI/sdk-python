# FunctionSimilarityEvidence

Function-similarity results suggestive of a capability.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'function_similarity']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'indirect']
**similarities** | [**List[FunctionSimilarity]**](FunctionSimilarity.md) |  | 

## Example

```python
from revengai.models.function_similarity_evidence import FunctionSimilarityEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSimilarityEvidence from a JSON string
function_similarity_evidence_instance = FunctionSimilarityEvidence.from_json(json)
# print the JSON string representation of the object
print(FunctionSimilarityEvidence.to_json())

# convert the object into a dict
function_similarity_evidence_dict = function_similarity_evidence_instance.to_dict()
# create an instance of FunctionSimilarityEvidence from a dict
function_similarity_evidence_from_dict = FunctionSimilarityEvidence.from_dict(function_similarity_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


