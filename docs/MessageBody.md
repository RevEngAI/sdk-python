# MessageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable status message | 

## Example

```python
from revengai.models.message_body import MessageBody

# TODO update the JSON string below
json = "{}"
# create an instance of MessageBody from a JSON string
message_body_instance = MessageBody.from_json(json)
# print the JSON string representation of the object
print(MessageBody.to_json())

# convert the object into a dict
message_body_dict = message_body_instance.to_dict()
# create an instance of MessageBody from a dict
message_body_from_dict = MessageBody.from_dict(message_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


