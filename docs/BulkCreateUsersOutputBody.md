# BulkCreateUsersOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** |  | 
**results** | [**List[BulkCreateUserResult]**](BulkCreateUserResult.md) |  | 
**succeeded** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from revengai.models.bulk_create_users_output_body import BulkCreateUsersOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateUsersOutputBody from a JSON string
bulk_create_users_output_body_instance = BulkCreateUsersOutputBody.from_json(json)
# print the JSON string representation of the object
print(BulkCreateUsersOutputBody.to_json())

# convert the object into a dict
bulk_create_users_output_body_dict = bulk_create_users_output_body_instance.to_dict()
# create an instance of BulkCreateUsersOutputBody from a dict
bulk_create_users_output_body_from_dict = BulkCreateUsersOutputBody.from_dict(bulk_create_users_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


