# PatchCollectionInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** | New collection name. Omit, null, or empty string to keep existing. | [optional] 
**collection_scope** | **str** | New scope (PUBLIC, PRIVATE, PROTECTED, TEAM). Omit or send null to keep existing. Empty string returns 422 UNPROCESSABLE ENTITY. | [optional] 
**description** | **str** | New description. Omit, null, or empty string to keep existing. | [optional] 

## Example

```python
from revengai.models.patch_collection_input_body import PatchCollectionInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCollectionInputBody from a JSON string
patch_collection_input_body_instance = PatchCollectionInputBody.from_json(json)
# print the JSON string representation of the object
print(PatchCollectionInputBody.to_json())

# convert the object into a dict
patch_collection_input_body_dict = patch_collection_input_body_instance.to_dict()
# create an instance of PatchCollectionInputBody from a dict
patch_collection_input_body_from_dict = PatchCollectionInputBody.from_dict(patch_collection_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


