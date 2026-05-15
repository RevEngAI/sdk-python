# UpsertOverridesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overrides** | **Dict[str, str]** | Token to name mappings. Empty string removes the override. | 

## Example

```python
from revengai.models.upsert_overrides_input_body import UpsertOverridesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertOverridesInputBody from a JSON string
upsert_overrides_input_body_instance = UpsertOverridesInputBody.from_json(json)
# print the JSON string representation of the object
print(UpsertOverridesInputBody.to_json())

# convert the object into a dict
upsert_overrides_input_body_dict = upsert_overrides_input_body_instance.to_dict()
# create an instance of UpsertOverridesInputBody from a dict
upsert_overrides_input_body_from_dict = UpsertOverridesInputBody.from_dict(upsert_overrides_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


