# SignatureParameterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_length** | **int** | Width in bits, when the parameter occupies less than its type&#39;s full size. | [optional] 
**data_type_id** | **int** | The parameter&#39;s type, which must belong to this analysis. Omit for an unresolved type. | [optional] 
**name** | **str** | Parameter name. Omit for an unnamed parameter. | [optional] 
**ordinal** | **int** | Zero-based argument position. Must equal the parameter&#39;s index in the list. | 
**storage** | [**SignatureStorageInput**](SignatureStorageInput.md) | Where the parameter is passed. | [optional] 

## Example

```python
from revengai.models.signature_parameter_input import SignatureParameterInput

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureParameterInput from a JSON string
signature_parameter_input_instance = SignatureParameterInput.from_json(json)
# print the JSON string representation of the object
print(SignatureParameterInput.to_json())

# convert the object into a dict
signature_parameter_input_dict = signature_parameter_input_instance.to_dict()
# create an instance of SignatureParameterInput from a dict
signature_parameter_input_from_dict = SignatureParameterInput.from_dict(signature_parameter_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


