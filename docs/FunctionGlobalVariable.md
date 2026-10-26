# FunctionGlobalVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**d_type** | **str** | Name of the assigned data type. | [optional] 
**data_type_id** | **int** | Analysis data type, when one is assigned. | [optional] 
**decomp_lines** | **List[int]** | 1-indexed lines of the function&#39;s AI decompilation that reference the global. | 
**function_count** | **int** | How many functions&#39; AI decompilations reference the global. | 
**indirect_target** | **int** | Address a pointer slot resolves to. | [optional] 
**is_bss** | **bool** | Whether the address falls in a zero-initialised section. | 
**name** | **str** | Recovered name, absent when nothing named the address. | [optional] 
**name_source** | **str** | What named it. | [optional] 
**ref_count** | **int** | How many times the function&#39;s AI decompilation references the global. | 
**size** | **int** | Size in bytes, when known. | [optional] 
**source_function_id** | **int** | Function a constructed static was initialised in. | [optional] 
**total_ref_count** | **int** | How many times those AI decompilations reference the global, summed across functions. | 
**type_source** | **str** | What typed it. | [optional] 
**vaddr** | **int** | Virtual address the global lives at. | 
**value** | **str** | Decoded initial value, rendered for display. | [optional] 
**value_confidence** | **str** | How much to trust the decoded value. | [optional] 
**value_kind** | **str** | How the value was interpreted. | [optional] 
**value_source** | **str** | What produced the value. | [optional] 

## Example

```python
from revengai.models.function_global_variable import FunctionGlobalVariable

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionGlobalVariable from a JSON string
function_global_variable_instance = FunctionGlobalVariable.from_json(json)
# print the JSON string representation of the object
print(FunctionGlobalVariable.to_json())

# convert the object into a dict
function_global_variable_dict = function_global_variable_instance.to_dict()
# create an instance of FunctionGlobalVariable from a dict
function_global_variable_from_dict = FunctionGlobalVariable.from_dict(function_global_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


