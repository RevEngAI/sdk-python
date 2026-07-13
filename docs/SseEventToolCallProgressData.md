# SseEventToolCallProgressData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**source_run_id** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_tool_call_progress_data import SseEventToolCallProgressData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventToolCallProgressData from a JSON string
sse_event_tool_call_progress_data_instance = SseEventToolCallProgressData.from_json(json)
# print the JSON string representation of the object
print(SseEventToolCallProgressData.to_json())

# convert the object into a dict
sse_event_tool_call_progress_data_dict = sse_event_tool_call_progress_data_instance.to_dict()
# create an instance of SseEventToolCallProgressData from a dict
sse_event_tool_call_progress_data_from_dict = SseEventToolCallProgressData.from_dict(sse_event_tool_call_progress_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


