# EventRUNFINISHED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventRunFinishedData**](SseEventRunFinishedData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_runfinished import EventRUNFINISHED

# TODO update the JSON string below
json = "{}"
# create an instance of EventRUNFINISHED from a JSON string
event_runfinished_instance = EventRUNFINISHED.from_json(json)
# print the JSON string representation of the object
print(EventRUNFINISHED.to_json())

# convert the object into a dict
event_runfinished_dict = event_runfinished_instance.to_dict()
# create an instance of EventRUNFINISHED from a dict
event_runfinished_from_dict = EventRUNFINISHED.from_dict(event_runfinished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


