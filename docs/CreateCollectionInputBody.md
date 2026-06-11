# CreateCollectionInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | **List[int]** | Optional binary IDs to link to the collection. | [optional] 
**collection_name** | **str** | Collection name. | 
**collection_scope** | **str** | Visibility scope. | [default to 'PRIVATE']
**description** | **str** | Collection description. | 
**model_id** | **int** | Model ID the collection is associated with. | 
**tags** | **List[str]** | Optional tags to attach to the collection. | [optional] 

## Example

```python
from revengai.models.create_collection_input_body import CreateCollectionInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionInputBody from a JSON string
create_collection_input_body_instance = CreateCollectionInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionInputBody.to_json())

# convert the object into a dict
create_collection_input_body_dict = create_collection_input_body_instance.to_dict()
# create an instance of CreateCollectionInputBody from a dict
create_collection_input_body_from_dict = CreateCollectionInputBody.from_dict(create_collection_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


