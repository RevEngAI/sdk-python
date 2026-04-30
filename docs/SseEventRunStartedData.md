# SseEventRunStartedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_run_started_data import SseEventRunStartedData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventRunStartedData from a JSON string
sse_event_run_started_data_instance = SseEventRunStartedData.from_json(json)
# print the JSON string representation of the object
print(SseEventRunStartedData.to_json())

# convert the object into a dict
sse_event_run_started_data_dict = sse_event_run_started_data_instance.to_dict()
# create an instance of SseEventRunStartedData from a dict
sse_event_run_started_data_from_dict = SseEventRunStartedData.from_dict(sse_event_run_started_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


