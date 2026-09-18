# FilesystemFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Function&#39;s virtual address, hex-encoded | 
**categories** | **List[str]** | Distinct filesystem categories evidenced by this function | 
**confidence** | **str** | High when a direct name match was found, medium when the function only calls into filesystem APIs | 
**direct_matches** | [**List[FilesystemDirectMatch]**](FilesystemDirectMatch.md) | Matches against the function&#39;s own name | [optional] 
**evidence_count** | **int** | Total number of direct matches and filesystem calls | 
**filesystem_calls** | [**List[FilesystemCall]**](FilesystemCall.md) | Matches against names this function calls | [optional] 
**function_id** | **int** | ID of the function the finding was reported in | 
**function_name** | **str** | Name of the function the finding was reported in | 
**function_size** | **int** | Size of the function in bytes | 
**modifies** | **bool** | Whether this function evidences modifying the filesystem rather than only observing it | 
**sources** | **List[str]** | Distinct filesystem sources evidenced by this function | 

## Example

```python
from revengai.models.filesystem_finding import FilesystemFinding

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemFinding from a JSON string
filesystem_finding_instance = FilesystemFinding.from_json(json)
# print the JSON string representation of the object
print(FilesystemFinding.to_json())

# convert the object into a dict
filesystem_finding_dict = filesystem_finding_instance.to_dict()
# create an instance of FilesystemFinding from a dict
filesystem_finding_from_dict = FilesystemFinding.from_dict(filesystem_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


