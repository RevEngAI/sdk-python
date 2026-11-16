# DynamicExecutionRunConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_entry_path** | **str** | Relative path of the archive entry executed. Empty when no archive was used. | 
**archive_sha_256_hash** | **str** | SHA-256 of the archive sent to the sandbox instead of the analysed binary. Empty when no archive was used. | 
**command_line_args** | **str** | Command-line arguments passed to the sample. Empty when none were given. | 
**has_archive_password** | **bool** | Whether a password was given for the archive. The password itself is never returned. | 
**start_method** | **str** | How the sandbox launched the sample. Null when the sandbox&#39;s standard behaviour was used. | 
**timeout_seconds** | **int** | Maximum sandbox execution time in seconds | 
**url** | **str** | URL opened in the sandbox&#39;s browser instead of a sample. Empty for a sample run. | 

## Example

```python
from revengai.models.dynamic_execution_run_config import DynamicExecutionRunConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionRunConfig from a JSON string
dynamic_execution_run_config_instance = DynamicExecutionRunConfig.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionRunConfig.to_json())

# convert the object into a dict
dynamic_execution_run_config_dict = dynamic_execution_run_config_instance.to_dict()
# create an instance of DynamicExecutionRunConfig from a dict
dynamic_execution_run_config_from_dict = DynamicExecutionRunConfig.from_dict(dynamic_execution_run_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


