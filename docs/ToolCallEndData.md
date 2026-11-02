# ToolCallEndData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_call_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.tool_call_end_data import ToolCallEndData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallEndData from a JSON string
tool_call_end_data_instance = ToolCallEndData.from_json(json)
# print the JSON string representation of the object
print(ToolCallEndData.to_json())

# convert the object into a dict
tool_call_end_data_dict = tool_call_end_data_instance.to_dict()
# create an instance of ToolCallEndData from a dict
tool_call_end_data_from_dict = ToolCallEndData.from_dict(tool_call_end_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


