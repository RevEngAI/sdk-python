# BinaryExportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name to give the downloaded file | 

## Example

```python
from revengai.models.binary_export_result import BinaryExportResult

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryExportResult from a JSON string
binary_export_result_instance = BinaryExportResult.from_json(json)
# print the JSON string representation of the object
print(BinaryExportResult.to_json())

# convert the object into a dict
binary_export_result_dict = binary_export_result_instance.to_dict()
# create an instance of BinaryExportResult from a dict
binary_export_result_from_dict = BinaryExportResult.from_dict(binary_export_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


