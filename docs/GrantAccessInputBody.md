# GrantAccessInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | The level of access to grant | 
**team_id** | **int** | The team to share with. Exactly one of user_id and team_id is required | [optional] 
**user_id** | **int** | The user to share with. Exactly one of user_id and team_id is required | [optional] 

## Example

```python
from revengai.models.grant_access_input_body import GrantAccessInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GrantAccessInputBody from a JSON string
grant_access_input_body_instance = GrantAccessInputBody.from_json(json)
# print the JSON string representation of the object
print(GrantAccessInputBody.to_json())

# convert the object into a dict
grant_access_input_body_dict = grant_access_input_body_instance.to_dict()
# create an instance of GrantAccessInputBody from a dict
grant_access_input_body_from_dict = GrantAccessInputBody.from_dict(grant_access_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


