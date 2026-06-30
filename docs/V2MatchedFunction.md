# V2MatchedFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** | Unique identifier of the matched function | 
**binary_id** | **int** |  | 
**function_name** | **str** |  | 
**function_vaddr** | **int** |  | 
**mangled_name** | **str** |  | 
**debug** | **bool** |  | 
**binary_name** | **str** |  | 
**sha_256_hash** | **str** |  | 
**analysis_id** | **int** |  | 
**similarity** | **float** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from revengai.models.v2_matched_function import V2MatchedFunction

# TODO update the JSON string below
json = "{}"
# create an instance of V2MatchedFunction from a JSON string
v2_matched_function_instance = V2MatchedFunction.from_json(json)
# print the JSON string representation of the object
print(V2MatchedFunction.to_json())

# convert the object into a dict
v2_matched_function_dict = v2_matched_function_instance.to_dict()
# create an instance of V2MatchedFunction from a dict
v2_matched_function_from_dict = V2MatchedFunction.from_dict(v2_matched_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


