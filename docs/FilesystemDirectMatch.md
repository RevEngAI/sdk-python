# FilesystemDirectMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Filesystem category of the match | 
**how** | **str** | Detection tier that produced the match | 
**matched_name** | **str** | Name or token that matched | 
**source** | **str** | Filesystem source the match belongs to | 

## Example

```python
from revengai.models.filesystem_direct_match import FilesystemDirectMatch

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemDirectMatch from a JSON string
filesystem_direct_match_instance = FilesystemDirectMatch.from_json(json)
# print the JSON string representation of the object
print(FilesystemDirectMatch.to_json())

# convert the object into a dict
filesystem_direct_match_dict = filesystem_direct_match_instance.to_dict()
# create an instance of FilesystemDirectMatch from a dict
filesystem_direct_match_from_dict = FilesystemDirectMatch.from_dict(filesystem_direct_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


