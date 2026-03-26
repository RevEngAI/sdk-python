# BaseResponseAnalysisCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnalysisCreateResponse**](AnalysisCreateResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_analysis_create_response import BaseResponseAnalysisCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseAnalysisCreateResponse from a JSON string
base_response_analysis_create_response_instance = BaseResponseAnalysisCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseAnalysisCreateResponse.to_json())

# convert the object into a dict
base_response_analysis_create_response_dict = base_response_analysis_create_response_instance.to_dict()
# create an instance of BaseResponseAnalysisCreateResponse from a dict
base_response_analysis_create_response_from_dict = BaseResponseAnalysisCreateResponse.from_dict(base_response_analysis_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


