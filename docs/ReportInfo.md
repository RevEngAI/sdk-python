# ReportInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**DrakvufFileMetadata**](DrakvufFileMetadata.md) |  | [optional] 
**id** | **str** |  | 
**options** | [**ReportOptions**](ReportOptions.md) |  | [optional] 
**os_profile** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time_analysis_finished** | **str** |  | [optional] 
**time_execution_started** | **str** |  | [optional] 
**time_started** | **str** |  | [optional] 

## Example

```python
from revengai.models.report_info import ReportInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReportInfo from a JSON string
report_info_instance = ReportInfo.from_json(json)
# print the JSON string representation of the object
print(ReportInfo.to_json())

# convert the object into a dict
report_info_dict = report_info_instance.to_dict()
# create an instance of ReportInfo from a dict
report_info_from_dict = ReportInfo.from_dict(report_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


