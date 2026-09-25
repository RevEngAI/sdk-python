# AnalysisXrefOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xref_from_list** | [**List[XrefFromBody]**](XrefFromBody.md) | Xrefs that originate at the queried vaddr, one per target address | 
**xref_to_list** | [**List[XrefIntoBody]**](XrefIntoBody.md) | Xrefs that target the queried vaddr, one per referencing address | 

## Example

```python
from revengai.models.analysis_xref_output_body import AnalysisXrefOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisXrefOutputBody from a JSON string
analysis_xref_output_body_instance = AnalysisXrefOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisXrefOutputBody.to_json())

# convert the object into a dict
analysis_xref_output_body_dict = analysis_xref_output_body_instance.to_dict()
# create an instance of AnalysisXrefOutputBody from a dict
analysis_xref_output_body_from_dict = AnalysisXrefOutputBody.from_dict(analysis_xref_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


