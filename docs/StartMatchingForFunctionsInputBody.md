# StartMatchingForFunctionsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**MatchFilters**](MatchFilters.md) | Narrow the candidate pool. | [optional] 
**function_ids** | **List[int]** | Source function IDs to match against the rest of the corpus. | 
**min_similarity** | **float** | Similarity floor as a percentage. Defaults to 90. | [optional] 
**results_per_function** | **int** | Max matches returned per source function. Defaults to 1. | [optional] 
**use_canonical_names** | **bool** | Collapse near-duplicate candidate names into canonical buckets and return per-name confidences (the response &#39;confidences&#39; array). Adds a canonicalisation step; defaults to false. | [optional] 

## Example

```python
from revengai.models.start_matching_for_functions_input_body import StartMatchingForFunctionsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of StartMatchingForFunctionsInputBody from a JSON string
start_matching_for_functions_input_body_instance = StartMatchingForFunctionsInputBody.from_json(json)
# print the JSON string representation of the object
print(StartMatchingForFunctionsInputBody.to_json())

# convert the object into a dict
start_matching_for_functions_input_body_dict = start_matching_for_functions_input_body_instance.to_dict()
# create an instance of StartMatchingForFunctionsInputBody from a dict
start_matching_for_functions_input_body_from_dict = StartMatchingForFunctionsInputBody.from_dict(start_matching_for_functions_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


