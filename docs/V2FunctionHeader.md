# V2FunctionHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_change** | **str** |  | [optional] 
**name** | **str** | Name of the function | 
**addr** | **int** | Memory address of the function | 
**type** | **str** | Return type of the function | 
**args** | [**Dict[str, Argument]**](Argument.md) | Dictionary of function arguments | 

## Example

```python
from revengai.models.v2_function_header import V2FunctionHeader

# TODO update the JSON string below
json = "{}"
# create an instance of V2FunctionHeader from a JSON string
v2_function_header_instance = V2FunctionHeader.from_json(json)
# print the JSON string representation of the object
print(V2FunctionHeader.to_json())

# convert the object into a dict
v2_function_header_dict = v2_function_header_instance.to_dict()
# create an instance of V2FunctionHeader from a dict
v2_function_header_from_dict = V2FunctionHeader.from_dict(v2_function_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


