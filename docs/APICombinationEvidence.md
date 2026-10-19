# APICombinationEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apis** | [**List[ReportImportedAPI]**](ReportImportedAPI.md) | The APIs in the combination. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

## Example

```python
from revengai.models.api_combination_evidence import APICombinationEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of APICombinationEvidence from a JSON string
api_combination_evidence_instance = APICombinationEvidence.from_json(json)
# print the JSON string representation of the object
print(APICombinationEvidence.to_json())

# convert the object into a dict
api_combination_evidence_dict = api_combination_evidence_instance.to_dict()
# create an instance of APICombinationEvidence from a dict
api_combination_evidence_from_dict = APICombinationEvidence.from_dict(api_combination_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


