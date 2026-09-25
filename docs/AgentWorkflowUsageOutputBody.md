# AgentWorkflowUsageOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**List[WorkflowDayBody]**](WorkflowDayBody.md) | One entry per day in the requested window, oldest first | 

## Example

```python
from revengai.models.agent_workflow_usage_output_body import AgentWorkflowUsageOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AgentWorkflowUsageOutputBody from a JSON string
agent_workflow_usage_output_body_instance = AgentWorkflowUsageOutputBody.from_json(json)
# print the JSON string representation of the object
print(AgentWorkflowUsageOutputBody.to_json())

# convert the object into a dict
agent_workflow_usage_output_body_dict = agent_workflow_usage_output_body_instance.to_dict()
# create an instance of AgentWorkflowUsageOutputBody from a dict
agent_workflow_usage_output_body_from_dict = AgentWorkflowUsageOutputBody.from_dict(agent_workflow_usage_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


