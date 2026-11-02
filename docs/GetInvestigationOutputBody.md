# GetInvestigationOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_ids** | **List[int]** | Analyses in the investigation that you are permitted to see. | 
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
from revengai.models.get_investigation_output_body import GetInvestigationOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvestigationOutputBody from a JSON string
get_investigation_output_body_instance = GetInvestigationOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetInvestigationOutputBody.to_json())

# convert the object into a dict
get_investigation_output_body_dict = get_investigation_output_body_instance.to_dict()
# create an instance of GetInvestigationOutputBody from a dict
get_investigation_output_body_from_dict = GetInvestigationOutputBody.from_dict(get_investigation_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


