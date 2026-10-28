# ToolConfirmationRequiredData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**tool_args** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 
**tool_name** | **str** |  | [optional] 

## Example

```python
from revengai.models.tool_confirmation_required_data import ToolConfirmationRequiredData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfirmationRequiredData from a JSON string
tool_confirmation_required_data_instance = ToolConfirmationRequiredData.from_json(json)
# print the JSON string representation of the object
print(ToolConfirmationRequiredData.to_json())

# convert the object into a dict
tool_confirmation_required_data_dict = tool_confirmation_required_data_instance.to_dict()
# create an instance of ToolConfirmationRequiredData from a dict
tool_confirmation_required_data_from_dict = ToolConfirmationRequiredData.from_dict(tool_confirmation_required_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


