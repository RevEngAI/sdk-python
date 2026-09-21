# GetConfigOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_decompiler_unsupported_languages** | **List[str]** | Source languages AI decompilation does not support | 
**max_file_size_bytes** | **int** | Largest binary the calling user may submit for analysis, in bytes | 

## Example

```python
from revengai.models.get_config_output_body import GetConfigOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigOutputBody from a JSON string
get_config_output_body_instance = GetConfigOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetConfigOutputBody.to_json())

# convert the object into a dict
get_config_output_body_dict = get_config_output_body_instance.to_dict()
# create an instance of GetConfigOutputBody from a dict
get_config_output_body_from_dict = GetConfigOutputBody.from_dict(get_config_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


