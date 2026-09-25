# FunctionSearchResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_name** | **str** |  | 
**created_at** | **datetime** |  | 
**function_id** | **int** |  | 
**function_name** | **str** |  | 
**model_id** | **int** |  | 
**model_name** | **str** |  | 
**owned_by** | **str** |  | 

## Example

```python
from revengai.models.function_search_result_body import FunctionSearchResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSearchResultBody from a JSON string
function_search_result_body_instance = FunctionSearchResultBody.from_json(json)
# print the JSON string representation of the object
print(FunctionSearchResultBody.to_json())

# convert the object into a dict
function_search_result_body_dict = function_search_result_body_instance.to_dict()
# create an instance of FunctionSearchResultBody from a dict
function_search_result_body_from_dict = FunctionSearchResultBody.from_dict(function_search_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


