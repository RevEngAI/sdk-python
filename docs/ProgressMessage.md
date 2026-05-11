# ProgressMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Severity level | 
**step** | **str** | Step name when the message was emitted | 
**text** | **str** | Message text | 
**timestamp** | **datetime** | When the message was emitted | 

## Example

```python
from revengai.models.progress_message import ProgressMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressMessage from a JSON string
progress_message_instance = ProgressMessage.from_json(json)
# print the JSON string representation of the object
print(ProgressMessage.to_json())

# convert the object into a dict
progress_message_dict = progress_message_instance.to_dict()
# create an instance of ProgressMessage from a dict
progress_message_from_dict = ProgressMessage.from_dict(progress_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


