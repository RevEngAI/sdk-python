# EventTEXTMESSAGEEND


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventTextMessageEndData**](SseEventTextMessageEndData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_textmessageend import EventTEXTMESSAGEEND

# TODO update the JSON string below
json = "{}"
# create an instance of EventTEXTMESSAGEEND from a JSON string
event_textmessageend_instance = EventTEXTMESSAGEEND.from_json(json)
# print the JSON string representation of the object
print(EventTEXTMESSAGEEND.to_json())

# convert the object into a dict
event_textmessageend_dict = event_textmessageend_instance.to_dict()
# create an instance of EventTEXTMESSAGEEND from a dict
event_textmessageend_from_dict = EventTEXTMESSAGEEND.from_dict(event_textmessageend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


