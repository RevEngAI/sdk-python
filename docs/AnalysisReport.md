# AnalysisReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_activity** | [**List[FileActivityEntry]**](FileActivityEntry.md) |  | [optional] 
**info** | [**ReportInfo**](ReportInfo.md) |  | 
**memdumps** | [**List[ProcessMemdumps]**](ProcessMemdumps.md) |  | [optional] 
**module_load_addresses** | [**List[ModuleLoadEntry]**](ModuleLoadEntry.md) |  | [optional] 
**mutexes** | [**List[MutexEntry]**](MutexEntry.md) |  | [optional] 
**network_activity** | [**NetworkActivity**](NetworkActivity.md) |  | [optional] 
**process_activity** | [**List[ProcessActivityEntry]**](ProcessActivityEntry.md) |  | [optional] 
**process_tree** | [**ProcessTree**](ProcessTree.md) |  | [optional] 
**registry_operations** | [**List[RegistryOperation]**](RegistryOperation.md) |  | [optional] 
**scheduled_tasks** | [**List[ScheduledTaskEntry]**](ScheduledTaskEntry.md) |  | [optional] 
**services** | [**List[ServiceEntry]**](ServiceEntry.md) |  | [optional] 
**startup** | [**StartupInfo**](StartupInfo.md) |  | [optional] 
**threat_score** | **int** |  | 
**ttps** | [**List[Ttp]**](Ttp.md) |  | [optional] 

## Example

```python
from revengai.models.analysis_report import AnalysisReport

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReport from a JSON string
analysis_report_instance = AnalysisReport.from_json(json)
# print the JSON string representation of the object
print(AnalysisReport.to_json())

# convert the object into a dict
analysis_report_dict = analysis_report_instance.to_dict()
# create an instance of AnalysisReport from a dict
analysis_report_from_dict = AnalysisReport.from_dict(analysis_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


