# ProcessActivityEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** |  | [optional] 
**child_seqid** | **int** |  | 
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**exit_code** | **int** |  | [optional] 
**exit_code_str** | **str** |  | [optional] 
**name** | **str** |  | 
**pid** | **int** |  | 

## Example

```python
from revengai.models.process_activity_entry import ProcessActivityEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessActivityEntry from a JSON string
process_activity_entry_instance = ProcessActivityEntry.from_json(json)
# print the JSON string representation of the object
print(ProcessActivityEntry.to_json())

# convert the object into a dict
process_activity_entry_dict = process_activity_entry_instance.to_dict()
# create an instance of ProcessActivityEntry from a dict
process_activity_entry_from_dict = ProcessActivityEntry.from_dict(process_activity_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


