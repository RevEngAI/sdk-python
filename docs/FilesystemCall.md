# FilesystemCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_name** | **str** | Name of the called function | 
**category** | **str** | Filesystem category of the match | 
**how** | **str** | Detection tier that produced the match | 
**matched_name** | **str** | Name or token that matched | 
**source** | **str** | Filesystem source the match belongs to | 

## Example

```python
from revengai.models.filesystem_call import FilesystemCall

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemCall from a JSON string
filesystem_call_instance = FilesystemCall.from_json(json)
# print the JSON string representation of the object
print(FilesystemCall.to_json())

# convert the object into a dict
filesystem_call_dict = filesystem_call_instance.to_dict()
# create an instance of FilesystemCall from a dict
filesystem_call_from_dict = FilesystemCall.from_dict(filesystem_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


