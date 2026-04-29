# EventRUNCANCELLED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventRunCancelledData**](SseEventRunCancelledData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_runcancelled import EventRUNCANCELLED

# TODO update the JSON string below
json = "{}"
# create an instance of EventRUNCANCELLED from a JSON string
event_runcancelled_instance = EventRUNCANCELLED.from_json(json)
# print the JSON string representation of the object
print(EventRUNCANCELLED.to_json())

# convert the object into a dict
event_runcancelled_dict = event_runcancelled_instance.to_dict()
# create an instance of EventRUNCANCELLED from a dict
event_runcancelled_from_dict = EventRUNCANCELLED.from_dict(event_runcancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


