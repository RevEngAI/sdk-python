# UpdatePasswordInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Password reset code received by email | 
**password** | **str** | New password (minimum 10 characters) | 

## Example

```python
from revengai.models.update_password_input_body import UpdatePasswordInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordInputBody from a JSON string
update_password_input_body_instance = UpdatePasswordInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdatePasswordInputBody.to_json())

# convert the object into a dict
update_password_input_body_dict = update_password_input_body_instance.to_dict()
# create an instance of UpdatePasswordInputBody from a dict
update_password_input_body_from_dict = UpdatePasswordInputBody.from_dict(update_password_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


