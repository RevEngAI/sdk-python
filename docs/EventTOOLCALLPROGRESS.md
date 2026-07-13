# EventTOOLCALLPROGRESS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventToolCallProgressData**](SseEventToolCallProgressData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_toolcallprogress import EventTOOLCALLPROGRESS

# TODO update the JSON string below
json = "{}"
# create an instance of EventTOOLCALLPROGRESS from a JSON string
event_toolcallprogress_instance = EventTOOLCALLPROGRESS.from_json(json)
# print the JSON string representation of the object
print(EventTOOLCALLPROGRESS.to_json())

# convert the object into a dict
event_toolcallprogress_dict = event_toolcallprogress_instance.to_dict()
# create an instance of EventTOOLCALLPROGRESS from a dict
event_toolcallprogress_from_dict = EventTOOLCALLPROGRESS.from_dict(event_toolcallprogress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


