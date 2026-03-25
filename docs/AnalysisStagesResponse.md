# AnalysisStagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[StageEvent]**](StageEvent.md) |  | 

## Example

```python
from revengai.models.analysis_stages_response import AnalysisStagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStagesResponse from a JSON string
analysis_stages_response_instance = AnalysisStagesResponse.from_json(json)
# print the JSON string representation of the object
print(AnalysisStagesResponse.to_json())

# convert the object into a dict
analysis_stages_response_dict = analysis_stages_response_instance.to_dict()
# create an instance of AnalysisStagesResponse from a dict
analysis_stages_response_from_dict = AnalysisStagesResponse.from_dict(analysis_stages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


