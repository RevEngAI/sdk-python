# SseEventToolConfirmationRequiredData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**event_id** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.sse_event_tool_confirmation_required_data import SseEventToolConfirmationRequiredData

# TODO update the JSON string below
json = "{}"
# create an instance of SseEventToolConfirmationRequiredData from a JSON string
sse_event_tool_confirmation_required_data_instance = SseEventToolConfirmationRequiredData.from_json(json)
# print the JSON string representation of the object
print(SseEventToolConfirmationRequiredData.to_json())

# convert the object into a dict
sse_event_tool_confirmation_required_data_dict = sse_event_tool_confirmation_required_data_instance.to_dict()
# create an instance of SseEventToolConfirmationRequiredData from a dict
sse_event_tool_confirmation_required_data_from_dict = SseEventToolConfirmationRequiredData.from_dict(sse_event_tool_confirmation_required_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


