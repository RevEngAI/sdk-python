# AutoRunAgentsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triage** | **bool** | Whether the triage agent ran automatically once the functions pipeline finished | 

## Example

```python
from revengai.models.auto_run_agents_body import AutoRunAgentsBody

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRunAgentsBody from a JSON string
auto_run_agents_body_instance = AutoRunAgentsBody.from_json(json)
# print the JSON string representation of the object
print(AutoRunAgentsBody.to_json())

# convert the object into a dict
auto_run_agents_body_dict = auto_run_agents_body_instance.to_dict()
# create an instance of AutoRunAgentsBody from a dict
auto_run_agents_body_from_dict = AutoRunAgentsBody.from_dict(auto_run_agents_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


