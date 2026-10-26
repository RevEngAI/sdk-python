# ListPublicUsersOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PublicUserBody]**](PublicUserBody.md) | Up to 5 matching active users, ordered by username | 

## Example

```python
from revengai.models.list_public_users_output_body import ListPublicUsersOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListPublicUsersOutputBody from a JSON string
list_public_users_output_body_instance = ListPublicUsersOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListPublicUsersOutputBody.to_json())

# convert the object into a dict
list_public_users_output_body_dict = list_public_users_output_body_instance.to_dict()
# create an instance of ListPublicUsersOutputBody from a dict
list_public_users_output_body_from_dict = ListPublicUsersOutputBody.from_dict(list_public_users_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


