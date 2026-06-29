# AnalysisConfigSnapshot

Point-in-time record of which features an analysis was submitted with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | **bool** |  | 
**sandbox** | **bool** |  | 
**scrape** | **bool** |  | 
**capabilities** | **bool** |  | 
**triage** | **bool** |  | 

## Example

```python
from revengai.models.analysis_config_snapshot import AnalysisConfigSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisConfigSnapshot from a JSON string
analysis_config_snapshot_instance = AnalysisConfigSnapshot.from_json(json)
# print the JSON string representation of the object
print(AnalysisConfigSnapshot.to_json())

# convert the object into a dict
analysis_config_snapshot_dict = analysis_config_snapshot_instance.to_dict()
# create an instance of AnalysisConfigSnapshot from a dict
analysis_config_snapshot_from_dict = AnalysisConfigSnapshot.from_dict(analysis_config_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


