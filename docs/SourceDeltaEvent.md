# SourceDeltaEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**content** | **str** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.source_delta_event import SourceDeltaEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDeltaEvent from a JSON string
source_delta_event_instance = SourceDeltaEvent.from_json(json)
# print the JSON string representation of the object
print(SourceDeltaEvent.to_json())

# convert the object into a dict
source_delta_event_dict = source_delta_event_instance.to_dict()
# create an instance of SourceDeltaEvent from a dict
source_delta_event_from_dict = SourceDeltaEvent.from_dict(source_delta_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


