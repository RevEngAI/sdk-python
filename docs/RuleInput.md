# RuleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Caller-chosen label used to attribute diagnostics | [optional] 
**source** | **str** | YARA rule source text | 

## Example

```python
from revengai.models.rule_input import RuleInput

# TODO update the JSON string below
json = "{}"
# create an instance of RuleInput from a JSON string
rule_input_instance = RuleInput.from_json(json)
# print the JSON string representation of the object
print(RuleInput.to_json())

# convert the object into a dict
rule_input_dict = rule_input_instance.to_dict()
# create an instance of RuleInput from a dict
rule_input_from_dict = RuleInput.from_dict(rule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


