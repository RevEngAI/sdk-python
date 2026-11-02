# EventAGENTRUNUPDATE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventAgentRunUpdateData**](SseEventAgentRunUpdateData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_agentrunupdate import EventAGENTRUNUPDATE

# TODO update the JSON string below
json = "{}"
# create an instance of EventAGENTRUNUPDATE from a JSON string
event_agentrunupdate_instance = EventAGENTRUNUPDATE.from_json(json)
# print the JSON string representation of the object
print(EventAGENTRUNUPDATE.to_json())

# convert the object into a dict
event_agentrunupdate_dict = event_agentrunupdate_instance.to_dict()
# create an instance of EventAGENTRUNUPDATE from a dict
event_agentrunupdate_from_dict = EventAGENTRUNUPDATE.from_dict(event_agentrunupdate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


