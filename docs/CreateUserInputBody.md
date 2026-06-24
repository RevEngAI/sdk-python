# CreateUserInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** | Initial credit balance in credits (1 credit &#x3D; 1000 units); defaults to 10 credits | [optional] 
**email** | **str** | Email address | 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**password** | **str** | Initial password | 
**role** | **str** | User role (defaults to USER) | [optional] 
**tier** | **str** | User tier (defaults to ENTHUSIAST) | [optional] 
**time_zone** | **str** | IANA time zone | [optional] 
**username** | **str** | Username | 

## Example

```python
from revengai.models.create_user_input_body import CreateUserInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserInputBody from a JSON string
create_user_input_body_instance = CreateUserInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateUserInputBody.to_json())

# convert the object into a dict
create_user_input_body_dict = create_user_input_body_instance.to_dict()
# create an instance of CreateUserInputBody from a dict
create_user_input_body_from_dict = CreateUserInputBody.from_dict(create_user_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


