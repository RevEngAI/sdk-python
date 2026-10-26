# ModelInterpretationEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**interpretations** | [**List[ReportModelInterpretation]**](ReportModelInterpretation.md) | Interpretations of the code by an AI model. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

## Example

```python
from revengai.models.model_interpretation_evidence import ModelInterpretationEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInterpretationEvidence from a JSON string
model_interpretation_evidence_instance = ModelInterpretationEvidence.from_json(json)
# print the JSON string representation of the object
print(ModelInterpretationEvidence.to_json())

# convert the object into a dict
model_interpretation_evidence_dict = model_interpretation_evidence_instance.to_dict()
# create an instance of ModelInterpretationEvidence from a dict
model_interpretation_evidence_from_dict = ModelInterpretationEvidence.from_dict(model_interpretation_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


