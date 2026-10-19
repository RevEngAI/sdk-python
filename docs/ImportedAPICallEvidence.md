# ImportedAPICallEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls** | [**List[ReportImportedAPICall]**](ReportImportedAPICall.md) | The observed calls. | 
**effect** | **str** | Whether the evidence supports or refutes the finding. | 
**evidence_kind** | **str** | Kind of evidence. | 
**kind** | **str** | How the evidence was derived. | 
**strength** | **str** | How directly the evidence bears on the finding. | 

## Example

```python
from revengai.models.imported_api_call_evidence import ImportedAPICallEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedAPICallEvidence from a JSON string
imported_api_call_evidence_instance = ImportedAPICallEvidence.from_json(json)
# print the JSON string representation of the object
print(ImportedAPICallEvidence.to_json())

# convert the object into a dict
imported_api_call_evidence_dict = imported_api_call_evidence_instance.to_dict()
# create an instance of ImportedAPICallEvidence from a dict
imported_api_call_evidence_from_dict = ImportedAPICallEvidence.from_dict(imported_api_call_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


