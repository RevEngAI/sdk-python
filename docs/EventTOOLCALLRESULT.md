# EventTOOLCALLRESULT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventToolCallResultData**](SseEventToolCallResultData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_toolcallresult import EventTOOLCALLRESULT

# TODO update the JSON string below
json = "{}"
# create an instance of EventTOOLCALLRESULT from a JSON string
event_toolcallresult_instance = EventTOOLCALLRESULT.from_json(json)
# print the JSON string representation of the object
print(EventTOOLCALLRESULT.to_json())

# convert the object into a dict
event_toolcallresult_dict = event_toolcallresult_instance.to_dict()
# create an instance of EventTOOLCALLRESULT from a dict
event_toolcallresult_from_dict = EventTOOLCALLRESULT.from_dict(event_toolcallresult_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


