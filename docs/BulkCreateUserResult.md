# BulkCreateUserResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**error** | **str** | Error description; present on failure | [optional] 
**index** | **int** | 1-based row index in the CSV | 
**success** | **bool** |  | 
**user** | [**User**](User.md) | Created user; present on success | [optional] 
**username** | **str** |  | 

## Example

```python
from revengai.models.bulk_create_user_result import BulkCreateUserResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateUserResult from a JSON string
bulk_create_user_result_instance = BulkCreateUserResult.from_json(json)
# print the JSON string representation of the object
print(BulkCreateUserResult.to_json())

# convert the object into a dict
bulk_create_user_result_dict = bulk_create_user_result_instance.to_dict()
# create an instance of BulkCreateUserResult from a dict
bulk_create_user_result_from_dict = BulkCreateUserResult.from_dict(bulk_create_user_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


