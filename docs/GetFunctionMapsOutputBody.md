# GetFunctionMapsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_map** | **Dict[str, int]** | Function ID (as a string key) to virtual address, for every function in the analysis&#39;s binary. | 
**inverse_function_map** | **Dict[str, int]** | Virtual address (as a string key) to function ID — the inverse of function_map. | 
**name_map** | **Dict[str, str]** | Virtual address (as a string key) to mangled function name. Empty string for a function with no mangled name. | 

## Example

```python
from revengai.models.get_function_maps_output_body import GetFunctionMapsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetFunctionMapsOutputBody from a JSON string
get_function_maps_output_body_instance = GetFunctionMapsOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetFunctionMapsOutputBody.to_json())

# convert the object into a dict
get_function_maps_output_body_dict = get_function_maps_output_body_instance.to_dict()
# create an instance of GetFunctionMapsOutputBody from a dict
get_function_maps_output_body_from_dict = GetFunctionMapsOutputBody.from_dict(get_function_maps_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


