# ImportedFunctionCallerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** |  | 
**function_name** | **str** |  | 
**function_vaddr** | **int** |  | 
**stub_vaddr** | **int** | The PLT/stub address this caller targets. | 

## Example

```python
from revengai.models.imported_function_caller_entry import ImportedFunctionCallerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedFunctionCallerEntry from a JSON string
imported_function_caller_entry_instance = ImportedFunctionCallerEntry.from_json(json)
# print the JSON string representation of the object
print(ImportedFunctionCallerEntry.to_json())

# convert the object into a dict
imported_function_caller_entry_dict = imported_function_caller_entry_instance.to_dict()
# create an instance of ImportedFunctionCallerEntry from a dict
imported_function_caller_entry_from_dict = ImportedFunctionCallerEntry.from_dict(imported_function_caller_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


