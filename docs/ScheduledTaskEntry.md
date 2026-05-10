# ScheduledTaskEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 
**day** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**executable** | **str** |  | [optional] 
**modifier** | **str** |  | [optional] 
**run_as** | **str** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**task_name** | **str** |  | [optional] 

## Example

```python
from revengai.models.scheduled_task_entry import ScheduledTaskEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskEntry from a JSON string
scheduled_task_entry_instance = ScheduledTaskEntry.from_json(json)
# print the JSON string representation of the object
print(ScheduledTaskEntry.to_json())

# convert the object into a dict
scheduled_task_entry_dict = scheduled_task_entry_instance.to_dict()
# create an instance of ScheduledTaskEntry from a dict
scheduled_task_entry_from_dict = ScheduledTaskEntry.from_dict(scheduled_task_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


