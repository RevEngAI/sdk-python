# SseEventRunFinishedData

The event envelope, sent as the JSON of the SSE data line. Its type names the event, and its data is that event's payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RunFinishedData**](RunFinishedData.md) | The payload of the event named in type. | 
**event_id** | **int** | The stored event&#39;s ID, the same as the SSE id field. Pass the last one received as last_event_id to resume after a reconnection. | 
**source_run_id** | **str** |  | [optional] 
**type** | **str** | The event name, the same as the SSE event field. | 

## Example

```python
from revengai.models.sse_event_run_finished_data import SseEventRunFinishedData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventRunFinishedData from a JSON string
sse_event_run_finished_data_instance = SseEventRunFinishedData.from_json(json)
# print the JSON string representation of the object
print(SseEventRunFinishedData.to_json())

# convert the object into a dict
sse_event_run_finished_data_dict = sse_event_run_finished_data_instance.to_dict()
# create an instance of SseEventRunFinishedData from a dict
sse_event_run_finished_data_from_dict = SseEventRunFinishedData.from_dict(sse_event_run_finished_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


