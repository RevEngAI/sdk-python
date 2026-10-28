# ToolCallProgressData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.tool_call_progress_data import ToolCallProgressData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallProgressData from a JSON string
tool_call_progress_data_instance = ToolCallProgressData.from_json(json)
# print the JSON string representation of the object
print(ToolCallProgressData.to_json())

# convert the object into a dict
tool_call_progress_data_dict = tool_call_progress_data_instance.to_dict()
# create an instance of ToolCallProgressData from a dict
tool_call_progress_data_from_dict = ToolCallProgressData.from_dict(tool_call_progress_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


