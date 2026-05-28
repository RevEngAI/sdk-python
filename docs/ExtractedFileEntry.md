# ExtractedFileEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_hash** | **str** |  | [optional] 
**file_size** | **int** |  | 
**file_type** | **str** |  | [optional] 
**filename** | **str** |  | 
**is_pe** | **bool** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**seq_num** | **int** |  | 
**sha256** | **str** |  | [optional] 
**zip_filename** | **str** |  | 

## Example

```python
from revengai.models.extracted_file_entry import ExtractedFileEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractedFileEntry from a JSON string
extracted_file_entry_instance = ExtractedFileEntry.from_json(json)
# print the JSON string representation of the object
print(ExtractedFileEntry.to_json())

# convert the object into a dict
extracted_file_entry_dict = extracted_file_entry_instance.to_dict()
# create an instance of ExtractedFileEntry from a dict
extracted_file_entry_from_dict = ExtractedFileEntry.from_dict(extracted_file_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


