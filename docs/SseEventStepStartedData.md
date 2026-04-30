# SseEventStepStartedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_step_started_data import SseEventStepStartedData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventStepStartedData from a JSON string
sse_event_step_started_data_instance = SseEventStepStartedData.from_json(json)
# print the JSON string representation of the object
print(SseEventStepStartedData.to_json())

# convert the object into a dict
sse_event_step_started_data_dict = sse_event_step_started_data_instance.to_dict()
# create an instance of SseEventStepStartedData from a dict
sse_event_step_started_data_from_dict = SseEventStepStartedData.from_dict(sse_event_step_started_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


