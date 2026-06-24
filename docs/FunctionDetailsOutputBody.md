# FunctionDetailsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_id** | **int** |  | 
**creation** | **datetime** |  | 
**debug** | **bool** |  | 
**function_id** | **int** |  | 
**function_name** | **str** |  | 
**function_size** | **int** |  | 
**function_vaddr** | **int** |  | 
**mangled_name** | **str** |  | [optional] 
**source_function_id** | **int** |  | [optional] 

## Example

```python
from revengai.models.function_details_output_body import FunctionDetailsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDetailsOutputBody from a JSON string
function_details_output_body_instance = FunctionDetailsOutputBody.from_json(json)
# print the JSON string representation of the object
print(FunctionDetailsOutputBody.to_json())

# convert the object into a dict
function_details_output_body_dict = function_details_output_body_instance.to_dict()
# create an instance of FunctionDetailsOutputBody from a dict
function_details_output_body_from_dict = FunctionDetailsOutputBody.from_dict(function_details_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


