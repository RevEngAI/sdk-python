# EventTOOLCONFIRMATIONREQUIRED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SseEventToolConfirmationRequiredData**](SseEventToolConfirmationRequiredData.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_toolconfirmationrequired import EventTOOLCONFIRMATIONREQUIRED

# TODO update the JSON string below
json = "{}"
# create an instance of EventTOOLCONFIRMATIONREQUIRED from a JSON string
event_toolconfirmationrequired_instance = EventTOOLCONFIRMATIONREQUIRED.from_json(json)
# print the JSON string representation of the object
print(EventTOOLCONFIRMATIONREQUIRED.to_json())

# convert the object into a dict
event_toolconfirmationrequired_dict = event_toolconfirmationrequired_instance.to_dict()
# create an instance of EventTOOLCONFIRMATIONREQUIRED from a dict
event_toolconfirmationrequired_from_dict = EventTOOLCONFIRMATIONREQUIRED.from_dict(event_toolconfirmationrequired_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


