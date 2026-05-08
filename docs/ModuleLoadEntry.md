# ModuleLoadEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modules** | **Dict[str, str]** |  | [optional] 
**pid** | **int** |  | 
**process_name** | **str** |  | [optional] 
**process_seqid** | **int** |  | [optional] 

## Example

```python
from revengai.models.module_load_entry import ModuleLoadEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleLoadEntry from a JSON string
module_load_entry_instance = ModuleLoadEntry.from_json(json)
# print the JSON string representation of the object
print(ModuleLoadEntry.to_json())

# convert the object into a dict
module_load_entry_dict = module_load_entry_instance.to_dict()
# create an instance of ModuleLoadEntry from a dict
module_load_entry_from_dict = ModuleLoadEntry.from_dict(module_load_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


