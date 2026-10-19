# FindingEvidenceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_chain** | **List[int]** | Addresses along the call chain. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 
**constants** | [**List[ReportReferencedConstant]**](ReportReferencedConstant.md) | The constants and where they are referenced. | 
**calls** | [**List[ImportedApiCall]**](ImportedApiCall.md) |  | 
**strings** | [**List[ReportStringMatch]**](ReportStringMatch.md) | The matched strings. | 
**similarities** | [**List[ReportFunctionSimilarity]**](ReportFunctionSimilarity.md) | The similar functions. | 
**apis** | [**List[ImportedApi]**](ImportedApi.md) |  | 
**summaries** | [**List[ReportCodeSummary]**](ReportCodeSummary.md) | Summaries of the decompiled code. | 
**interpretations** | [**List[ReportModelInterpretation]**](ReportModelInterpretation.md) | Interpretations of the code by an AI model. | 
**values** | [**List[ReportBytesConstant]**](ReportBytesConstant.md) | The well-known constants found in the binary. | 
**description** | **str** | What the rule detects. | 
**entropy** | **float** | Shannon entropy of the secret, in bits per byte. | 
**references** | **List[int]** | Address of the secret in the binary&#39;s data. | 
**rule_id** | **str** | Identifier of the secret-scanning rule that matched. | 
**secret** | **str** | The secret as it appears in the binary. | 
**secret_kind** | **str** | Category of the secret. | 
**size** | **int** | Size of the secret in bytes. | 

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


