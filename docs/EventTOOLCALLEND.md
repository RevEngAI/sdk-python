# EventTOOLCALLEND


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventToolCallEndData**](SseEventToolCallEndData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_toolcallend import EventTOOLCALLEND

# TODO update the JSON string below
json = "{}"
# create an instance of EventTOOLCALLEND from a JSON string
event_toolcallend_instance = EventTOOLCALLEND.from_json(json)
# print the JSON string representation of the object
print(EventTOOLCALLEND.to_json())

# convert the object into a dict
event_toolcallend_dict = event_toolcallend_instance.to_dict()
# create an instance of EventTOOLCALLEND from a dict
event_toolcallend_from_dict = EventTOOLCALLEND.from_dict(event_toolcallend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


