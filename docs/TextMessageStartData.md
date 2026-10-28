# TextMessageStartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.text_message_start_data import TextMessageStartData

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessageStartData from a JSON string
text_message_start_data_instance = TextMessageStartData.from_json(json)
# print the JSON string representation of the object
print(TextMessageStartData.to_json())

# convert the object into a dict
text_message_start_data_dict = text_message_start_data_instance.to_dict()
# create an instance of TextMessageStartData from a dict
text_message_start_data_from_dict = TextMessageStartData.from_dict(text_message_start_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


