# ConversationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | The analysis the conversation is about. Null when it is about the whole investigation. | 
**conversation_uuid** | **str** | Use with the /v2/conversations endpoints to read, stream and send messages. | 
**created_at** | **datetime** |  | 
**investigation_id** | **int** |  | 
**starter_id** | **int** | The user who started the conversation, and the only one who can send messages in it. | 
**starter_username** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** | When the conversation was last active: its newest message or event, or a change such as a new title. | 

## Example

```python
from revengai.models.conversation_body import ConversationBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationBody from a JSON string
conversation_body_instance = ConversationBody.from_json(json)
# print the JSON string representation of the object
print(ConversationBody.to_json())

# convert the object into a dict
conversation_body_dict = conversation_body_instance.to_dict()
# create an instance of ConversationBody from a dict
conversation_body_from_dict = ConversationBody.from_dict(conversation_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


