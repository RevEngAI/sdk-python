# ToolCallResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_error** | **bool** |  | [optional] 
**result** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 
**tool_name** | **str** |  | [optional] 
**updated** | [**List[EntityUpdate]**](EntityUpdate.md) |  | [optional] 

## Example

```python
from revengai.models.tool_call_result_data import ToolCallResultData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallResultData from a JSON string
tool_call_result_data_instance = ToolCallResultData.from_json(json)
# print the JSON string representation of the object
print(ToolCallResultData.to_json())

# convert the object into a dict
tool_call_result_data_dict = tool_call_result_data_instance.to_dict()
# create an instance of ToolCallResultData from a dict
tool_call_result_data_from_dict = ToolCallResultData.from_dict(tool_call_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


