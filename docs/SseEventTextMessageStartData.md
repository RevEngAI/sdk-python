# SseEventTextMessageStartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_text_message_start_data import SseEventTextMessageStartData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventTextMessageStartData from a JSON string
sse_event_text_message_start_data_instance = SseEventTextMessageStartData.from_json(json)
# print the JSON string representation of the object
print(SseEventTextMessageStartData.to_json())

# convert the object into a dict
sse_event_text_message_start_data_dict = sse_event_text_message_start_data_instance.to_dict()
# create an instance of SseEventTextMessageStartData from a dict
sse_event_text_message_start_data_from_dict = SseEventTextMessageStartData.from_dict(sse_event_text_message_start_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


