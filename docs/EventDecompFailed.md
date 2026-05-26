# EventDecompFailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DecompFailedEvent**](DecompFailedEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.event_decomp_failed import EventDecompFailed

# TODO update the JSON string below
json = "{}"
# create an instance of EventDecompFailed from a JSON string
event_decomp_failed_instance = EventDecompFailed.from_json(json)
# print the JSON string representation of the object
print(EventDecompFailed.to_json())

# convert the object into a dict
event_decomp_failed_dict = event_decomp_failed_instance.to_dict()
# create an instance of EventDecompFailed from a dict
event_decomp_failed_from_dict = EventDecompFailed.from_dict(event_decomp_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


