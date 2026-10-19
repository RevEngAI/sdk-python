# ReportImportedAPICall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported_api** | [**ReportImportedAPI**](ReportImportedAPI.md) | The API called. | 
**reachability** | [**ReportCallChain**](ReportCallChain.md) | A call chain reaching the call, absent when none was found. | [optional] 
**subject** | [**ReportSubject**](ReportSubject.md) | Where the call is made. | 

## Example

```python
from revengai.models.report_imported_api_call import ReportImportedAPICall

# TODO update the JSON string below
json = "{}"
# create an instance of ReportImportedAPICall from a JSON string
report_imported_api_call_instance = ReportImportedAPICall.from_json(json)
# print the JSON string representation of the object
print(ReportImportedAPICall.to_json())

# convert the object into a dict
report_imported_api_call_dict = report_imported_api_call_instance.to_dict()
# create an instance of ReportImportedAPICall from a dict
report_imported_api_call_from_dict = ReportImportedAPICall.from_dict(report_imported_api_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


