# TypesAppliedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**seq** | **int** |  | 
**skipped** | **int** |  | 
**type** | **str** |  | 
**types** | **int** |  | 

## Example

```python
from revengai.models.types_applied_event import TypesAppliedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TypesAppliedEvent from a JSON string
types_applied_event_instance = TypesAppliedEvent.from_json(json)
# print the JSON string representation of the object
print(TypesAppliedEvent.to_json())

# convert the object into a dict
types_applied_event_dict = types_applied_event_instance.to_dict()
# create an instance of TypesAppliedEvent from a dict
types_applied_event_from_dict = TypesAppliedEvent.from_dict(types_applied_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


