# PublicUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The user&#39;s ID | 
**username** | **str** | The user&#39;s display name | 

## Example

```python
from revengai.models.public_user_body import PublicUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of PublicUserBody from a JSON string
public_user_body_instance = PublicUserBody.from_json(json)
# print the JSON string representation of the object
print(PublicUserBody.to_json())

# convert the object into a dict
public_user_body_dict = public_user_body_instance.to_dict()
# create an instance of PublicUserBody from a dict
public_user_body_from_dict = PublicUserBody.from_dict(public_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


