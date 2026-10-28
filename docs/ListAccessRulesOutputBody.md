# ListAccessRulesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[AccessRuleBody]**](AccessRuleBody.md) | Every user and team the analysis is shared with, oldest first | 

## Example

```python
from revengai.models.list_access_rules_output_body import ListAccessRulesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccessRulesOutputBody from a JSON string
list_access_rules_output_body_instance = ListAccessRulesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAccessRulesOutputBody.to_json())

# convert the object into a dict
list_access_rules_output_body_dict = list_access_rules_output_body_instance.to_dict()
# create an instance of ListAccessRulesOutputBody from a dict
list_access_rules_output_body_from_dict = ListAccessRulesOutputBody.from_dict(list_access_rules_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


