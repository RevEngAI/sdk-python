# CreateDataTypeEntry

A data type to create. `kind` selects the variant and so which definition the type must carry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**FunctionTypeDefinition**](FunctionTypeDefinition.md) |  | 
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.create_data_type_entry import CreateDataTypeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataTypeEntry from a JSON string
create_data_type_entry_instance = CreateDataTypeEntry.from_json(json)
# print the JSON string representation of the object
print(CreateDataTypeEntry.to_json())

# convert the object into a dict
create_data_type_entry_dict = create_data_type_entry_instance.to_dict()
# create an instance of CreateDataTypeEntry from a dict
create_data_type_entry_from_dict = CreateDataTypeEntry.from_dict(create_data_type_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


