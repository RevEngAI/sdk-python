# EventRUNERROR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventRunErrorData**](SseEventRunErrorData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_runerror import EventRUNERROR

# TODO update the JSON string below
json = "{}"
# create an instance of EventRUNERROR from a JSON string
event_runerror_instance = EventRUNERROR.from_json(json)
# print the JSON string representation of the object
print(EventRUNERROR.to_json())

# convert the object into a dict
event_runerror_dict = event_runerror_instance.to_dict()
# create an instance of EventRUNERROR from a dict
event_runerror_from_dict = EventRUNERROR.from_dict(event_runerror_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


