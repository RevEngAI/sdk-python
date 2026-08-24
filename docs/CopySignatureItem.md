# CopySignatureItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_function_id** | **int** | Function to copy the signature from. May belong to another analysis the caller can read. | 
**target_function_id** | **int** | Function to copy the signature to. Must belong to the analysis in the URL. | 

## Example

```python
from revengai.models.copy_signature_item import CopySignatureItem

# TODO update the JSON string below
json = "{}"
# create an instance of CopySignatureItem from a JSON string
copy_signature_item_instance = CopySignatureItem.from_json(json)
# print the JSON string representation of the object
print(CopySignatureItem.to_json())

# convert the object into a dict
copy_signature_item_dict = copy_signature_item_instance.to_dict()
# create an instance of CopySignatureItem from a dict
copy_signature_item_from_dict = CopySignatureItem.from_dict(copy_signature_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


