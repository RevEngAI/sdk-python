# StartBatchMatchingInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_ids** | **List[int]** | Binary IDs to match the analysis against, one workflow per binary. | 
**debug_types** | **List[Optional[str]]** | Restrict matches to candidates with these debug source types. Defaults to [\&quot;SYSTEM\&quot;]. | [optional] 
**min_similarity** | **float** | Similarity floor as a percentage. Defaults to 90. | [optional] 
**results_per_function** | **int** | Max matches returned per source function. Defaults to 1. | [optional] 

## Example

```python
from revengai.models.start_batch_matching_input_body import StartBatchMatchingInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of StartBatchMatchingInputBody from a JSON string
start_batch_matching_input_body_instance = StartBatchMatchingInputBody.from_json(json)
# print the JSON string representation of the object
print(StartBatchMatchingInputBody.to_json())

# convert the object into a dict
start_batch_matching_input_body_dict = start_batch_matching_input_body_instance.to_dict()
# create an instance of StartBatchMatchingInputBody from a dict
start_batch_matching_input_body_from_dict = StartBatchMatchingInputBody.from_dict(start_batch_matching_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


