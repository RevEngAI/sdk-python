# UpdateUserInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**role** | **str** | User role (SUPERADMIN only) | [optional] 
**tier** | **str** | User tier (SUPERADMIN only) | [optional] 
**time_zone** | **str** | IANA time zone | [optional] 
**username** | **str** | Username | [optional] 

## Example

```python
from revengai.models.update_user_input_body import UpdateUserInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserInputBody from a JSON string
update_user_input_body_instance = UpdateUserInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateUserInputBody.to_json())

# convert the object into a dict
update_user_input_body_dict = update_user_input_body_instance.to_dict()
# create an instance of UpdateUserInputBody from a dict
update_user_input_body_from_dict = UpdateUserInputBody.from_dict(update_user_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


