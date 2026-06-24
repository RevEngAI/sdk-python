# UpdateTeamInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_name** | **str** | Team name | [optional] 

## Example

```python
from revengai.models.update_team_input_body import UpdateTeamInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamInputBody from a JSON string
update_team_input_body_instance = UpdateTeamInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamInputBody.to_json())

# convert the object into a dict
update_team_input_body_dict = update_team_input_body_instance.to_dict()
# create an instance of UpdateTeamInputBody from a dict
update_team_input_body_from_dict = UpdateTeamInputBody.from_dict(update_team_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


