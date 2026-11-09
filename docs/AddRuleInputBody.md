# AddRuleInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**rule_id** | **int** |  | 
**version** | **int** | Pin to this version; omit (0) to follow the rule&#39;s current version | [optional] 

## Example

```python
from revengai.models.add_rule_input_body import AddRuleInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddRuleInputBody from a JSON string
add_rule_input_body_instance = AddRuleInputBody.from_json(json)
# print the JSON string representation of the object
print(AddRuleInputBody.to_json())

# convert the object into a dict
add_rule_input_body_dict = add_rule_input_body_instance.to_dict()
# create an instance of AddRuleInputBody from a dict
add_rule_input_body_from_dict = AddRuleInputBody.from_dict(add_rule_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


