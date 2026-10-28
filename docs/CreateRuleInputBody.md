# CreateRuleInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**name** | **str** |  | 
**source** | **str** | YARA rule source text | 

## Example

```python
from revengai.models.create_rule_input_body import CreateRuleInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRuleInputBody from a JSON string
create_rule_input_body_instance = CreateRuleInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateRuleInputBody.to_json())

# convert the object into a dict
create_rule_input_body_dict = create_rule_input_body_instance.to_dict()
# create an instance of CreateRuleInputBody from a dict
create_rule_input_body_from_dict = CreateRuleInputBody.from_dict(create_rule_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


