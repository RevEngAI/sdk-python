# TypesSuggestedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**members** | **int** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 
**types** | **int** |  | 

## Example

```python
from revengai.models.types_suggested_event import TypesSuggestedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TypesSuggestedEvent from a JSON string
types_suggested_event_instance = TypesSuggestedEvent.from_json(json)
# print the JSON string representation of the object
print(TypesSuggestedEvent.to_json())

# convert the object into a dict
types_suggested_event_dict = types_suggested_event_instance.to_dict()
# create an instance of TypesSuggestedEvent from a dict
types_suggested_event_from_dict = TypesSuggestedEvent.from_dict(types_suggested_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


