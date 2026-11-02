# InvestigationListItemBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**BudgetBody**](BudgetBody.md) |  | 
**case_type** | **str** |  | 
**created_at** | **datetime** |  | 
**investigation_id** | **int** |  | 
**name** | **str** |  | 
**owner_id** | **int** |  | 
**owner_username** | **str** |  | 
**rollup** | [**RollupBody**](RollupBody.md) |  | 
**scope** | **str** |  | 
**severity** | **str** |  | 
**status** | **str** |  | 
**team_id** | **int** | Team the investigation belongs to; 0 when its owner had no team | 
**updated_at** | **datetime** |  | 

## Example

```python
from revengai.models.investigation_list_item_body import InvestigationListItemBody

# TODO update the JSON string below
json = "{}"
# create an instance of InvestigationListItemBody from a JSON string
investigation_list_item_body_instance = InvestigationListItemBody.from_json(json)
# print the JSON string representation of the object
print(InvestigationListItemBody.to_json())

# convert the object into a dict
investigation_list_item_body_dict = investigation_list_item_body_instance.to_dict()
# create an instance of InvestigationListItemBody from a dict
investigation_list_item_body_from_dict = InvestigationListItemBody.from_dict(investigation_list_item_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


