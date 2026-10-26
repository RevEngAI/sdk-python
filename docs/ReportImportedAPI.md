# ReportImportedAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | Name of the API. | 
**module** | **str** | Module the API is imported from, or null when unknown. | 

## Example

```python
from revengai.models.report_imported_api import ReportImportedAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ReportImportedAPI from a JSON string
report_imported_api_instance = ReportImportedAPI.from_json(json)
# print the JSON string representation of the object
print(ReportImportedAPI.to_json())

# convert the object into a dict
report_imported_api_dict = report_imported_api_instance.to_dict()
# create an instance of ReportImportedAPI from a dict
report_imported_api_from_dict = ReportImportedAPI.from_dict(report_imported_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


