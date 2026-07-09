# CanonicalizeNamesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CanonicalName]**](CanonicalName.md) | Canonicalized names in the same order as the input. | 

## Example

```python
from revengai.models.canonicalize_names_output_body import CanonicalizeNamesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CanonicalizeNamesOutputBody from a JSON string
canonicalize_names_output_body_instance = CanonicalizeNamesOutputBody.from_json(json)
# print the JSON string representation of the object
print(CanonicalizeNamesOutputBody.to_json())

# convert the object into a dict
canonicalize_names_output_body_dict = canonicalize_names_output_body_instance.to_dict()
# create an instance of CanonicalizeNamesOutputBody from a dict
canonicalize_names_output_body_from_dict = CanonicalizeNamesOutputBody.from_dict(canonicalize_names_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


