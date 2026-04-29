# EventRUNSTARTED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventRunStartedData**](SseEventRunStartedData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_runstarted import EventRUNSTARTED

# TODO update the JSON string below
json = "{}"
# create an instance of EventRUNSTARTED from a JSON string
event_runstarted_instance = EventRUNSTARTED.from_json(json)
# print the JSON string representation of the object
print(EventRUNSTARTED.to_json())

# convert the object into a dict
event_runstarted_dict = event_runstarted_instance.to_dict()
# create an instance of EventRUNSTARTED from a dict
event_runstarted_from_dict = EventRUNSTARTED.from_dict(event_runstarted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


