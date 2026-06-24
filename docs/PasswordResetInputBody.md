# PasswordResetInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the account whose password should be reset | 

## Example

```python
from revengai.models.password_reset_input_body import PasswordResetInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordResetInputBody from a JSON string
password_reset_input_body_instance = PasswordResetInputBody.from_json(json)
# print the JSON string representation of the object
print(PasswordResetInputBody.to_json())

# convert the object into a dict
password_reset_input_body_dict = password_reset_input_body_instance.to_dict()
# create an instance of PasswordResetInputBody from a dict
password_reset_input_body_from_dict = PasswordResetInputBody.from_dict(password_reset_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


