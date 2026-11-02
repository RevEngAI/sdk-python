# AgentCompletedBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **int** | Agent tasks completed that day | 

## Example

```python
from revengai.models.agent_completed_body import AgentCompletedBody

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCompletedBody from a JSON string
agent_completed_body_instance = AgentCompletedBody.from_json(json)
# print the JSON string representation of the object
print(AgentCompletedBody.to_json())

# convert the object into a dict
agent_completed_body_dict = agent_completed_body_instance.to_dict()
# create an instance of AgentCompletedBody from a dict
agent_completed_body_from_dict = AgentCompletedBody.from_dict(agent_completed_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


