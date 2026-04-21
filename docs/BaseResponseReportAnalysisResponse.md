# BaseResponseReportAnalysisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]
**data** | [**ReportAnalysisResponse**](ReportAnalysisResponse.md) |  | [optional] 
**message** | **str** |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 

## Example

```python
from revengai.models.base_response_report_analysis_response import BaseResponseReportAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseReportAnalysisResponse from a JSON string
base_response_report_analysis_response_instance = BaseResponseReportAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseReportAnalysisResponse.to_json())

# convert the object into a dict
base_response_report_analysis_response_dict = base_response_report_analysis_response_instance.to_dict()
# create an instance of BaseResponseReportAnalysisResponse from a dict
base_response_report_analysis_response_from_dict = BaseResponseReportAnalysisResponse.from_dict(base_response_report_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


