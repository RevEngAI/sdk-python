# ImportedApiCallEvidence

Imported API calls observed in the program.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_kind** | **str** |  | [optional] [default to 'imported_api_call']
**kind** | **str** |  | [optional] [default to 'deterministic_derivation']
**effect** | [**EvidenceEffect**](EvidenceEffect.md) |  | 
**strength** | **str** |  | [optional] [default to 'direct']
**calls** | [**List[ImportedApiCall]**](ImportedApiCall.md) |  | 

## Example

```python
from revengai.models.imported_api_call_evidence import ImportedApiCallEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedApiCallEvidence from a JSON string
imported_api_call_evidence_instance = ImportedApiCallEvidence.from_json(json)
# print the JSON string representation of the object
print(ImportedApiCallEvidence.to_json())

# convert the object into a dict
imported_api_call_evidence_dict = imported_api_call_evidence_instance.to_dict()
# create an instance of ImportedApiCallEvidence from a dict
imported_api_call_evidence_from_dict = ImportedApiCallEvidence.from_dict(imported_api_call_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


