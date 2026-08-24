# FunctionDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When this type was extracted. | 
**data_type_id** | **int** | Identifies the type within its analysis. 0 is a valid id. | 
**definition** | [**FunctionTypeDefinition**](FunctionTypeDefinition.md) | Absent only for a type referenced but never defined. | [optional] 
**has_definition** | **bool** | Whether this type carries a definition. False for the kinds that never have one and for a type referenced but never defined. | 
**kind** | **str** |  | 
**name** | **str** | Type name. | 
**namespace** | **str** | The scope qualifying the type name. Empty for a program-defined type. | 
**size** | **int** | Size in bytes, absent when it could not be determined. | [optional] 
**source_function_id** | **int** | The function this type was copied from, when transferred rather than extracted. | [optional] 
**source_type** | **str** | Where this type came from. | 

## Example

```python
from revengai.models.function_data_type import FunctionDataType

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDataType from a JSON string
function_data_type_instance = FunctionDataType.from_json(json)
# print the JSON string representation of the object
print(FunctionDataType.to_json())

# convert the object into a dict
function_data_type_dict = function_data_type_instance.to_dict()
# create an instance of FunctionDataType from a dict
function_data_type_from_dict = FunctionDataType.from_dict(function_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


