# V2FunctionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_change** | **str** |  | [optional] 
**addr** | **int** | Memory address of the function | 
**size** | **int** | Size of the function in bytes | 
**header** | [**V2FunctionHeader**](V2FunctionHeader.md) | Function header information | 
**stack_vars** | [**Dict[str, StackVariable]**](StackVariable.md) |  | [optional] 
**name** | **str** | Name of the function | 
**type** | **str** | Return type of the function | 
**artifact_type** | **str** | Type of artifact that the structure is associated with | [optional] [default to 'Function']

## Example

```python
from revengai.models.v2_function_type import V2FunctionType

# TODO update the JSON string below
json = "{}"
# create an instance of V2FunctionType from a JSON string
v2_function_type_instance = V2FunctionType.from_json(json)
# print the JSON string representation of the object
print(V2FunctionType.to_json())

# convert the object into a dict
v2_function_type_dict = v2_function_type_instance.to_dict()
# create an instance of V2FunctionType from a dict
v2_function_type_from_dict = V2FunctionType.from_dict(v2_function_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


