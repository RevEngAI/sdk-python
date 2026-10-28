# ToolCallArgsDeltaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.tool_call_args_delta_data import ToolCallArgsDeltaData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallArgsDeltaData from a JSON string
tool_call_args_delta_data_instance = ToolCallArgsDeltaData.from_json(json)
# print the JSON string representation of the object
print(ToolCallArgsDeltaData.to_json())

# convert the object into a dict
tool_call_args_delta_data_dict = tool_call_args_delta_data_instance.to_dict()
# create an instance of ToolCallArgsDeltaData from a dict
tool_call_args_delta_data_from_dict = ToolCallArgsDeltaData.from_dict(tool_call_args_delta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


