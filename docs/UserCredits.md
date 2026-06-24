# UserCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**credits** | **int** |  | 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **int** |  | 

## Example

```python
from revengai.models.user_credits import UserCredits

# TODO update the JSON string below
json = "{}"
# create an instance of UserCredits from a JSON string
user_credits_instance = UserCredits.from_json(json)
# print the JSON string representation of the object
print(UserCredits.to_json())

# convert the object into a dict
user_credits_dict = user_credits_instance.to_dict()
# create an instance of UserCredits from a dict
user_credits_from_dict = UserCredits.from_dict(user_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


