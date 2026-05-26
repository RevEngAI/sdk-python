# AttemptStartedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.attempt_started_event import AttemptStartedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AttemptStartedEvent from a JSON string
attempt_started_event_instance = AttemptStartedEvent.from_json(json)
# print the JSON string representation of the object
print(AttemptStartedEvent.to_json())

# convert the object into a dict
attempt_started_event_dict = attempt_started_event_instance.to_dict()
# create an instance of AttemptStartedEvent from a dict
attempt_started_event_from_dict = AttemptStartedEvent.from_dict(attempt_started_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


