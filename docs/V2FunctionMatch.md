# V2FunctionMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** | Unique identifier of the function | 
**matched_functions** | [**List[V2MatchedFunction]**](V2MatchedFunction.md) |  | 
**confidences** | [**List[V2NameConfidence]**](V2NameConfidence.md) |  | [optional] 

## Example

```python
from revengai.models.v2_function_match import V2FunctionMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V2FunctionMatch from a JSON string
v2_function_match_instance = V2FunctionMatch.from_json(json)
# print the JSON string representation of the object
print(V2FunctionMatch.to_json())

# convert the object into a dict
v2_function_match_dict = v2_function_match_instance.to_dict()
# create an instance of V2FunctionMatch from a dict
v2_function_match_from_dict = V2FunctionMatch.from_dict(v2_function_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


