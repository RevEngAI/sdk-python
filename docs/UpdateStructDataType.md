# UpdateStructDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | The type to replace, as returned by the data types list for this analysis. | 
**definition** | [**StructDefinition**](StructDefinition.md) |  | 
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.update_struct_data_type import UpdateStructDataType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStructDataType from a JSON string
update_struct_data_type_instance = UpdateStructDataType.from_json(json)
# print the JSON string representation of the object
print(UpdateStructDataType.to_json())

# convert the object into a dict
update_struct_data_type_dict = update_struct_data_type_instance.to_dict()
# create an instance of UpdateStructDataType from a dict
update_struct_data_type_from_dict = UpdateStructDataType.from_dict(update_struct_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


