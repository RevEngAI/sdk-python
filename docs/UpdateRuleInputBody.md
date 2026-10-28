# UpdateRuleInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**source** | **str** | New YARA rule source text | 

## Example

```python
from revengai.models.update_rule_input_body import UpdateRuleInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuleInputBody from a JSON string
update_rule_input_body_instance = UpdateRuleInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateRuleInputBody.to_json())

# convert the object into a dict
update_rule_input_body_dict = update_rule_input_body_instance.to_dict()
# create an instance of UpdateRuleInputBody from a dict
update_rule_input_body_from_dict = UpdateRuleInputBody.from_dict(update_rule_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


