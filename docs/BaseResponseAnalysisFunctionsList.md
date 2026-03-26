# BaseResponseAnalysisFunctionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnalysisFunctionsList**](AnalysisFunctionsList.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_analysis_functions_list import BaseResponseAnalysisFunctionsList

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseAnalysisFunctionsList from a JSON string
base_response_analysis_functions_list_instance = BaseResponseAnalysisFunctionsList.from_json(json)
# print the JSON string representation of the object
print(BaseResponseAnalysisFunctionsList.to_json())

# convert the object into a dict
base_response_analysis_functions_list_dict = base_response_analysis_functions_list_instance.to_dict()
# create an instance of BaseResponseAnalysisFunctionsList from a dict
base_response_analysis_functions_list_from_dict = BaseResponseAnalysisFunctionsList.from_dict(base_response_analysis_functions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


