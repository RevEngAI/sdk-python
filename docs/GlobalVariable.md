# GlobalVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**d_type** | **str** | Name of the assigned data type. Only resolved on the function-scoped list. | [optional] 
**data_type_id** | **int** | Analysis data type, when one is assigned. | [optional] 
**indirect_target** | **int** | Address a pointer slot resolves to. | [optional] 
**is_bss** | **bool** | Whether the address falls in a zero-initialised section. | 
**name** | **str** | Recovered name, absent when nothing named the address. | [optional] 
**name_source** | **str** | What named it. | [optional] 
**size** | **int** | Size in bytes, when known. | [optional] 
**source_function_id** | **int** | Function a constructed static was initialised in. | [optional] 
**type_source** | **str** | What typed it. | [optional] 
**vaddr** | **int** | Virtual address the global lives at. | 
**value** | **str** | Decoded initial value, rendered for display. | [optional] 
**value_confidence** | **str** | How much to trust the decoded value. | [optional] 
**value_kind** | **str** | How the value was interpreted. | [optional] 
**value_source** | **str** | What produced the value. | [optional] 

## Example

```python
from revengai.models.global_variable import GlobalVariable

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalVariable from a JSON string
global_variable_instance = GlobalVariable.from_json(json)
# print the JSON string representation of the object
print(GlobalVariable.to_json())

# convert the object into a dict
global_variable_dict = global_variable_instance.to_dict()
# create an instance of GlobalVariable from a dict
global_variable_from_dict = GlobalVariable.from_dict(global_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


