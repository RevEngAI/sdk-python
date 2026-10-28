# ContextCompactedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** |  | [optional] 
**messages_after** | **int** |  | [optional] 
**messages_before** | **int** |  | [optional] 
**removed_turns** | **int** |  | [optional] 
**strategy** | **str** |  | [optional] 

## Example

```python
from revengai.models.context_compacted_data import ContextCompactedData

# TODO update the JSON string below
json = "{}"
# create an instance of ContextCompactedData from a JSON string
context_compacted_data_instance = ContextCompactedData.from_json(json)
# print the JSON string representation of the object
print(ContextCompactedData.to_json())

# convert the object into a dict
context_compacted_data_dict = context_compacted_data_instance.to_dict()
# create an instance of ContextCompactedData from a dict
context_compacted_data_from_dict = ContextCompactedData.from_dict(context_compacted_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


