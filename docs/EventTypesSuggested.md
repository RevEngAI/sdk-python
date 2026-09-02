# EventTypesSuggested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TypesSuggestedEvent**](TypesSuggestedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_types_suggested import EventTypesSuggested

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypesSuggested from a JSON string
event_types_suggested_instance = EventTypesSuggested.from_json(json)
# print the JSON string representation of the object
print(EventTypesSuggested.to_json())

# convert the object into a dict
event_types_suggested_dict = event_types_suggested_instance.to_dict()
# create an instance of EventTypesSuggested from a dict
event_types_suggested_from_dict = EventTypesSuggested.from_dict(event_types_suggested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


