# FilesystemScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the run was performed against | 
**findings** | [**List[FilesystemFinding]**](FilesystemFinding.md) | Functions with filesystem-related evidence, sorted by whether they modify the filesystem, then confidence, then evidence count | [optional] 
**total_functions** | **int** | Functions the run considered | 

## Example

```python
from revengai.models.filesystem_scan_result import FilesystemScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemScanResult from a JSON string
filesystem_scan_result_instance = FilesystemScanResult.from_json(json)
# print the JSON string representation of the object
print(FilesystemScanResult.to_json())

# convert the object into a dict
filesystem_scan_result_dict = filesystem_scan_result_instance.to_dict()
# create an instance of FilesystemScanResult from a dict
filesystem_scan_result_from_dict = FilesystemScanResult.from_dict(filesystem_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


