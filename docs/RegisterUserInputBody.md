# RegisterUserInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address | 
**first_name** | **str** | First name | 
**invite_code** | **str** | Invite code from the registration email | [optional] 
**last_name** | **str** | Last name | 
**password** | **str** | Password (minimum 10 characters) | 
**username** | **str** | Username | 

## Example

```python
from revengai.models.register_user_input_body import RegisterUserInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserInputBody from a JSON string
register_user_input_body_instance = RegisterUserInputBody.from_json(json)
# print the JSON string representation of the object
print(RegisterUserInputBody.to_json())

# convert the object into a dict
register_user_input_body_dict = register_user_input_body_instance.to_dict()
# create an instance of RegisterUserInputBody from a dict
register_user_input_body_from_dict = RegisterUserInputBody.from_dict(register_user_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


