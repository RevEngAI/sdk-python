# UpsertOverridesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_override_mappings** | **Dict[str, str]** | Merged override mappings after applying changes | 

## Example

```python
from revengai.models.upsert_overrides_data import UpsertOverridesData

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertOverridesData from a JSON string
upsert_overrides_data_instance = UpsertOverridesData.from_json(json)
# print the JSON string representation of the object
print(UpsertOverridesData.to_json())

# convert the object into a dict
upsert_overrides_data_dict = upsert_overrides_data_instance.to_dict()
# create an instance of UpsertOverridesData from a dict
upsert_overrides_data_from_dict = UpsertOverridesData.from_dict(upsert_overrides_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


