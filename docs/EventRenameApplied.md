# EventRenameApplied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RenameAppliedEvent**](RenameAppliedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_rename_applied import EventRenameApplied

# TODO update the JSON string below
json = "{}"
# create an instance of EventRenameApplied from a JSON string
event_rename_applied_instance = EventRenameApplied.from_json(json)
# print the JSON string representation of the object
print(EventRenameApplied.to_json())

# convert the object into a dict
event_rename_applied_dict = event_rename_applied_instance.to_dict()
# create an instance of EventRenameApplied from a dict
event_rename_applied_from_dict = EventRenameApplied.from_dict(event_rename_applied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


