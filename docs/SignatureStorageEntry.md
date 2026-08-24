# SignatureStorageEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Storage class — typically reg, stack, mem or unknown. Not restricted to a fixed set. | [optional] 
**location** | **str** | Register name or stack slot. | [optional] 

## Example

```python
from revengai.models.signature_storage_entry import SignatureStorageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureStorageEntry from a JSON string
signature_storage_entry_instance = SignatureStorageEntry.from_json(json)
# print the JSON string representation of the object
print(SignatureStorageEntry.to_json())

# convert the object into a dict
signature_storage_entry_dict = signature_storage_entry_instance.to_dict()
# create an instance of SignatureStorageEntry from a dict
signature_storage_entry_from_dict = SignatureStorageEntry.from_dict(signature_storage_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


