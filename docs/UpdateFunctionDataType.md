# UpdateFunctionDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | The type to replace, as returned by the data types list for this analysis. | 
**definition** | [**FunctionTypeDefinition**](FunctionTypeDefinition.md) |  | 
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.update_function_data_type import UpdateFunctionDataType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFunctionDataType from a JSON string
update_function_data_type_instance = UpdateFunctionDataType.from_json(json)
# print the JSON string representation of the object
print(UpdateFunctionDataType.to_json())

# convert the object into a dict
update_function_data_type_dict = update_function_data_type_instance.to_dict()
# create an instance of UpdateFunctionDataType from a dict
update_function_data_type_from_dict = UpdateFunctionDataType.from_dict(update_function_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


