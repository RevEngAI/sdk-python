# RenameAppliedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr_hex** | **str** |  | [optional] 
**attempt** | **int** |  | 
**new_name** | **str** |  | 
**old_name** | **str** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.rename_applied_event import RenameAppliedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RenameAppliedEvent from a JSON string
rename_applied_event_instance = RenameAppliedEvent.from_json(json)
# print the JSON string representation of the object
print(RenameAppliedEvent.to_json())

# convert the object into a dict
rename_applied_event_dict = rename_applied_event_instance.to_dict()
# create an instance of RenameAppliedEvent from a dict
rename_applied_event_from_dict = RenameAppliedEvent.from_dict(rename_applied_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


