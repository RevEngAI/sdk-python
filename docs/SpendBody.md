# SpendBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** | The conversation of a CHAT spend. | 
**created_at** | **datetime** |  | 
**credits** | **float** |  | 
**source** | **str** | What the credits were spent on: a conversation turn or an agent run started from the investigation. | 
**spend_id** | **int** |  | 
**task_id** | **str** | The agent run of an AGENT_RUN spend. | 
**user_id** | **int** | Who was charged. Zero when that user has been deleted. | 
**username** | **str** |  | 

## Example

```python
from revengai.models.spend_body import SpendBody

# TODO update the JSON string below
json = "{}"
# create an instance of SpendBody from a JSON string
spend_body_instance = SpendBody.from_json(json)
# print the JSON string representation of the object
print(SpendBody.to_json())

# convert the object into a dict
spend_body_dict = spend_body_instance.to_dict()
# create an instance of SpendBody from a dict
spend_body_from_dict = SpendBody.from_dict(spend_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


