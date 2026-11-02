# PatchInvestigationInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_type** | **str** | New case type. Omit to keep the existing one. | [optional] 
**name** | **str** | New name. Omit to keep the existing one. | [optional] 
**scope** | **str** | New scope. Omit to keep the existing one. | [optional] 
**severity** | **str** | New severity. Omit to keep the existing one. | [optional] 
**status** | **str** | New status. Omit to keep the existing one. | [optional] 

## Example

```python
from revengai.models.patch_investigation_input_body import PatchInvestigationInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInvestigationInputBody from a JSON string
patch_investigation_input_body_instance = PatchInvestigationInputBody.from_json(json)
# print the JSON string representation of the object
print(PatchInvestigationInputBody.to_json())

# convert the object into a dict
patch_investigation_input_body_dict = patch_investigation_input_body_instance.to_dict()
# create an instance of PatchInvestigationInputBody from a dict
patch_investigation_input_body_from_dict = PatchInvestigationInputBody.from_dict(patch_investigation_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


