# EventSTEPFINISHED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventStepFinishedData**](SseEventStepFinishedData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_stepfinished import EventSTEPFINISHED

# TODO update the JSON string below
json = "{}"
# create an instance of EventSTEPFINISHED from a JSON string
event_stepfinished_instance = EventSTEPFINISHED.from_json(json)
# print the JSON string representation of the object
print(EventSTEPFINISHED.to_json())

# convert the object into a dict
event_stepfinished_dict = event_stepfinished_instance.to_dict()
# create an instance of EventSTEPFINISHED from a dict
event_stepfinished_from_dict = EventSTEPFINISHED.from_dict(event_stepfinished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


