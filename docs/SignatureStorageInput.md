# SignatureStorageInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Storage class — typically reg, stack, mem or unknown. Not restricted to a fixed set. | [optional] 
**location** | **str** | Register name or stack slot. | [optional] 

## Example

```python
from revengai.models.signature_storage_input import SignatureStorageInput

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureStorageInput from a JSON string
signature_storage_input_instance = SignatureStorageInput.from_json(json)
# print the JSON string representation of the object
print(SignatureStorageInput.to_json())

# convert the object into a dict
signature_storage_input_dict = signature_storage_input_instance.to_dict()
# create an instance of SignatureStorageInput from a dict
signature_storage_input_from_dict = SignatureStorageInput.from_dict(signature_storage_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


