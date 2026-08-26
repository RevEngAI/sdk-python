# EventNamesFinished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NamesFinishedEvent**](NamesFinishedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_names_finished import EventNamesFinished

# TODO update the JSON string below
json = "{}"
# create an instance of EventNamesFinished from a JSON string
event_names_finished_instance = EventNamesFinished.from_json(json)
# print the JSON string representation of the object
print(EventNamesFinished.to_json())

# convert the object into a dict
event_names_finished_dict = event_names_finished_instance.to_dict()
# create an instance of EventNamesFinished from a dict
event_names_finished_from_dict = EventNamesFinished.from_dict(event_names_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


