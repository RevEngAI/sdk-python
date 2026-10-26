# ReferencedConstantEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constants** | [**List[ReportReferencedConstant]**](ReportReferencedConstant.md) | The constants and where they are referenced. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

## Example

```python
from revengai.models.referenced_constant_evidence import ReferencedConstantEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedConstantEvidence from a JSON string
referenced_constant_evidence_instance = ReferencedConstantEvidence.from_json(json)
# print the JSON string representation of the object
print(ReferencedConstantEvidence.to_json())

# convert the object into a dict
referenced_constant_evidence_dict = referenced_constant_evidence_instance.to_dict()
# create an instance of ReferencedConstantEvidence from a dict
referenced_constant_evidence_from_dict = ReferencedConstantEvidence.from_dict(referenced_constant_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


