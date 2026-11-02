# AgentRunUpdateIOC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**source** | **str** | Where in the binary the agent found the indicator. Empty when the agent gives no location. | 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from revengai.models.agent_run_update_ioc import AgentRunUpdateIOC

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunUpdateIOC from a JSON string
agent_run_update_ioc_instance = AgentRunUpdateIOC.from_json(json)
# print the JSON string representation of the object
print(AgentRunUpdateIOC.to_json())

# convert the object into a dict
agent_run_update_ioc_dict = agent_run_update_ioc_instance.to_dict()
# create an instance of AgentRunUpdateIOC from a dict
agent_run_update_ioc_from_dict = AgentRunUpdateIOC.from_dict(agent_run_update_ioc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


