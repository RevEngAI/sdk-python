# ImportDynamicExecutionFileOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_extract** | **bool** | Whether the firmware/extraction flow can accept this file. | 
**can_sandbox** | **bool** | Whether the file can be extracted and run in the Windows sandbox. | 
**is_archive** | **bool** | Whether the detected format is a container/compression archive. | 
**mime** | **str** | The MIME type detected from the file&#39;s contents. | 
**sha_256_hash** | **str** | SHA-256 hash the file is stored under; the storage key for every subsequent reference to it. | 
**size** | **int** | Size of the file in bytes. | 

## Example

```python
from revengai.models.import_dynamic_execution_file_output_body import ImportDynamicExecutionFileOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDynamicExecutionFileOutputBody from a JSON string
import_dynamic_execution_file_output_body_instance = ImportDynamicExecutionFileOutputBody.from_json(json)
# print the JSON string representation of the object
print(ImportDynamicExecutionFileOutputBody.to_json())

# convert the object into a dict
import_dynamic_execution_file_output_body_dict = import_dynamic_execution_file_output_body_instance.to_dict()
# create an instance of ImportDynamicExecutionFileOutputBody from a dict
import_dynamic_execution_file_output_body_from_dict = ImportDynamicExecutionFileOutputBody.from_dict(import_dynamic_execution_file_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


