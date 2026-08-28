# NamesFinishedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **int** |  | 
**attempt** | **int** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.names_finished_event import NamesFinishedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NamesFinishedEvent from a JSON string
names_finished_event_instance = NamesFinishedEvent.from_json(json)
# print the JSON string representation of the object
print(NamesFinishedEvent.to_json())

# convert the object into a dict
names_finished_event_dict = names_finished_event_instance.to_dict()
# create an instance of NamesFinishedEvent from a dict
names_finished_event_from_dict = NamesFinishedEvent.from_dict(names_finished_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


