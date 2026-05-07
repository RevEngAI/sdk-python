# ReportEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_calls** | [**List[ApiCall]**](ApiCall.md) |  | [optional] 
**process_seqid** | **int** |  | [optional] 
**total_bytes_requested** | **int** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | [optional] 
**value_name** | **str** |  | [optional] 
**write_count** | **int** |  | [optional] 

## Example

```python
from revengai.models.report_event import ReportEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEvent from a JSON string
report_event_instance = ReportEvent.from_json(json)
# print the JSON string representation of the object
print(ReportEvent.to_json())

# convert the object into a dict
report_event_dict = report_event_instance.to_dict()
# create an instance of ReportEvent from a dict
report_event_from_dict = ReportEvent.from_dict(report_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


