# PatchCollectionBinariesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | **List[int]** | Binary IDs to set on the collection. The collection&#39;s binaries are fully replaced with this list. | 

## Example

```python
from revengai.models.patch_collection_binaries_input_body import PatchCollectionBinariesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCollectionBinariesInputBody from a JSON string
patch_collection_binaries_input_body_instance = PatchCollectionBinariesInputBody.from_json(json)
# print the JSON string representation of the object
print(PatchCollectionBinariesInputBody.to_json())

# convert the object into a dict
patch_collection_binaries_input_body_dict = patch_collection_binaries_input_body_instance.to_dict()
# create an instance of PatchCollectionBinariesInputBody from a dict
patch_collection_binaries_input_body_from_dict = PatchCollectionBinariesInputBody.from_dict(patch_collection_binaries_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


