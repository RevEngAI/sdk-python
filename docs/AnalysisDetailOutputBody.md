# AnalysisDetailOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AnalysisAccessBody**](AnalysisAccessBody.md) |  | 
**analysis_id** | **int** |  | 
**analysis_scope** | **str** |  | 
**architecture** | **str** |  | 
**auto_run_agents** | [**AutoRunAgentsBody**](AutoRunAgentsBody.md) |  | 
**binary_dynamic** | **bool** |  | 
**binary_format** | **str** |  | 
**binary_name** | **str** |  | 
**binary_size** | **int** |  | 
**binary_type** | **str** |  | 
**capability_count** | **int** | Number of capabilities in the latest capabilities agent result. Null when the agent has not produced a result | 
**creation** | **str** |  | 
**dashboard_url** | **str** | URL to view this analysis in the dashboard | 
**debug** | **bool** |  | 
**model_name** | **str** |  | 
**requested_config** | [**RequestedConfigBody**](RequestedConfigBody.md) | Snapshot of the configuration the analysis was submitted with | 
**security_finding_count** | **int** | Number of HIGH or CRITICAL findings in the latest security scan. Null when the scan has not produced a result | 
**sha_256_hash** | **str** |  | 
**threat_score** | **float** | Software threat score from the latest triage result, from 0 to 1. Null when triage has not produced a result | 

## Example

```python
from revengai.models.analysis_detail_output_body import AnalysisDetailOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisDetailOutputBody from a JSON string
analysis_detail_output_body_instance = AnalysisDetailOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisDetailOutputBody.to_json())

# convert the object into a dict
analysis_detail_output_body_dict = analysis_detail_output_body_instance.to_dict()
# create an instance of AnalysisDetailOutputBody from a dict
analysis_detail_output_body_from_dict = AnalysisDetailOutputBody.from_dict(analysis_detail_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


