# DataTypeEnumValueEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Constant name. | 
**value** | **str** | Constant value, a decimal integer as a string, with no leading zeros. A string because the value may be negative or exceed 64 unsigned bits, which a JSON number cannot carry safely. | 

## Example

```python
from revengai.models.data_type_enum_value_entry import DataTypeEnumValueEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeEnumValueEntry from a JSON string
data_type_enum_value_entry_instance = DataTypeEnumValueEntry.from_json(json)
# print the JSON string representation of the object
print(DataTypeEnumValueEntry.to_json())

# convert the object into a dict
data_type_enum_value_entry_dict = data_type_enum_value_entry_instance.to_dict()
# create an instance of DataTypeEnumValueEntry from a dict
data_type_enum_value_entry_from_dict = DataTypeEnumValueEntry.from_dict(data_type_enum_value_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


