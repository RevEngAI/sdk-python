# AutoRunAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triage** | **bool** |  | [optional] [default to False]

## Example

```python
from revengai.models.auto_run_agents import AutoRunAgents

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRunAgents from a JSON string
auto_run_agents_instance = AutoRunAgents.from_json(json)
# print the JSON string representation of the object
print(AutoRunAgents.to_json())

# convert the object into a dict
auto_run_agents_dict = auto_run_agents_instance.to_dict()
# create an instance of AutoRunAgents from a dict
auto_run_agents_from_dict = AutoRunAgents.from_dict(auto_run_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


