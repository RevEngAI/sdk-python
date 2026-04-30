# EventTEXTMESSAGECONTENT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventTextMessageContentData**](SseEventTextMessageContentData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_textmessagecontent import EventTEXTMESSAGECONTENT

# TODO update the JSON string below
json = "{}"
# create an instance of EventTEXTMESSAGECONTENT from a JSON string
event_textmessagecontent_instance = EventTEXTMESSAGECONTENT.from_json(json)
# print the JSON string representation of the object
print(EventTEXTMESSAGECONTENT.to_json())

# convert the object into a dict
event_textmessagecontent_dict = event_textmessagecontent_instance.to_dict()
# create an instance of EventTEXTMESSAGECONTENT from a dict
event_textmessagecontent_from_dict = EventTEXTMESSAGECONTENT.from_dict(event_textmessagecontent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


