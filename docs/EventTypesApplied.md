# EventTypesApplied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TypesAppliedEvent**](TypesAppliedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_types_applied import EventTypesApplied

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypesApplied from a JSON string
event_types_applied_instance = EventTypesApplied.from_json(json)
# print the JSON string representation of the object
print(EventTypesApplied.to_json())

# convert the object into a dict
event_types_applied_dict = event_types_applied_instance.to_dict()
# create an instance of EventTypesApplied from a dict
event_types_applied_from_dict = EventTypesApplied.from_dict(event_types_applied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


