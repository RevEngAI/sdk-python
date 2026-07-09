# CanonicalizeNamesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Function names to canonicalize. | 

## Example

```python
from revengai.models.canonicalize_names_input_body import CanonicalizeNamesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CanonicalizeNamesInputBody from a JSON string
canonicalize_names_input_body_instance = CanonicalizeNamesInputBody.from_json(json)
# print the JSON string representation of the object
print(CanonicalizeNamesInputBody.to_json())

# convert the object into a dict
canonicalize_names_input_body_dict = canonicalize_names_input_body_instance.to_dict()
# create an instance of CanonicalizeNamesInputBody from a dict
canonicalize_names_input_body_from_dict = CanonicalizeNamesInputBody.from_dict(canonicalize_names_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


