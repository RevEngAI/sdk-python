# DeleteMeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Current password. Required for users who sign in with a password; ignored for users from an external identity provider. | [optional] 

## Example

```python
from revengai.models.delete_me_body import DeleteMeBody

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMeBody from a JSON string
delete_me_body_instance = DeleteMeBody.from_json(json)
# print the JSON string representation of the object
print(DeleteMeBody.to_json())

# convert the object into a dict
delete_me_body_dict = delete_me_body_instance.to_dict()
# create an instance of DeleteMeBody from a dict
delete_me_body_from_dict = DeleteMeBody.from_dict(delete_me_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


