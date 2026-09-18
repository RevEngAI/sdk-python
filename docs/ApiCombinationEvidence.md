# ApiCombinationEvidence

A known combination of APIs without a demonstrated semantic flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'api_combination']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'indirect']
**apis** | [**List[ImportedApi]**](ImportedApi.md) |  | 

## Example

```python
from revengai.models.api_combination_evidence import ApiCombinationEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCombinationEvidence from a JSON string
api_combination_evidence_instance = ApiCombinationEvidence.from_json(json)
# print the JSON string representation of the object
print(ApiCombinationEvidence.to_json())

# convert the object into a dict
api_combination_evidence_dict = api_combination_evidence_instance.to_dict()
# create an instance of ApiCombinationEvidence from a dict
api_combination_evidence_from_dict = ApiCombinationEvidence.from_dict(api_combination_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


