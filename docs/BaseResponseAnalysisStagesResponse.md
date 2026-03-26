# BaseResponseAnalysisStagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnalysisStagesResponse**](AnalysisStagesResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_analysis_stages_response import BaseResponseAnalysisStagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseAnalysisStagesResponse from a JSON string
base_response_analysis_stages_response_instance = BaseResponseAnalysisStagesResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseAnalysisStagesResponse.to_json())

# convert the object into a dict
base_response_analysis_stages_response_dict = base_response_analysis_stages_response_instance.to_dict()
# create an instance of BaseResponseAnalysisStagesResponse from a dict
base_response_analysis_stages_response_from_dict = BaseResponseAnalysisStagesResponse.from_dict(base_response_analysis_stages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


