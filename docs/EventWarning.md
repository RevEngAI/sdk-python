# EventWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WarningEvent**](WarningEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_warning import EventWarning

# TODO update the JSON string below
json = "{}"
# create an instance of EventWarning from a JSON string
event_warning_instance = EventWarning.from_json(json)
# print the JSON string representation of the object
print(EventWarning.to_json())

# convert the object into a dict
event_warning_dict = event_warning_instance.to_dict()
# create an instance of EventWarning from a dict
event_warning_from_dict = EventWarning.from_dict(event_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


