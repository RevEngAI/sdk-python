# ConfirmToolInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Whether the user approves the pending tool call. | 

## Example

```python
from revengai.models.confirm_tool_input_body import ConfirmToolInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmToolInputBody from a JSON string
confirm_tool_input_body_instance = ConfirmToolInputBody.from_json(json)
# print the JSON string representation of the object
print(ConfirmToolInputBody.to_json())

# convert the object into a dict
confirm_tool_input_body_dict = confirm_tool_input_body_instance.to_dict()
# create an instance of ConfirmToolInputBody from a dict
confirm_tool_input_body_from_dict = ConfirmToolInputBody.from_dict(confirm_tool_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


