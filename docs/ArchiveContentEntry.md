# ArchiveContentEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted** | **bool** | Whether this entry is password-protected | 
**path** | **str** | Path relative to the archive root | 
**size** | **int** | Uncompressed size in bytes | 

## Example

```python
from revengai.models.archive_content_entry import ArchiveContentEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveContentEntry from a JSON string
archive_content_entry_instance = ArchiveContentEntry.from_json(json)
# print the JSON string representation of the object
print(ArchiveContentEntry.to_json())

# convert the object into a dict
archive_content_entry_dict = archive_content_entry_instance.to_dict()
# create an instance of ArchiveContentEntry from a dict
archive_content_entry_from_dict = ArchiveContentEntry.from_dict(archive_content_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


