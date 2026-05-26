# WarningEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**identifiers** | **List[str]** |  | [optional] 
**kind** | **str** |  | 
**message** | **str** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.warning_event import WarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WarningEvent from a JSON string
warning_event_instance = WarningEvent.from_json(json)
# print the JSON string representation of the object
print(WarningEvent.to_json())

# convert the object into a dict
warning_event_dict = warning_event_instance.to_dict()
# create an instance of WarningEvent from a dict
warning_event_from_dict = WarningEvent.from_dict(warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


