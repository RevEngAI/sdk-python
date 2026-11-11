# VersionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**versions** | [**List[RuleVersion]**](RuleVersion.md) |  | 

## Example

```python
from revengai.models.versions_output_body import VersionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of VersionsOutputBody from a JSON string
versions_output_body_instance = VersionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(VersionsOutputBody.to_json())

# convert the object into a dict
versions_output_body_dict = versions_output_body_instance.to_dict()
# create an instance of VersionsOutputBody from a dict
versions_output_body_from_dict = VersionsOutputBody.from_dict(versions_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


