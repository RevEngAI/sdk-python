# FunctionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_change** | **str** |  | [optional] 
**addr** | **int** | Memory address of the function | 
**size** | **int** | Size of the function in bytes | 
**header** | [**FunctionHeader**](FunctionHeader.md) | Function header information | 
**stack_vars** | [**Dict[str, StackVariable]**](StackVariable.md) |  | [optional] 
**name** | **str** | Name of the function | 
**type** | **str** | Return type of the function | 
**artifact_type** | **str** | Type of artifact that the structure is associated with | [optional] [default to 'Function']

## Example

```python
from revengai.models.function_type import FunctionType

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionType from a JSON string
function_type_instance = FunctionType.from_json(json)
# print the JSON string representation of the object
print(FunctionType.to_json())

# convert the object into a dict
function_type_dict = function_type_instance.to_dict()
# create an instance of FunctionType from a dict
function_type_from_dict = FunctionType.from_dict(function_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


