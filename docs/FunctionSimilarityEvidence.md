# FunctionSimilarityEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**similarities** | [**List[ReportFunctionSimilarity]**](ReportFunctionSimilarity.md) | The similar functions. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

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


