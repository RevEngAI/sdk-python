# AgentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** | Stable identifier of the agent. | 
**state** | **str** |  | 

## Example

```python
from revengai.models.agent_body import AgentBody

# TODO update the JSON string below
json = "{}"
# create an instance of AgentBody from a JSON string
agent_body_instance = AgentBody.from_json(json)
# print the JSON string representation of the object
print(AgentBody.to_json())

# convert the object into a dict
agent_body_dict = agent_body_instance.to_dict()
# create an instance of AgentBody from a dict
agent_body_from_dict = AgentBody.from_dict(agent_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


