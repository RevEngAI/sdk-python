# AddOwnerInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID to add as owner | 

## Example

```python
from revengai.models.add_owner_input_body import AddOwnerInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddOwnerInputBody from a JSON string
add_owner_input_body_instance = AddOwnerInputBody.from_json(json)
# print the JSON string representation of the object
print(AddOwnerInputBody.to_json())

# convert the object into a dict
add_owner_input_body_dict = add_owner_input_body_instance.to_dict()
# create an instance of AddOwnerInputBody from a dict
add_owner_input_body_from_dict = AddOwnerInputBody.from_dict(add_owner_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


