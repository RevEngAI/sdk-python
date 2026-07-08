# StartMatchingForAnalysisInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**MatchFilters**](MatchFilters.md) | Narrow the candidate pool. | [optional] 
**min_similarity** | **float** | Similarity floor as a percentage. Defaults to 90. | [optional] 
**no_cache** | **bool** | By default a completed matching run for the same request is reused (response status&#x3D;COMPLETED, no new run). Set true to force a fresh run. | [optional] 
**results_per_function** | **int** | Max matches returned per source function. Defaults to 1. | [optional] 

## Example

```python
from revengai.models.start_matching_for_analysis_input_body import StartMatchingForAnalysisInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of StartMatchingForAnalysisInputBody from a JSON string
start_matching_for_analysis_input_body_instance = StartMatchingForAnalysisInputBody.from_json(json)
# print the JSON string representation of the object
print(StartMatchingForAnalysisInputBody.to_json())

# convert the object into a dict
start_matching_for_analysis_input_body_dict = start_matching_for_analysis_input_body_instance.to_dict()
# create an instance of StartMatchingForAnalysisInputBody from a dict
start_matching_for_analysis_input_body_from_dict = StartMatchingForAnalysisInputBody.from_dict(start_matching_for_analysis_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


