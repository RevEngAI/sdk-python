# RuleVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**rule_hash** | **str** | Content hash of the version&#39;s source | 
**source** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from revengai.models.rule_version import RuleVersion

# TODO update the JSON string below
json = "{}"
# create an instance of RuleVersion from a JSON string
rule_version_instance = RuleVersion.from_json(json)
# print the JSON string representation of the object
print(RuleVersion.to_json())

# convert the object into a dict
rule_version_dict = rule_version_instance.to_dict()
# create an instance of RuleVersion from a dict
rule_version_from_dict = RuleVersion.from_dict(rule_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


