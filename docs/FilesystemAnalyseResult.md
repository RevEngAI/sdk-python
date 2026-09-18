# FilesystemAnalyseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** | Whether the run was cancelled | 
**data_description** | **str** | Description of the data read or written | [optional] 
**data_destination** | **str** | Where the data ends up | [optional] 
**data_origin** | **str** | Where the data originates from | [optional] 
**function_id** | **int** | ID of the explained function | 
**function_name** | **str** | Name of the explained function | [optional] 
**functions_involved** | [**List[FilesystemExplainedFunction]**](FilesystemExplainedFunction.md) | Other functions involved in the filesystem access | [optional] 
**summary** | **str** | Explanation of the filesystem access the function performs | [optional] 
**targets** | **List[str]** | Concrete filesystem targets identified -- paths, registry keys, or environment variables | [optional] 

## Example

```python
from revengai.models.filesystem_analyse_result import FilesystemAnalyseResult

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemAnalyseResult from a JSON string
filesystem_analyse_result_instance = FilesystemAnalyseResult.from_json(json)
# print the JSON string representation of the object
print(FilesystemAnalyseResult.to_json())

# convert the object into a dict
filesystem_analyse_result_dict = filesystem_analyse_result_instance.to_dict()
# create an instance of FilesystemAnalyseResult from a dict
filesystem_analyse_result_from_dict = FilesystemAnalyseResult.from_dict(filesystem_analyse_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


