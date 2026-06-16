# PatchCollectionOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_count** | **int** |  | 
**collection_id** | **int** |  | 
**collection_name** | **str** |  | 
**collection_scope** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**model_id** | **int** |  | 
**team_id** | **int** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **int** |  | 

## Example

```python
from revengai.models.patch_collection_output_body import PatchCollectionOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCollectionOutputBody from a JSON string
patch_collection_output_body_instance = PatchCollectionOutputBody.from_json(json)
# print the JSON string representation of the object
print(PatchCollectionOutputBody.to_json())

# convert the object into a dict
patch_collection_output_body_dict = patch_collection_output_body_instance.to_dict()
# create an instance of PatchCollectionOutputBody from a dict
patch_collection_output_body_from_dict = PatchCollectionOutputBody.from_dict(patch_collection_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


