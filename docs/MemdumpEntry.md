# MemdumpEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**dump_reason** | **str** |  | 
**file_type** | **str** |  | [optional] 
**filename** | **str** |  | 
**index** | **int** |  | 
**is_pe** | **bool** |  | [optional] 
**method** | **str** |  | 
**mime_type** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**size** | **int** |  | 
**target_addr** | **str** |  | [optional] 
**target_process** | **int** |  | [optional] 

## Example

```python
from revengai.models.memdump_entry import MemdumpEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MemdumpEntry from a JSON string
memdump_entry_instance = MemdumpEntry.from_json(json)
# print the JSON string representation of the object
print(MemdumpEntry.to_json())

# convert the object into a dict
memdump_entry_dict = memdump_entry_instance.to_dict()
# create an instance of MemdumpEntry from a dict
memdump_entry_from_dict = MemdumpEntry.from_dict(memdump_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


