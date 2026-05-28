# ProcessExtractedFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ExtractedFileEntry]**](ExtractedFileEntry.md) |  | [optional] 
**process_seqid** | **int** |  | 

## Example

```python
from revengai.models.process_extracted_files import ProcessExtractedFiles

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessExtractedFiles from a JSON string
process_extracted_files_instance = ProcessExtractedFiles.from_json(json)
# print the JSON string representation of the object
print(ProcessExtractedFiles.to_json())

# convert the object into a dict
process_extracted_files_dict = process_extracted_files_instance.to_dict()
# create an instance of ProcessExtractedFiles from a dict
process_extracted_files_from_dict = ProcessExtractedFiles.from_dict(process_extracted_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


