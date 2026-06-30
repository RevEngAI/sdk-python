# V2FunctionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**func_types** | [**V2FunctionType**](V2FunctionType.md) |  | [optional] 
**func_deps** | [**List[V2FunctionInfoFuncDepsInner]**](V2FunctionInfoFuncDepsInner.md) | List of function dependencies | 

## Example

```python
from revengai.models.v2_function_info import V2FunctionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2FunctionInfo from a JSON string
v2_function_info_instance = V2FunctionInfo.from_json(json)
# print the JSON string representation of the object
print(V2FunctionInfo.to_json())

# convert the object into a dict
v2_function_info_dict = v2_function_info_instance.to_dict()
# create an instance of V2FunctionInfo from a dict
v2_function_info_from_dict = V2FunctionInfo.from_dict(v2_function_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


