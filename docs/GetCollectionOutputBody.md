# GetCollectionOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | [**List[Binary]**](Binary.md) |  | [optional] 
**collection_id** | **int** |  | 
**collection_name** | **str** |  | 
**collection_scope** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**has_next_page** | **bool** |  | [optional] 
**model_id** | **int** |  | 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**team_id** | **int** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **int** |  | 

## Example

```python
from revengai.models.get_collection_output_body import GetCollectionOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollectionOutputBody from a JSON string
get_collection_output_body_instance = GetCollectionOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetCollectionOutputBody.to_json())

# convert the object into a dict
get_collection_output_body_dict = get_collection_output_body_instance.to_dict()
# create an instance of GetCollectionOutputBody from a dict
get_collection_output_body_from_dict = GetCollectionOutputBody.from_dict(get_collection_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


