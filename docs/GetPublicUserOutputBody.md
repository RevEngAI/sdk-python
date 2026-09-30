# GetPublicUserOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The user&#39;s ID | 
**username** | **str** | The user&#39;s display name | 

## Example

```python
from revengai.models.get_public_user_output_body import GetPublicUserOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicUserOutputBody from a JSON string
get_public_user_output_body_instance = GetPublicUserOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetPublicUserOutputBody.to_json())

# convert the object into a dict
get_public_user_output_body_dict = get_public_user_output_body_instance.to_dict()
# create an instance of GetPublicUserOutputBody from a dict
get_public_user_output_body_from_dict = GetPublicUserOutputBody.from_dict(get_public_user_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


