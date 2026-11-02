# CreateConversationInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Scopes the conversation to one of the investigation&#39;s analyses. Omit it to cover the whole investigation. | [optional] 
**title** | **str** | A title for the conversation. When empty, one is generated from the first message. | [optional] 

## Example

```python
from revengai.models.create_conversation_input_body import CreateConversationInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConversationInputBody from a JSON string
create_conversation_input_body_instance = CreateConversationInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateConversationInputBody.to_json())

# convert the object into a dict
create_conversation_input_body_dict = create_conversation_input_body_instance.to_dict()
# create an instance of CreateConversationInputBody from a dict
create_conversation_input_body_from_dict = CreateConversationInputBody.from_dict(create_conversation_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


