# FunctionNameHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_made_by** | **str** | The user who made the change | 
**created_at** | **str** | The timestamp when the function name was created | 
**function_name** | **str** | The name of the function | 
**history_id** | **int** | The ID of the history record | 
**is_debug** | **bool** | Whether the function is debugged | 
**mangled_name** | **str** | The mangled name of the function | 
**source_type** | [**FunctionSourceType**](FunctionSourceType.md) | The source type of the function | 

## Example

```python
from revengai.models.function_name_history import FunctionNameHistory

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionNameHistory from a JSON string
function_name_history_instance = FunctionNameHistory.from_json(json)
# print the JSON string representation of the object
print(FunctionNameHistory.to_json())

# convert the object into a dict
function_name_history_dict = function_name_history_instance.to_dict()
# create an instance of FunctionNameHistory from a dict
function_name_history_from_dict = FunctionNameHistory.from_dict(function_name_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


