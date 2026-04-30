# ConversationContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | [optional] 
**function_id** | **int** |  | [optional] 

## Example

```python
from revengai.models.conversation_context import ConversationContext

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationContext from a JSON string
conversation_context_instance = ConversationContext.from_json(json)
# print the JSON string representation of the object
print(ConversationContext.to_json())

# convert the object into a dict
conversation_context_dict = conversation_context_instance.to_dict()
# create an instance of ConversationContext from a dict
conversation_context_from_dict = ConversationContext.from_dict(conversation_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


