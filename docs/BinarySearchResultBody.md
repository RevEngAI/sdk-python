# BinarySearchResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | 
**binary_id** | **int** |  | 
**binary_name** | **str** |  | 
**created_at** | **datetime** |  | 
**model_id** | **int** |  | 
**model_name** | **str** |  | 
**owned_by** | **str** |  | 
**sha_256_hash** | **str** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from revengai.models.binary_search_result_body import BinarySearchResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of BinarySearchResultBody from a JSON string
binary_search_result_body_instance = BinarySearchResultBody.from_json(json)
# print the JSON string representation of the object
print(BinarySearchResultBody.to_json())

# convert the object into a dict
binary_search_result_body_dict = binary_search_result_body_instance.to_dict()
# create an instance of BinarySearchResultBody from a dict
binary_search_result_body_from_dict = BinarySearchResultBody.from_dict(binary_search_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


