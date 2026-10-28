# ListRulesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**rules** | [**List[Rule]**](Rule.md) |  | 

## Example

```python
from revengai.models.list_rules_output_body import ListRulesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListRulesOutputBody from a JSON string
list_rules_output_body_instance = ListRulesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListRulesOutputBody.to_json())

# convert the object into a dict
list_rules_output_body_dict = list_rules_output_body_instance.to_dict()
# create an instance of ListRulesOutputBody from a dict
list_rules_output_body_from_dict = ListRulesOutputBody.from_dict(list_rules_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


