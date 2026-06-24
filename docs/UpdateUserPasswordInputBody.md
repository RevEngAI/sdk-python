# UpdateUserPasswordInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Current password (required when changing your own password; ignored for SUPERADMIN updates of other users) | [optional] 
**new_password** | **str** | New password (minimum 10 characters) | 

## Example

```python
from revengai.models.update_user_password_input_body import UpdateUserPasswordInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPasswordInputBody from a JSON string
update_user_password_input_body_instance = UpdateUserPasswordInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateUserPasswordInputBody.to_json())

# convert the object into a dict
update_user_password_input_body_dict = update_user_password_input_body_instance.to_dict()
# create an instance of UpdateUserPasswordInputBody from a dict
update_user_password_input_body_from_dict = UpdateUserPasswordInputBody.from_dict(update_user_password_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


