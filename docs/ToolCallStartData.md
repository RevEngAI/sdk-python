# ToolCallStartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_args** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 
**tool_name** | **str** |  | [optional] 

## Example

```python
from revengai.models.tool_call_start_data import ToolCallStartData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallStartData from a JSON string
tool_call_start_data_instance = ToolCallStartData.from_json(json)
# print the JSON string representation of the object
print(ToolCallStartData.to_json())

# convert the object into a dict
tool_call_start_data_dict = tool_call_start_data_instance.to_dict()
# create an instance of ToolCallStartData from a dict
tool_call_start_data_from_dict = ToolCallStartData.from_dict(tool_call_start_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


