# SandboxConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_entry_path** | **str** |  | [optional] 
**archive_password** | **str** |  | [optional] 
**archive_sha_256_hash** | **str** |  | [optional] 
**command_line_args** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**start_method** | **str** |  | [optional] 
**timeout** | **int** |  | [optional] [default to 120]

## Example

```python
from revengai.models.sandbox_config import SandboxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxConfig from a JSON string
sandbox_config_instance = SandboxConfig.from_json(json)
# print the JSON string representation of the object
print(SandboxConfig.to_json())

# convert the object into a dict
sandbox_config_dict = sandbox_config_instance.to_dict()
# create an instance of SandboxConfig from a dict
sandbox_config_from_dict = SandboxConfig.from_dict(sandbox_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


