# DecompFinishedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**seq** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from revengai.models.decomp_finished_event import DecompFinishedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DecompFinishedEvent from a JSON string
decomp_finished_event_instance = DecompFinishedEvent.from_json(json)
# print the JSON string representation of the object
print(DecompFinishedEvent.to_json())

# convert the object into a dict
decomp_finished_event_dict = decomp_finished_event_instance.to_dict()
# create an instance of DecompFinishedEvent from a dict
decomp_finished_event_from_dict = DecompFinishedEvent.from_dict(decomp_finished_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


