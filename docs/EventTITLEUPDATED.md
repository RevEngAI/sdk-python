# EventTITLEUPDATED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventTitleUpdatedData**](SseEventTitleUpdatedData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_titleupdated import EventTITLEUPDATED

# TODO update the JSON string below
json = "{}"
# create an instance of EventTITLEUPDATED from a JSON string
event_titleupdated_instance = EventTITLEUPDATED.from_json(json)
# print the JSON string representation of the object
print(EventTITLEUPDATED.to_json())

# convert the object into a dict
event_titleupdated_dict = event_titleupdated_instance.to_dict()
# create an instance of EventTITLEUPDATED from a dict
event_titleupdated_from_dict = EventTITLEUPDATED.from_dict(event_titleupdated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


