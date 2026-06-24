# UpdateUserCreditsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** | Credit balance to set | 

## Example

```python
from revengai.models.update_user_credits_input_body import UpdateUserCreditsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserCreditsInputBody from a JSON string
update_user_credits_input_body_instance = UpdateUserCreditsInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateUserCreditsInputBody.to_json())

# convert the object into a dict
update_user_credits_input_body_dict = update_user_credits_input_body_instance.to_dict()
# create an instance of UpdateUserCreditsInputBody from a dict
update_user_credits_input_body_from_dict = UpdateUserCreditsInputBody.from_dict(update_user_credits_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


