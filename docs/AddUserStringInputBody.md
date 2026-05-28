# AddUserStringInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | String literal | 
**virtual_address** | **int** | Virtual address at which this string is defined. | 

## Example

```python
from revengai.models.add_user_string_input_body import AddUserStringInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserStringInputBody from a JSON string
add_user_string_input_body_instance = AddUserStringInputBody.from_json(json)
# print the JSON string representation of the object
print(AddUserStringInputBody.to_json())

# convert the object into a dict
add_user_string_input_body_dict = add_user_string_input_body_instance.to_dict()
# create an instance of AddUserStringInputBody from a dict
add_user_string_input_body_from_dict = AddUserStringInputBody.from_dict(add_user_string_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


