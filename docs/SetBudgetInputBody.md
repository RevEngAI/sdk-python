# SetBudgetInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_budget** | **int** | The most credits the investigation may spend, up to 1,000,000,000, or null to remove the limit. | 

## Example

```python
from revengai.models.set_budget_input_body import SetBudgetInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetBudgetInputBody from a JSON string
set_budget_input_body_instance = SetBudgetInputBody.from_json(json)
# print the JSON string representation of the object
print(SetBudgetInputBody.to_json())

# convert the object into a dict
set_budget_input_body_dict = set_budget_input_body_instance.to_dict()
# create an instance of SetBudgetInputBody from a dict
set_budget_input_body_from_dict = SetBudgetInputBody.from_dict(set_budget_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


