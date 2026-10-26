# DecompilerSummaryEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 
**summaries** | [**List[ReportCodeSummary]**](ReportCodeSummary.md) | Summaries of the decompiled code. | 

## Example

```python
from revengai.models.decompiler_summary_evidence import DecompilerSummaryEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of DecompilerSummaryEvidence from a JSON string
decompiler_summary_evidence_instance = DecompilerSummaryEvidence.from_json(json)
# print the JSON string representation of the object
print(DecompilerSummaryEvidence.to_json())

# convert the object into a dict
decompiler_summary_evidence_dict = decompiler_summary_evidence_instance.to_dict()
# create an instance of DecompilerSummaryEvidence from a dict
decompiler_summary_evidence_from_dict = DecompilerSummaryEvidence.from_dict(decompiler_summary_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


