# ListArchiveContentsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ArchiveContentEntry]**](ArchiveContentEntry.md) | Files inside the archive, with paths relative to the archive root | 
**has_next** | **bool** | Whether a further page of entries follows this one. | 
**page** | **int** | Page number of this response (1-indexed). | 
**page_size** | **int** | Number of entries per page. | 
**total_count** | **int** | Total number of file entries in the archive, ignoring pagination. | 

## Example

```python
from revengai.models.list_archive_contents_output_body import ListArchiveContentsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListArchiveContentsOutputBody from a JSON string
list_archive_contents_output_body_instance = ListArchiveContentsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListArchiveContentsOutputBody.to_json())

# convert the object into a dict
list_archive_contents_output_body_dict = list_archive_contents_output_body_instance.to_dict()
# create an instance of ListArchiveContentsOutputBody from a dict
list_archive_contents_output_body_from_dict = ListArchiveContentsOutputBody.from_dict(list_archive_contents_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


