# AttemptFailedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**error** | **str** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.attempt_failed_event import AttemptFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AttemptFailedEvent from a JSON string
attempt_failed_event_instance = AttemptFailedEvent.from_json(json)
# print the JSON string representation of the object
print(AttemptFailedEvent.to_json())

# convert the object into a dict
attempt_failed_event_dict = attempt_failed_event_instance.to_dict()
# create an instance of AttemptFailedEvent from a dict
attempt_failed_event_from_dict = AttemptFailedEvent.from_dict(attempt_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


