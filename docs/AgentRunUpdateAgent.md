# AgentRunUpdateAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** | Stable identifier of the agent. | 
**state** | **str** |  | 

## Example

```python
from revengai.models.agent_run_update_agent import AgentRunUpdateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunUpdateAgent from a JSON string
agent_run_update_agent_instance = AgentRunUpdateAgent.from_json(json)
# print the JSON string representation of the object
print(AgentRunUpdateAgent.to_json())

# convert the object into a dict
agent_run_update_agent_dict = agent_run_update_agent_instance.to_dict()
# create an instance of AgentRunUpdateAgent from a dict
agent_run_update_agent_from_dict = AgentRunUpdateAgent.from_dict(agent_run_update_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


