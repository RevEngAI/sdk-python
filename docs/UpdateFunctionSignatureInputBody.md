# UpdateFunctionSignatureInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calling_convention** | **str** | Calling convention. Omit when there is none to record. | [optional] 
**parameters** | [**List[SignatureParameterInput]**](SignatureParameterInput.md) | Parameters in argument order. An empty list records a function that takes no arguments. | 
**return_data_type_id** | **int** | Return type, which must belong to this analysis. Omit for an unresolved return type. | [optional] 

## Example

```python
from revengai.models.update_function_signature_input_body import UpdateFunctionSignatureInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFunctionSignatureInputBody from a JSON string
update_function_signature_input_body_instance = UpdateFunctionSignatureInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateFunctionSignatureInputBody.to_json())

# convert the object into a dict
update_function_signature_input_body_dict = update_function_signature_input_body_instance.to_dict()
# create an instance of UpdateFunctionSignatureInputBody from a dict
update_function_signature_input_body_from_dict = UpdateFunctionSignatureInputBody.from_dict(update_function_signature_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


