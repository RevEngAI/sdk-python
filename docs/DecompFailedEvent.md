# DecompFailedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**error** | **str** |  | 
**error_code** | **str** |  | [optional] 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.decomp_failed_event import DecompFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DecompFailedEvent from a JSON string
decomp_failed_event_instance = DecompFailedEvent.from_json(json)
# print the JSON string representation of the object
print(DecompFailedEvent.to_json())

# convert the object into a dict
decomp_failed_event_dict = decomp_failed_event_instance.to_dict()
# create an instance of DecompFailedEvent from a dict
decomp_failed_event_from_dict = DecompFailedEvent.from_dict(decomp_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


