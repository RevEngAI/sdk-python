# FunctionTypeDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[DataTypeFunctionParameterEntry]**](DataTypeFunctionParameterEntry.md) | The parameters, in argument order. | 
**return_data_type_id** | **int** | The return type. | [optional] 

## Example

```python
from revengai.models.function_type_definition import FunctionTypeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionTypeDefinition from a JSON string
function_type_definition_instance = FunctionTypeDefinition.from_json(json)
# print the JSON string representation of the object
print(FunctionTypeDefinition.to_json())

# convert the object into a dict
function_type_definition_dict = function_type_definition_instance.to_dict()
# create an instance of FunctionTypeDefinition from a dict
function_type_definition_from_dict = FunctionTypeDefinition.from_dict(function_type_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


