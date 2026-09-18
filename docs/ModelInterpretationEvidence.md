# ModelInterpretationEvidence

LLM interpretations of observations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'model_interpretation']
**kind** | **str** |  | [optional] [default to 'model_interpretation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | [**EvidenceStrength**](EvidenceStrength.md) |  | [optional] 
**interpretations** | [**List[ModelInterpretation]**](ModelInterpretation.md) |  | 

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


