# PatchCollectionTagsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | Tags to set on the collection. The collection&#39;s tags are fully replaced with this list. | 

## Example

```python
from revengai.models.patch_collection_tags_input_body import PatchCollectionTagsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCollectionTagsInputBody from a JSON string
patch_collection_tags_input_body_instance = PatchCollectionTagsInputBody.from_json(json)
# print the JSON string representation of the object
print(PatchCollectionTagsInputBody.to_json())

# convert the object into a dict
patch_collection_tags_input_body_dict = patch_collection_tags_input_body_instance.to_dict()
# create an instance of PatchCollectionTagsInputBody from a dict
patch_collection_tags_input_body_from_dict = PatchCollectionTagsInputBody.from_dict(patch_collection_tags_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


