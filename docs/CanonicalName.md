# CanonicalName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_name** | **str** | Canonical form of the name, or the input name itself when it has no canonical form. | 
**name** | **str** | The input function name. | 

## Example

```python
from revengai.models.canonical_name import CanonicalName

# TODO update the JSON string below
json = "{}"
# create an instance of CanonicalName from a JSON string
canonical_name_instance = CanonicalName.from_json(json)
# print the JSON string representation of the object
print(CanonicalName.to_json())

# convert the object into a dict
canonical_name_dict = canonical_name_instance.to_dict()
# create an instance of CanonicalName from a dict
canonical_name_from_dict = CanonicalName.from_dict(canonical_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


