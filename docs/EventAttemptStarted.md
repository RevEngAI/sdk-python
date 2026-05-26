# EventAttemptStarted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttemptStartedEvent**](AttemptStartedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_attempt_started import EventAttemptStarted

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttemptStarted from a JSON string
event_attempt_started_instance = EventAttemptStarted.from_json(json)
# print the JSON string representation of the object
print(EventAttemptStarted.to_json())

# convert the object into a dict
event_attempt_started_dict = event_attempt_started_instance.to_dict()
# create an instance of EventAttemptStarted from a dict
event_attempt_started_from_dict = EventAttemptStarted.from_dict(event_attempt_started_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


