# ListConversationsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**results** | [**List[ConversationBody]**](ConversationBody.md) |  | 
**total_count** | **int** | Conversations in the investigation across all pages. | 

## Example

```python
from revengai.models.list_conversations_output_body import ListConversationsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListConversationsOutputBody from a JSON string
list_conversations_output_body_instance = ListConversationsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListConversationsOutputBody.to_json())

# convert the object into a dict
list_conversations_output_body_dict = list_conversations_output_body_instance.to_dict()
# create an instance of ListConversationsOutputBody from a dict
list_conversations_output_body_from_dict = ListConversationsOutputBody.from_dict(list_conversations_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


