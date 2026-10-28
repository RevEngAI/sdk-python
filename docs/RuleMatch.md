# RuleMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**namespace** | **str** |  | [optional] 
**patterns** | [**List[PatternMatch]**](PatternMatch.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from revengai.models.rule_match import RuleMatch

# TODO update the JSON string below
json = "{}"
# create an instance of RuleMatch from a JSON string
rule_match_instance = RuleMatch.from_json(json)
# print the JSON string representation of the object
print(RuleMatch.to_json())

# convert the object into a dict
rule_match_dict = rule_match_instance.to_dict()
# create an instance of RuleMatch from a dict
rule_match_from_dict = RuleMatch.from_dict(rule_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


