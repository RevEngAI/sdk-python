# AccessRuleBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | VIEW lets the principal read the analysis; EDIT also lets them modify it | 
**team_id** | **int** | The team the rule applies to. Set for a team rule | [optional] 
**team_name** | **str** | The team&#39;s name. Set for a team rule | [optional] 
**user_id** | **int** | The user the rule applies to. Set for a user rule | [optional] 
**username** | **str** | The user&#39;s username. Set for a user rule | [optional] 

## Example

```python
from revengai.models.access_rule_body import AccessRuleBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRuleBody from a JSON string
access_rule_body_instance = AccessRuleBody.from_json(json)
# print the JSON string representation of the object
print(AccessRuleBody.to_json())

# convert the object into a dict
access_rule_body_dict = access_rule_body_instance.to_dict()
# create an instance of AccessRuleBody from a dict
access_rule_body_from_dict = AccessRuleBody.from_dict(access_rule_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


