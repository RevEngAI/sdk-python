# SseEventRunCancelledData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_run_cancelled_data import SseEventRunCancelledData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventRunCancelledData from a JSON string
sse_event_run_cancelled_data_instance = SseEventRunCancelledData.from_json(json)
# print the JSON string representation of the object
print(SseEventRunCancelledData.to_json())

# convert the object into a dict
sse_event_run_cancelled_data_dict = sse_event_run_cancelled_data_instance.to_dict()
# create an instance of SseEventRunCancelledData from a dict
sse_event_run_cancelled_data_from_dict = SseEventRunCancelledData.from_dict(sse_event_run_cancelled_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


