# FilesystemAnalyseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this function. | 

## Example

```python
from revengai.models.filesystem_analyse_metadata import FilesystemAnalyseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemAnalyseMetadata from a JSON string
filesystem_analyse_metadata_instance = FilesystemAnalyseMetadata.from_json(json)
# print the JSON string representation of the object
print(FilesystemAnalyseMetadata.to_json())

# convert the object into a dict
filesystem_analyse_metadata_dict = filesystem_analyse_metadata_instance.to_dict()
# create an instance of FilesystemAnalyseMetadata from a dict
filesystem_analyse_metadata_from_dict = FilesystemAnalyseMetadata.from_dict(filesystem_analyse_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


