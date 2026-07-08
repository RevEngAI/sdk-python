# ListImportedFunctionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported_functions** | [**List[ImportedFunctionEntry]**](ImportedFunctionEntry.md) |  | 
**total_count** | **int** | Total imported functions for the binary, ignoring pagination. | 

## Example

```python
from revengai.models.list_imported_functions_output_body import ListImportedFunctionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListImportedFunctionsOutputBody from a JSON string
list_imported_functions_output_body_instance = ListImportedFunctionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListImportedFunctionsOutputBody.to_json())

# convert the object into a dict
list_imported_functions_output_body_dict = list_imported_functions_output_body_instance.to_dict()
# create an instance of ListImportedFunctionsOutputBody from a dict
list_imported_functions_output_body_from_dict = ListImportedFunctionsOutputBody.from_dict(list_imported_functions_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


