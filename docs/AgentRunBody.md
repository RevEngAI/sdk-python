# AgentRunBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**AgentBody**](AgentBody.md) |  | 
**analysis_id** | **int** | The earliest-added analysis of the file in the investigation that you may see. | 
**binary_name** | **str** |  | 
**card** | [**AgentRunCardBody**](AgentRunCardBody.md) | A summary of the agent&#39;s result. Absent until the run is done, and when its result cannot be summarised. | [optional] 
**created_at** | **datetime** |  | 
**error** | **str** | Why the run failed. Null unless it failed with a reason. | 
**investigation_id** | **int** |  | 
**task_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from revengai.models.agent_run_body import AgentRunBody

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunBody from a JSON string
agent_run_body_instance = AgentRunBody.from_json(json)
# print the JSON string representation of the object
print(AgentRunBody.to_json())

# convert the object into a dict
agent_run_body_dict = agent_run_body_instance.to_dict()
# create an instance of AgentRunBody from a dict
agent_run_body_from_dict = AgentRunBody.from_dict(agent_run_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


