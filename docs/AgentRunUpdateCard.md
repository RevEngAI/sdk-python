# AgentRunUpdateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iocs** | [**List[AgentRunUpdateIOC]**](AgentRunUpdateIOC.md) |  | 
**score** | **float** | The agent&#39;s suspicion score from 0 to 1. Null when the agent gives none. | 
**summary** | **str** |  | 

## Example

```python
from revengai.models.agent_run_update_card import AgentRunUpdateCard

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunUpdateCard from a JSON string
agent_run_update_card_instance = AgentRunUpdateCard.from_json(json)
# print the JSON string representation of the object
print(AgentRunUpdateCard.to_json())

# convert the object into a dict
agent_run_update_card_dict = agent_run_update_card_instance.to_dict()
# create an instance of AgentRunUpdateCard from a dict
agent_run_update_card_from_dict = AgentRunUpdateCard.from_dict(agent_run_update_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


