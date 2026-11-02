# ConversationWithEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConversationContext**](ConversationContext.md) | The analysis, and optionally the function, the conversation is about. Absent when it is about neither. | [optional] 
**conversation_uuid** | **str** |  | 
**created_at** | **datetime** |  | 
**events** | [**List[Event]**](Event.md) |  | 
**investigation_id** | **int** | The investigation the conversation belongs to. Absent for a conversation outside any investigation. | [optional] 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **int** |  | 

## Example

```python
from revengai.models.conversation_with_events import ConversationWithEvents

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationWithEvents from a JSON string
conversation_with_events_instance = ConversationWithEvents.from_json(json)
# print the JSON string representation of the object
print(ConversationWithEvents.to_json())

# convert the object into a dict
conversation_with_events_dict = conversation_with_events_instance.to_dict()
# create an instance of ConversationWithEvents from a dict
conversation_with_events_from_dict = ConversationWithEvents.from_dict(conversation_with_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


