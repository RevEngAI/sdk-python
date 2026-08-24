# DataTypeMemberEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_offset** | **int** | Bit offset from the start of the containing type, for bitfields. | [optional] 
**bit_size** | **int** | Width in bits, for bitfields. | [optional] 
**data_type_id** | **int** | The member&#39;s type. | [optional] 
**is_bitfield** | **bool** | Whether this member is a bitfield. | 
**name** | **str** | Member name, absent for unnamed padding. | [optional] 
**offset** | **int** | Byte offset from the start of the containing type. | 
**size** | **int** | Member size in bytes. | 

## Example

```python
from revengai.models.data_type_member_entry import DataTypeMemberEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeMemberEntry from a JSON string
data_type_member_entry_instance = DataTypeMemberEntry.from_json(json)
# print the JSON string representation of the object
print(DataTypeMemberEntry.to_json())

# convert the object into a dict
data_type_member_entry_dict = data_type_member_entry_instance.to_dict()
# create an instance of DataTypeMemberEntry from a dict
data_type_member_entry_from_dict = DataTypeMemberEntry.from_dict(data_type_member_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


