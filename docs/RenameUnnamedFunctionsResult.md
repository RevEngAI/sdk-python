# RenameUnnamedFunctionsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the run was performed against | 
**failed** | **int** | Functions whose rename attempt errored | 
**renamed** | **int** | Functions successfully renamed | 
**skipped** | **int** | Functions the agent chose not to rename | 
**total** | **int** | Unnamed functions the run considered | 

## Example

```python
from revengai.models.rename_unnamed_functions_result import RenameUnnamedFunctionsResult

# TODO update the JSON string below
json = "{}"
# create an instance of RenameUnnamedFunctionsResult from a JSON string
rename_unnamed_functions_result_instance = RenameUnnamedFunctionsResult.from_json(json)
# print the JSON string representation of the object
print(RenameUnnamedFunctionsResult.to_json())

# convert the object into a dict
rename_unnamed_functions_result_dict = rename_unnamed_functions_result_instance.to_dict()
# create an instance of RenameUnnamedFunctionsResult from a dict
rename_unnamed_functions_result_from_dict = RenameUnnamedFunctionsResult.from_dict(rename_unnamed_functions_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


