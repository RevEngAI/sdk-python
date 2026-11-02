# InvestigationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_type** | **str** |  | 
**created_at** | **datetime** |  | 
**investigation_id** | **int** |  | 
**name** | **str** |  | 
**owner_id** | **int** |  | 
**owner_username** | **str** |  | 
**scope** | **str** |  | 
**severity** | **str** |  | 
**status** | **str** |  | 
**team_id** | **int** | Team the investigation belongs to; 0 when its owner had no team | 
**updated_at** | **datetime** |  | 

## Example

```python
from revengai.models.investigation_body import InvestigationBody

# TODO update the JSON string below
json = "{}"
# create an instance of InvestigationBody from a JSON string
investigation_body_instance = InvestigationBody.from_json(json)
# print the JSON string representation of the object
print(InvestigationBody.to_json())

# convert the object into a dict
investigation_body_dict = investigation_body_instance.to_dict()
# create an instance of InvestigationBody from a dict
investigation_body_from_dict = InvestigationBody.from_dict(investigation_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


