# ProseEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**seq** | **int** |  | 
**text** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.prose_event import ProseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProseEvent from a JSON string
prose_event_instance = ProseEvent.from_json(json)
# print the JSON string representation of the object
print(ProseEvent.to_json())

# convert the object into a dict
prose_event_dict = prose_event_instance.to_dict()
# create an instance of ProseEvent from a dict
prose_event_from_dict = ProseEvent.from_dict(prose_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


