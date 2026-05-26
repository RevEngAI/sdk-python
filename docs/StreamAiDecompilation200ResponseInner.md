# StreamAiDecompilation200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WarningEvent**](WarningEvent.md) |  | 
**event** | **str** | The event name. | 
**id** | **int** | The event ID. | [optional] 
**retry** | **int** | The retry time in milliseconds. | [optional] 

## Example

```python
from revengai.models.stream_ai_decompilation200_response_inner import StreamAiDecompilation200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAiDecompilation200ResponseInner from a JSON string
stream_ai_decompilation200_response_inner_instance = StreamAiDecompilation200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(StreamAiDecompilation200ResponseInner.to_json())

# convert the object into a dict
stream_ai_decompilation200_response_inner_dict = stream_ai_decompilation200_response_inner_instance.to_dict()
# create an instance of StreamAiDecompilation200ResponseInner from a dict
stream_ai_decompilation200_response_inner_from_dict = StreamAiDecompilation200ResponseInner.from_dict(stream_ai_decompilation200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


