# DrakvufFileMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** |  | [optional] 
**name** | **str** |  | 
**sha256** | **str** |  | 
**type** | **str** |  | [optional] 
**type_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.drakvuf_file_metadata import DrakvufFileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DrakvufFileMetadata from a JSON string
drakvuf_file_metadata_instance = DrakvufFileMetadata.from_json(json)
# print the JSON string representation of the object
print(DrakvufFileMetadata.to_json())

# convert the object into a dict
drakvuf_file_metadata_dict = drakvuf_file_metadata_instance.to_dict()
# create an instance of DrakvufFileMetadata from a dict
drakvuf_file_metadata_from_dict = DrakvufFileMetadata.from_dict(drakvuf_file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


