# ListUsersOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**users** | [**List[User]**](User.md) |  | 

## Example

```python
from revengai.models.list_users_output_body import ListUsersOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersOutputBody from a JSON string
list_users_output_body_instance = ListUsersOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListUsersOutputBody.to_json())

# convert the object into a dict
list_users_output_body_dict = list_users_output_body_instance.to_dict()
# create an instance of ListUsersOutputBody from a dict
list_users_output_body_from_dict = ListUsersOutputBody.from_dict(list_users_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


