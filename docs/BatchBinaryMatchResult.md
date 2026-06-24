# BatchBinaryMatchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_id** | **int** | Target binary | 
**error_message** | **str** | Error description when status&#x3D;FAILED. | [optional] 
**matched_function_count** | **int** | Number of source functions that received at least one candidate match. Only meaningful when status&#x3D;COMPLETED. | 
**status** | **str** | Per-binary workflow status | 

## Example

```python
from revengai.models.batch_binary_match_result import BatchBinaryMatchResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchBinaryMatchResult from a JSON string
batch_binary_match_result_instance = BatchBinaryMatchResult.from_json(json)
# print the JSON string representation of the object
print(BatchBinaryMatchResult.to_json())

# convert the object into a dict
batch_binary_match_result_dict = batch_binary_match_result_instance.to_dict()
# create an instance of BatchBinaryMatchResult from a dict
batch_binary_match_result_from_dict = BatchBinaryMatchResult.from_dict(batch_binary_match_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


