# TriggerRenameUnnamedFunctionsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Stop after this many functions. Omit to process every unnamed function in the analysis. | [optional] 

## Example

```python
from revengai.models.trigger_rename_unnamed_functions_input_body import TriggerRenameUnnamedFunctionsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerRenameUnnamedFunctionsInputBody from a JSON string
trigger_rename_unnamed_functions_input_body_instance = TriggerRenameUnnamedFunctionsInputBody.from_json(json)
# print the JSON string representation of the object
print(TriggerRenameUnnamedFunctionsInputBody.to_json())

# convert the object into a dict
trigger_rename_unnamed_functions_input_body_dict = trigger_rename_unnamed_functions_input_body_instance.to_dict()
# create an instance of TriggerRenameUnnamedFunctionsInputBody from a dict
trigger_rename_unnamed_functions_input_body_from_dict = TriggerRenameUnnamedFunctionsInputBody.from_dict(trigger_rename_unnamed_functions_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


