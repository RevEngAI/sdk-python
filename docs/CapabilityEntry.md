# CapabilityEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **str** |  | 
**description** | **str** |  | 
**function_id** | **int** |  | 
**function_name** | **str** |  | 
**type** | **str** |  | 
**vaddr** | **int** |  | 

## Example

```python
from revengai.models.capability_entry import CapabilityEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityEntry from a JSON string
capability_entry_instance = CapabilityEntry.from_json(json)
# print the JSON string representation of the object
print(CapabilityEntry.to_json())

# convert the object into a dict
capability_entry_dict = capability_entry_instance.to_dict()
# create an instance of CapabilityEntry from a dict
capability_entry_from_dict = CapabilityEntry.from_dict(capability_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


