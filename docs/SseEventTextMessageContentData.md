# SseEventTextMessageContentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_text_message_content_data import SseEventTextMessageContentData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventTextMessageContentData from a JSON string
sse_event_text_message_content_data_instance = SseEventTextMessageContentData.from_json(json)
# print the JSON string representation of the object
print(SseEventTextMessageContentData.to_json())

# convert the object into a dict
sse_event_text_message_content_data_dict = sse_event_text_message_content_data_instance.to_dict()
# create an instance of SseEventTextMessageContentData from a dict
sse_event_text_message_content_data_from_dict = SseEventTextMessageContentData.from_dict(sse_event_text_message_content_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


