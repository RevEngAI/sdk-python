# ConversationWithEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**conversation_uuid** | **str** |  | 
**created_at** | **datetime** |  | 
**events** | [**List[Event]**](Event.md) |  | 
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


