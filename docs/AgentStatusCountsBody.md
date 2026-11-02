# AgentStatusCountsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents_running** | **int** |  | 
**complete** | **int** |  | 
**queued** | **int** |  | 

## Example

```python
from revengai.models.agent_status_counts_body import AgentStatusCountsBody

# TODO update the JSON string below
json = "{}"
# create an instance of AgentStatusCountsBody from a JSON string
agent_status_counts_body_instance = AgentStatusCountsBody.from_json(json)
# print the JSON string representation of the object
print(AgentStatusCountsBody.to_json())

# convert the object into a dict
agent_status_counts_body_dict = agent_status_counts_body_instance.to_dict()
# create an instance of AgentStatusCountsBody from a dict
agent_status_counts_body_from_dict = AgentStatusCountsBody.from_dict(agent_status_counts_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


