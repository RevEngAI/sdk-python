# EventSourceDelta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SourceDeltaEvent**](SourceDeltaEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_source_delta import EventSourceDelta

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourceDelta from a JSON string
event_source_delta_instance = EventSourceDelta.from_json(json)
# print the JSON string representation of the object
print(EventSourceDelta.to_json())

# convert the object into a dict
event_source_delta_dict = event_source_delta_instance.to_dict()
# create an instance of EventSourceDelta from a dict
event_source_delta_from_dict = EventSourceDelta.from_dict(event_source_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


