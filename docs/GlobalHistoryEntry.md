# GlobalHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | [**GlobalVariable**](GlobalVariable.md) | The global as it stood before that edit. | 
**replaced_at** | **datetime** | When the value below was replaced. | 
**replaced_by_user_id** | **int** | Who replaced it. | 

## Example

```python
from revengai.models.global_history_entry import GlobalHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalHistoryEntry from a JSON string
global_history_entry_instance = GlobalHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(GlobalHistoryEntry.to_json())

# convert the object into a dict
global_history_entry_dict = global_history_entry_instance.to_dict()
# create an instance of GlobalHistoryEntry from a dict
global_history_entry_from_dict = GlobalHistoryEntry.from_dict(global_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


