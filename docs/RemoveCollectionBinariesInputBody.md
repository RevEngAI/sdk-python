# RemoveCollectionBinariesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | **List[int]** | Binary IDs to remove from the collection. Binary IDs not linked to the collection are ignored. | 

## Example

```python
from revengai.models.remove_collection_binaries_input_body import RemoveCollectionBinariesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCollectionBinariesInputBody from a JSON string
remove_collection_binaries_input_body_instance = RemoveCollectionBinariesInputBody.from_json(json)
# print the JSON string representation of the object
print(RemoveCollectionBinariesInputBody.to_json())

# convert the object into a dict
remove_collection_binaries_input_body_dict = remove_collection_binaries_input_body_instance.to_dict()
# create an instance of RemoveCollectionBinariesInputBody from a dict
remove_collection_binaries_input_body_from_dict = RemoveCollectionBinariesInputBody.from_dict(remove_collection_binaries_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


