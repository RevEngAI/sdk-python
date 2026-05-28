# AddUserStringToFunctionInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | String literal | 
**virtual_address** | **int** | Virtual address at which this string is defined. | 

## Example

```python
from revengai.models.add_user_string_to_function_input_body import AddUserStringToFunctionInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserStringToFunctionInputBody from a JSON string
add_user_string_to_function_input_body_instance = AddUserStringToFunctionInputBody.from_json(json)
# print the JSON string representation of the object
print(AddUserStringToFunctionInputBody.to_json())

# convert the object into a dict
add_user_string_to_function_input_body_dict = add_user_string_to_function_input_body_instance.to_dict()
# create an instance of AddUserStringToFunctionInputBody from a dict
add_user_string_to_function_input_body_from_dict = AddUserStringToFunctionInputBody.from_dict(add_user_string_to_function_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


