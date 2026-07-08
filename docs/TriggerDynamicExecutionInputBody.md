# TriggerDynamicExecutionInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_entry_path** | **str** | Relative path of the entry inside the archive to execute | [optional] 
**archive_password** | **str** | Password for an encrypted archive | [optional] 
**archive_sha_256_hash** | **str** | SHA-256 of the archive object to send to the sandbox instead of the analysed binary | [optional] 
**command_line_args** | **str** | Command-line arguments passed to the sample when the sandbox launches it | [optional] 
**start_method** | **str** | How the sandbox launches the sample. Defaults to the sandbox&#39;s standard behaviour when omitted. | [optional] 
**timeout** | **int** | Maximum sandbox execution time in seconds | [optional] [default to 120]

## Example

```python
from revengai.models.trigger_dynamic_execution_input_body import TriggerDynamicExecutionInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDynamicExecutionInputBody from a JSON string
trigger_dynamic_execution_input_body_instance = TriggerDynamicExecutionInputBody.from_json(json)
# print the JSON string representation of the object
print(TriggerDynamicExecutionInputBody.to_json())

# convert the object into a dict
trigger_dynamic_execution_input_body_dict = trigger_dynamic_execution_input_body_instance.to_dict()
# create an instance of TriggerDynamicExecutionInputBody from a dict
trigger_dynamic_execution_input_body_from_dict = TriggerDynamicExecutionInputBody.from_dict(trigger_dynamic_execution_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


