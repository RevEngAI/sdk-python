# HistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_made_by** | **str** | Username of the user who made the change | 
**created_at** | **datetime** | When this name change was recorded | 
**function_name** | **str** | Function name at this point in history | 
**history_id** | **int** | History record ID | 
**is_debug** | **bool** | Whether the function had debug info | 
**mangled_name** | **str** | Mangled function name | [optional] 
**source_type** | **str** | Source of the rename (USER, SYSTEM, AI_UNSTRIP, etc.) | 

## Example

```python
from revengai.models.history_entry import HistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryEntry from a JSON string
history_entry_instance = HistoryEntry.from_json(json)
# print the JSON string representation of the object
print(HistoryEntry.to_json())

# convert the object into a dict
history_entry_dict = history_entry_instance.to_dict()
# create an instance of HistoryEntry from a dict
history_entry_from_dict = HistoryEntry.from_dict(history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


