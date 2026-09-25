# BinaryExternalsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mb** | **object** |  | 
**mb_last_updated** | **datetime** | When the MalwareBazaar lookup last ran, null if never looked up | 
**sha_256_hash** | **str** | SHA-256 hash the lookups were keyed by | 
**vt** | **object** |  | 
**vt_last_updated** | **datetime** | When the VirusTotal lookup last ran | 

## Example

```python
from revengai.models.binary_externals_body import BinaryExternalsBody

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryExternalsBody from a JSON string
binary_externals_body_instance = BinaryExternalsBody.from_json(json)
# print the JSON string representation of the object
print(BinaryExternalsBody.to_json())

# convert the object into a dict
binary_externals_body_dict = binary_externals_body_instance.to_dict()
# create an instance of BinaryExternalsBody from a dict
binary_externals_body_from_dict = BinaryExternalsBody.from_dict(binary_externals_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


