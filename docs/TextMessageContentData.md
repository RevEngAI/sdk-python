# TextMessageContentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.text_message_content_data import TextMessageContentData

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessageContentData from a JSON string
text_message_content_data_instance = TextMessageContentData.from_json(json)
# print the JSON string representation of the object
print(TextMessageContentData.to_json())

# convert the object into a dict
text_message_content_data_dict = text_message_content_data_instance.to_dict()
# create an instance of TextMessageContentData from a dict
text_message_content_data_from_dict = TextMessageContentData.from_dict(text_message_content_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


