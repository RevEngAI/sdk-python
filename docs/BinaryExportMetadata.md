# BinaryExportMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis ID | 

## Example

```python
from revengai.models.binary_export_metadata import BinaryExportMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryExportMetadata from a JSON string
binary_export_metadata_instance = BinaryExportMetadata.from_json(json)
# print the JSON string representation of the object
print(BinaryExportMetadata.to_json())

# convert the object into a dict
binary_export_metadata_dict = binary_export_metadata_instance.to_dict()
# create an instance of BinaryExportMetadata from a dict
binary_export_metadata_from_dict = BinaryExportMetadata.from_dict(binary_export_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


