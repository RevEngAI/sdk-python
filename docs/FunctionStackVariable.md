# FunctionStackVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **int** |  | 
**last_change** | **str** |  | [optional] 
**name** | **str** |  | 
**offset** | **int** |  | 
**scope** | **str** |  | [optional] 
**size** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.function_stack_variable import FunctionStackVariable

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionStackVariable from a JSON string
function_stack_variable_instance = FunctionStackVariable.from_json(json)
# print the JSON string representation of the object
print(FunctionStackVariable.to_json())

# convert the object into a dict
function_stack_variable_dict = function_stack_variable_instance.to_dict()
# create an instance of FunctionStackVariable from a dict
function_stack_variable_from_dict = FunctionStackVariable.from_dict(function_stack_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


