# BudgetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_budget** | **int** | The most credits the investigation may spend. Null when it has no limit. | 
**credits_spent** | **float** | Credits spent on the investigation&#39;s conversations and the agents run from it. | 
**spent** | **bool** | Whether the budget is spent, so nothing more that consumes credits can be started from the investigation. | 

## Example

```python
from revengai.models.budget_body import BudgetBody

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetBody from a JSON string
budget_body_instance = BudgetBody.from_json(json)
# print the JSON string representation of the object
print(BudgetBody.to_json())

# convert the object into a dict
budget_body_dict = budget_body_instance.to_dict()
# create an instance of BudgetBody from a dict
budget_body_from_dict = BudgetBody.from_dict(budget_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


