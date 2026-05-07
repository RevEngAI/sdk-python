# MutexEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from revengai.models.mutex_entry import MutexEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MutexEntry from a JSON string
mutex_entry_instance = MutexEntry.from_json(json)
# print the JSON string representation of the object
print(MutexEntry.to_json())

# convert the object into a dict
mutex_entry_dict = mutex_entry_instance.to_dict()
# create an instance of MutexEntry from a dict
mutex_entry_from_dict = MutexEntry.from_dict(mutex_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


