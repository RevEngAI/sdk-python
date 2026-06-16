# AIDecompFunctionMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **Dict[str, Dict[str, ReplacementValue]]** |  | 
**inverse_function_map** | [**Dict[str, AIDecompInverseFunctionMapItem]**](AIDecompInverseFunctionMapItem.md) |  | 
**inverse_string_map** | [**Dict[str, AIDecompInverseStringMapItem]**](AIDecompInverseStringMapItem.md) |  | 
**unmatched_custom_function_pointers** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_custom_types** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_enums** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_external_vars** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_functions** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_global_vars** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_go_to_labels** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_strings** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_variadic_lists** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**unmatched_vars** | [**Dict[str, ReplacementValue]**](ReplacementValue.md) |  | 
**user_override_mappings** | **Dict[str, str]** |  | 

## Example

```python
from revengai.models.ai_decomp_function_mapping import AIDecompFunctionMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AIDecompFunctionMapping from a JSON string
ai_decomp_function_mapping_instance = AIDecompFunctionMapping.from_json(json)
# print the JSON string representation of the object
print(AIDecompFunctionMapping.to_json())

# convert the object into a dict
ai_decomp_function_mapping_dict = ai_decomp_function_mapping_instance.to_dict()
# create an instance of AIDecompFunctionMapping from a dict
ai_decomp_function_mapping_from_dict = AIDecompFunctionMapping.from_dict(ai_decomp_function_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


