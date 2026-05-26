# EventSourceReset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SourceResetEvent**](SourceResetEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_source_reset import EventSourceReset

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourceReset from a JSON string
event_source_reset_instance = EventSourceReset.from_json(json)
# print the JSON string representation of the object
print(EventSourceReset.to_json())

# convert the object into a dict
event_source_reset_dict = event_source_reset_instance.to_dict()
# create an instance of EventSourceReset from a dict
event_source_reset_from_dict = EventSourceReset.from_dict(event_source_reset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


