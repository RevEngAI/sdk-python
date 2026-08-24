# CreateBitfieldDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.create_bitfield_data_type import CreateBitfieldDataType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBitfieldDataType from a JSON string
create_bitfield_data_type_instance = CreateBitfieldDataType.from_json(json)
# print the JSON string representation of the object
print(CreateBitfieldDataType.to_json())

# convert the object into a dict
create_bitfield_data_type_dict = create_bitfield_data_type_instance.to_dict()
# create an instance of CreateBitfieldDataType from a dict
create_bitfield_data_type_from_dict = CreateBitfieldDataType.from_dict(create_bitfield_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


