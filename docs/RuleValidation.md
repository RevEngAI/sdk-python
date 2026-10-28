# RuleValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Diagnostic]**](Diagnostic.md) |  | 
**name** | **str** |  | 
**ok** | **bool** | True when the rule compiled with no errors | 
**warnings** | [**List[Diagnostic]**](Diagnostic.md) |  | 

## Example

```python
from revengai.models.rule_validation import RuleValidation

# TODO update the JSON string below
json = "{}"
# create an instance of RuleValidation from a JSON string
rule_validation_instance = RuleValidation.from_json(json)
# print the JSON string representation of the object
print(RuleValidation.to_json())

# convert the object into a dict
rule_validation_dict = rule_validation_instance.to_dict()
# create an instance of RuleValidation from a dict
rule_validation_from_dict = RuleValidation.from_dict(rule_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


