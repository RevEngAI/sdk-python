# EventDecompFinished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DecompFinishedEvent**](DecompFinishedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_decomp_finished import EventDecompFinished

# TODO update the JSON string below
json = "{}"
# create an instance of EventDecompFinished from a JSON string
event_decomp_finished_instance = EventDecompFinished.from_json(json)
# print the JSON string representation of the object
print(EventDecompFinished.to_json())

# convert the object into a dict
event_decomp_finished_dict = event_decomp_finished_instance.to_dict()
# create an instance of EventDecompFinished from a dict
event_decomp_finished_from_dict = EventDecompFinished.from_dict(event_decomp_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


