# ListAgentRunsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**results** | [**List[AgentRunBody]**](AgentRunBody.md) |  | 
**total_count** | **int** | Runs matching the filters across all pages. | 

## Example

```python
from revengai.models.list_agent_runs_output_body import ListAgentRunsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAgentRunsOutputBody from a JSON string
list_agent_runs_output_body_instance = ListAgentRunsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAgentRunsOutputBody.to_json())

# convert the object into a dict
list_agent_runs_output_body_dict = list_agent_runs_output_body_instance.to_dict()
# create an instance of ListAgentRunsOutputBody from a dict
list_agent_runs_output_body_from_dict = ListAgentRunsOutputBody.from_dict(list_agent_runs_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


