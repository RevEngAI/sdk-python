# ListCollectionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**page_number** | **int** |  | 
**page_size** | **int** |  | 
**results** | [**List[CollectionListItemBody]**](CollectionListItemBody.md) |  | 

## Example

```python
from revengai.models.list_collections_output_body import ListCollectionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollectionsOutputBody from a JSON string
list_collections_output_body_instance = ListCollectionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListCollectionsOutputBody.to_json())

# convert the object into a dict
list_collections_output_body_dict = list_collections_output_body_instance.to_dict()
# create an instance of ListCollectionsOutputBody from a dict
list_collections_output_body_from_dict = ListCollectionsOutputBody.from_dict(list_collections_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


