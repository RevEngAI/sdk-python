# CreateStructDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**StructDefinition**](StructDefinition.md) |  | 
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.create_struct_data_type import CreateStructDataType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStructDataType from a JSON string
create_struct_data_type_instance = CreateStructDataType.from_json(json)
# print the JSON string representation of the object
print(CreateStructDataType.to_json())

# convert the object into a dict
create_struct_data_type_dict = create_struct_data_type_instance.to_dict()
# create an instance of CreateStructDataType from a dict
create_struct_data_type_from_dict = CreateStructDataType.from_dict(create_struct_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


