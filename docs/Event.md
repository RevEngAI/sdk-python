# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** |  | 
**created_at** | **datetime** |  | 
**data** | [**EventData**](EventData.md) |  | 
**event_id** | **int** |  | 
**role** | **int** |  | 
**tokens_used** | **int** |  | 
**type** | **int** | The event type, which decides the shape of data: 1 RUN_STARTED, 2 RUN_FINISHED, 3 RUN_ERROR, 4 STEP_STARTED, 5 STEP_FINISHED, 6 TEXT_MESSAGE_START, 7 TEXT_MESSAGE_CONTENT, 8 TEXT_MESSAGE_END, 9 TOOL_CALL_START, 10 TOOL_CALL_ARGS_DELTA, 11 TOOL_CALL_END, 12 TOOL_CALL_RESULT, 13 TITLE_UPDATED, 14 RUN_CANCELLED, 15 CONTEXT_COMPACTED, 16 TOOL_CONFIRMATION_REQUIRED, 19 TOOL_CALL_PROGRESS, 20 AGENT_RUN_UPDATE. | 

## Example

```python
from revengai.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


