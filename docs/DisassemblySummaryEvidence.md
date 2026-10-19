# DisassemblySummaryEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 
**summaries** | [**List[ReportCodeSummary]**](ReportCodeSummary.md) | Summaries of the disassembled code. | 

## Example

```python
from revengai.models.disassembly_summary_evidence import DisassemblySummaryEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of DisassemblySummaryEvidence from a JSON string
disassembly_summary_evidence_instance = DisassemblySummaryEvidence.from_json(json)
# print the JSON string representation of the object
print(DisassemblySummaryEvidence.to_json())

# convert the object into a dict
disassembly_summary_evidence_dict = disassembly_summary_evidence_instance.to_dict()
# create an instance of DisassemblySummaryEvidence from a dict
disassembly_summary_evidence_from_dict = DisassemblySummaryEvidence.from_dict(disassembly_summary_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


