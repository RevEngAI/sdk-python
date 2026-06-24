# InviteUserInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** | Initial credit balance for the invited user in raw units (1 credit &#x3D; 1000 units). | 
**email** | **str** | Email address to invite | 
**first_name** | **str** | First name included in the invite email and registration URL | 
**last_name** | **str** | Last name pre-filled in the registration URL | [optional] 
**team_id** | **int** | Team to assign the invited user to | [optional] 
**username** | **str** | Username pre-filled in the registration URL | [optional] 

## Example

```python
from revengai.models.invite_user_input_body import InviteUserInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserInputBody from a JSON string
invite_user_input_body_instance = InviteUserInputBody.from_json(json)
# print the JSON string representation of the object
print(InviteUserInputBody.to_json())

# convert the object into a dict
invite_user_input_body_dict = invite_user_input_body_instance.to_dict()
# create an instance of InviteUserInputBody from a dict
invite_user_input_body_from_dict = InviteUserInputBody.from_dict(invite_user_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


