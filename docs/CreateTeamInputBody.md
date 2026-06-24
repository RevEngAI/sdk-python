# CreateTeamInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Team name | 

## Example

```python
from revengai.models.create_team_input_body import CreateTeamInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamInputBody from a JSON string
create_team_input_body_instance = CreateTeamInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateTeamInputBody.to_json())

# convert the object into a dict
create_team_input_body_dict = create_team_input_body_instance.to_dict()
# create an instance of CreateTeamInputBody from a dict
create_team_input_body_from_dict = CreateTeamInputBody.from_dict(create_team_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


