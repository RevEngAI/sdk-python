# FunctionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **int** |  | 
**artifact_type** | **str** |  | [optional] 
**header** | [**FunctionHeader**](FunctionHeader.md) |  | 
**last_change** | **str** |  | [optional] 
**name** | **str** |  | 
**scope** | **str** |  | [optional] 
**size** | **int** |  | 
**stack_vars** | [**Dict[str, FunctionStackVariable]**](FunctionStackVariable.md) | Stack variables keyed by offset hex. | [optional] 
**type** | **str** |  | 

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


