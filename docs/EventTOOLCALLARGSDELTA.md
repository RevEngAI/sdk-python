# EventTOOLCALLARGSDELTA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventToolCallArgsDeltaData**](SseEventToolCallArgsDeltaData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_toolcallargsdelta import EventTOOLCALLARGSDELTA

# TODO update the JSON string below
json = "{}"
# create an instance of EventTOOLCALLARGSDELTA from a JSON string
event_toolcallargsdelta_instance = EventTOOLCALLARGSDELTA.from_json(json)
# print the JSON string representation of the object
print(EventTOOLCALLARGSDELTA.to_json())

# convert the object into a dict
event_toolcallargsdelta_dict = event_toolcallargsdelta_instance.to_dict()
# create an instance of EventTOOLCALLARGSDELTA from a dict
event_toolcallargsdelta_from_dict = EventTOOLCALLARGSDELTA.from_dict(event_toolcallargsdelta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


