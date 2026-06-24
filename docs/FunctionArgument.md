# FunctionArgument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_change** | **str** |  | [optional] 
**name** | **str** |  | 
**offset** | **int** |  | 
**scope** | **str** |  | [optional] 
**size** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.function_argument import FunctionArgument

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionArgument from a JSON string
function_argument_instance = FunctionArgument.from_json(json)
# print the JSON string representation of the object
print(FunctionArgument.to_json())

# convert the object into a dict
function_argument_dict = function_argument_instance.to_dict()
# create an instance of FunctionArgument from a dict
function_argument_from_dict = FunctionArgument.from_dict(function_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


