# CopyFunctionSignaturesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copies** | [**List[CopySignatureItem]**](CopySignatureItem.md) | Signatures to copy. No target may repeat, and no pair may name the same function twice. | 

## Example

```python
from revengai.models.copy_function_signatures_input_body import CopyFunctionSignaturesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CopyFunctionSignaturesInputBody from a JSON string
copy_function_signatures_input_body_instance = CopyFunctionSignaturesInputBody.from_json(json)
# print the JSON string representation of the object
print(CopyFunctionSignaturesInputBody.to_json())

# convert the object into a dict
copy_function_signatures_input_body_dict = copy_function_signatures_input_body_instance.to_dict()
# create an instance of CopyFunctionSignaturesInputBody from a dict
copy_function_signatures_input_body_from_dict = CopyFunctionSignaturesInputBody.from_dict(copy_function_signatures_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


