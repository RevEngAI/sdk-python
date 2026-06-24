# AddTeamMemberInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID to add | 

## Example

```python
from revengai.models.add_team_member_input_body import AddTeamMemberInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddTeamMemberInputBody from a JSON string
add_team_member_input_body_instance = AddTeamMemberInputBody.from_json(json)
# print the JSON string representation of the object
print(AddTeamMemberInputBody.to_json())

# convert the object into a dict
add_team_member_input_body_dict = add_team_member_input_body_instance.to_dict()
# create an instance of AddTeamMemberInputBody from a dict
add_team_member_input_body_from_dict = AddTeamMemberInputBody.from_dict(add_team_member_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


