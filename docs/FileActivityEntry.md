# FileActivityEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**path** | **str** |  | 

## Example

```python
from revengai.models.file_activity_entry import FileActivityEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FileActivityEntry from a JSON string
file_activity_entry_instance = FileActivityEntry.from_json(json)
# print the JSON string representation of the object
print(FileActivityEntry.to_json())

# convert the object into a dict
file_activity_entry_dict = file_activity_entry_instance.to_dict()
# create an instance of FileActivityEntry from a dict
file_activity_entry_from_dict = FileActivityEntry.from_dict(file_activity_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


