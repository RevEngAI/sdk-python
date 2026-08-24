# AnalysisLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Severity | 
**source** | **str** | Component that emitted the line | 
**text** | **str** | Log line text | 
**timestamp** | **datetime** | When the line was emitted (UTC) | 

## Example

```python
from revengai.models.analysis_log_entry import AnalysisLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisLogEntry from a JSON string
analysis_log_entry_instance = AnalysisLogEntry.from_json(json)
# print the JSON string representation of the object
print(AnalysisLogEntry.to_json())

# convert the object into a dict
analysis_log_entry_dict = analysis_log_entry_instance.to_dict()
# create an instance of AnalysisLogEntry from a dict
analysis_log_entry_from_dict = AnalysisLogEntry.from_dict(analysis_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


