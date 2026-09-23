# FindingEvidenceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'hardcoded_secret']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | **str** |  | [default to 'supports']
**strength** | [**EvidenceStrength**](EvidenceStrength.md) |  | 
**call_chain** | **List[int]** |  | 
**constants** | [**List[ReferencedConstant]**](ReferencedConstant.md) |  | 
**calls** | [**List[ImportedApiCall]**](ImportedApiCall.md) |  | 
**strings** | [**List[StringMatch]**](StringMatch.md) |  | 
**similarities** | [**List[FunctionSimilarity]**](FunctionSimilarity.md) |  | 
**apis** | [**List[ImportedApi]**](ImportedApi.md) |  | 
**summaries** | [**List[DecompilerSummary]**](DecompilerSummary.md) |  | 
**interpretations** | [**List[ModelInterpretation]**](ModelInterpretation.md) |  | 
**values** | [**List[BytesConstant]**](BytesConstant.md) |  | 
**rule_id** | **str** |  | 
**description** | **str** |  | 
**secret_kind** | [**RuleKind**](RuleKind.md) |  | 
**secret** | **str** |  | 
**entropy** | **float** |  | 
**size** | **int** |  | 
**references** | **List[int]** |  | 

## Example

```python
from revengai.models.finding_evidence_inner import FindingEvidenceInner

# TODO update the JSON string below
json = "{}"
# create an instance of FindingEvidenceInner from a JSON string
finding_evidence_inner_instance = FindingEvidenceInner.from_json(json)
# print the JSON string representation of the object
print(FindingEvidenceInner.to_json())

# convert the object into a dict
finding_evidence_inner_dict = finding_evidence_inner_instance.to_dict()
# create an instance of FindingEvidenceInner from a dict
finding_evidence_inner_from_dict = FindingEvidenceInner.from_dict(finding_evidence_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


