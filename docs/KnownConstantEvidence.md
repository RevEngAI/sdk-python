# KnownConstantEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 
**values** | [**List[ReportBytesConstant]**](ReportBytesConstant.md) | The well-known constants found in the binary. | 

## Example

```python
from revengai.models.known_constant_evidence import KnownConstantEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of KnownConstantEvidence from a JSON string
known_constant_evidence_instance = KnownConstantEvidence.from_json(json)
# print the JSON string representation of the object
print(KnownConstantEvidence.to_json())

# convert the object into a dict
known_constant_evidence_dict = known_constant_evidence_instance.to_dict()
# create an instance of KnownConstantEvidence from a dict
known_constant_evidence_from_dict = KnownConstantEvidence.from_dict(known_constant_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


