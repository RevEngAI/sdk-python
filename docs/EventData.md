# EventData

The payload of the event type in type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** |  | [optional] 
**definition_name** | **str** |  | [optional] 
**input_tokens** | **int** |  | [optional] 
**output_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 
**error** | **str** | Why the run failed. Null unless it failed with a reason. | 
**step_index** | **int** |  | [optional] 
**finish_reason** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 
**delta** | **str** |  | [optional] 
**tool_args** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 
**tool_name** | **str** |  | [optional] 
**is_error** | **bool** |  | [optional] 
**result** | **str** |  | [optional] 
**updated** | [**List[EntityUpdate]**](EntityUpdate.md) |  | [optional] 
**title** | **str** |  | [optional] 
**messages_after** | **int** |  | [optional] 
**messages_before** | **int** |  | [optional] 
**removed_turns** | **int** |  | [optional] 
**strategy** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**agent** | [**AgentRunUpdateAgent**](AgentRunUpdateAgent.md) |  | 
**analysis_id** | **int** | The earliest-added analysis of the file in the investigation that the conversation&#39;s starter may see. | 
**binary_name** | **str** |  | 
**card** | [**AgentRunUpdateCard**](AgentRunUpdateCard.md) | A summary of the agent&#39;s result. Absent until the run is done, and when its result cannot be summarised. | [optional] 
**created_at** | **datetime** |  | 
**investigation_id** | **int** |  | 
**task_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from revengai.models.event_data import EventData

# TODO update the JSON string below
json = "{}"
# create an instance of EventData from a JSON string
event_data_instance = EventData.from_json(json)
# print the JSON string representation of the object
print(EventData.to_json())

# convert the object into a dict
event_data_dict = event_data_instance.to_dict()
# create an instance of EventData from a dict
event_data_from_dict = EventData.from_dict(event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


