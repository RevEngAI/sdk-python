# Artifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**dump_addr** | **str** |  | [optional] 
**dump_pid** | **int** |  | [optional] 
**file_type** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**is_pe** | **bool** |  | 
**mime_type** | **str** |  | [optional] 
**name** | **str** |  | 
**network_source** | **str** |  | [optional] 
**original_filename** | **str** |  | [optional] 
**path** | **str** |  | 
**process_seqid** | **int** |  | [optional] 
**reason** | **str** |  | 
**response_status** | **int** |  | [optional] 
**sha256** | **str** |  | [optional] 
**size** | **int** |  | 
**source** | **str** |  | 
**uri** | **str** |  | [optional] 
**was_mapped** | **bool** |  | [optional] 
**yara_hits** | **List[str]** |  | [optional] 

## Example

```python
from revengai.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print(Artifact.to_json())

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_from_dict = Artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


