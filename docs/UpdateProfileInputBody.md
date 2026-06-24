# UpdateProfileInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_team_id** | **int** | Default team ID | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**time_zone** | **str** | IANA time zone | [optional] 
**username** | **str** | Username | [optional] 

## Example

```python
from revengai.models.update_profile_input_body import UpdateProfileInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfileInputBody from a JSON string
update_profile_input_body_instance = UpdateProfileInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateProfileInputBody.to_json())

# convert the object into a dict
update_profile_input_body_dict = update_profile_input_body_instance.to_dict()
# create an instance of UpdateProfileInputBody from a dict
update_profile_input_body_from_dict = UpdateProfileInputBody.from_dict(update_profile_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


