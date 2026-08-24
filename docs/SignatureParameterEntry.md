# SignatureParameterEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_length** | **int** | Width in bits, when the parameter occupies less than its type&#39;s full size. | [optional] 
**data_type_id** | **int** | The parameter&#39;s type, resolvable against the analysis data types list. Absent when the type could not be resolved. | [optional] 
**name** | **str** | Parameter name, absent when the producer had none. | [optional] 
**ordinal** | **int** | Zero-based argument position. | 
**storage** | [**SignatureStorageEntry**](SignatureStorageEntry.md) | Where the parameter is passed. | [optional] 

## Example

```python
from revengai.models.signature_parameter_entry import SignatureParameterEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureParameterEntry from a JSON string
signature_parameter_entry_instance = SignatureParameterEntry.from_json(json)
# print the JSON string representation of the object
print(SignatureParameterEntry.to_json())

# convert the object into a dict
signature_parameter_entry_dict = signature_parameter_entry_instance.to_dict()
# create an instance of SignatureParameterEntry from a dict
signature_parameter_entry_from_dict = SignatureParameterEntry.from_dict(signature_parameter_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


