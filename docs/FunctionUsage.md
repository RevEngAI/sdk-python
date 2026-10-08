# FunctionUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** |  | 
**function_name** | **str** |  | 
**function_vaddr** | **int** |  | 
**ref_count** | **int** |  | 

## Example

```python
from revengai.models.function_usage import FunctionUsage

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionUsage from a JSON string
function_usage_instance = FunctionUsage.from_json(json)
# print the JSON string representation of the object
print(FunctionUsage.to_json())

# convert the object into a dict
function_usage_dict = function_usage_instance.to_dict()
# create an instance of FunctionUsage from a dict
function_usage_from_dict = FunctionUsage.from_dict(function_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


