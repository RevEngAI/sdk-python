# SseEventStepFinishedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_step_finished_data import SseEventStepFinishedData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventStepFinishedData from a JSON string
sse_event_step_finished_data_instance = SseEventStepFinishedData.from_json(json)
# print the JSON string representation of the object
print(SseEventStepFinishedData.to_json())

# convert the object into a dict
sse_event_step_finished_data_dict = sse_event_step_finished_data_instance.to_dict()
# create an instance of SseEventStepFinishedData from a dict
sse_event_step_finished_data_from_dict = SseEventStepFinishedData.from_dict(sse_event_step_finished_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


