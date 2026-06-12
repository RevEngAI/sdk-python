# CollectionListItemBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** |  | 
**collection_name** | **str** |  | 
**collection_owner** | **str** |  | 
**collection_scope** | **str** |  | 
**collection_size** | **int** |  | 
**collection_tags** | **List[str]** |  | 
**creation** | **datetime** |  | 
**description** | **str** |  | 
**model_name** | **str** |  | 
**official_collection** | **bool** |  | 
**team_id** | **int** |  | 

## Example

```python
from revengai.models.collection_list_item_body import CollectionListItemBody

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionListItemBody from a JSON string
collection_list_item_body_instance = CollectionListItemBody.from_json(json)
# print the JSON string representation of the object
print(CollectionListItemBody.to_json())

# convert the object into a dict
collection_list_item_body_dict = collection_list_item_body_instance.to_dict()
# create an instance of CollectionListItemBody from a dict
collection_list_item_body_from_dict = CollectionListItemBody.from_dict(collection_list_item_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


