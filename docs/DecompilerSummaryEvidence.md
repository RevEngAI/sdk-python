# DecompilerSummaryEvidence

Semantic summaries derived from decompiler output.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'decompiler_summary']
**kind** | **str** |  | [optional] [default to 'model_interpretation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'indirect']
**summaries** | [**List[DecompilerSummary]**](DecompilerSummary.md) |  | 

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


