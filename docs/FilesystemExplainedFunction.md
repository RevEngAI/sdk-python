# FilesystemExplainedFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Role this function plays in the filesystem access | 
**function_id** | **int** | ID of the function | 
**function_name** | **str** | Name of the function | 

## Example

```python
from revengai.models.filesystem_explained_function import FilesystemExplainedFunction

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemExplainedFunction from a JSON string
filesystem_explained_function_instance = FilesystemExplainedFunction.from_json(json)
# print the JSON string representation of the object
print(FilesystemExplainedFunction.to_json())

# convert the object into a dict
filesystem_explained_function_dict = filesystem_explained_function_instance.to_dict()
# create an instance of FilesystemExplainedFunction from a dict
filesystem_explained_function_from_dict = FilesystemExplainedFunction.from_dict(filesystem_explained_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


