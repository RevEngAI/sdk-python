# SourceResetEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.source_reset_event import SourceResetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SourceResetEvent from a JSON string
source_reset_event_instance = SourceResetEvent.from_json(json)
# print the JSON string representation of the object
print(SourceResetEvent.to_json())

# convert the object into a dict
source_reset_event_dict = source_reset_event_instance.to_dict()
# create an instance of SourceResetEvent from a dict
source_reset_event_from_dict = SourceResetEvent.from_dict(source_reset_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


