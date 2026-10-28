# AgentRunCardBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iocs** | [**List[AgentRunIOCBody]**](AgentRunIOCBody.md) |  | 
**score** | **float** | The agent&#39;s suspicion score from 0 to 1. Null when the agent gives none. | 
**summary** | **str** |  | 

## Example

```python
from revengai.models.agent_run_card_body import AgentRunCardBody

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunCardBody from a JSON string
agent_run_card_body_instance = AgentRunCardBody.from_json(json)
# print the JSON string representation of the object
print(AgentRunCardBody.to_json())

# convert the object into a dict
agent_run_card_body_dict = agent_run_card_body_instance.to_dict()
# create an instance of AgentRunCardBody from a dict
agent_run_card_body_from_dict = AgentRunCardBody.from_dict(agent_run_card_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


