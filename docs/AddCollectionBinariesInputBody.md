# AddCollectionBinariesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | **List[int]** | Binary IDs to add to the collection. Binary IDs already linked to the collection are ignored. | 

## Example

```python
from revengai.models.add_collection_binaries_input_body import AddCollectionBinariesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddCollectionBinariesInputBody from a JSON string
add_collection_binaries_input_body_instance = AddCollectionBinariesInputBody.from_json(json)
# print the JSON string representation of the object
print(AddCollectionBinariesInputBody.to_json())

# convert the object into a dict
add_collection_binaries_input_body_dict = add_collection_binaries_input_body_instance.to_dict()
# create an instance of AddCollectionBinariesInputBody from a dict
add_collection_binaries_input_body_from_dict = AddCollectionBinariesInputBody.from_dict(add_collection_binaries_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


