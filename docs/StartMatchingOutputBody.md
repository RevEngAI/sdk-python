# StartMatchingOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **str** | Opaque token for this matching run. Pass it to the GET/status endpoints&#39; match_id query parameter to fetch this exact run. | 
**messages** | [**List[ProgressMessage]**](ProgressMessage.md) | Log messages emitted during execution | 
**percent** | **int** | Overall completion as a percentage, weighted by step duration | 
**status** | **str** | Current workflow status | 
**step** | **str** | Name of the current step | 
**step_index** | **int** | Zero-based index of the current step | 
**step_share** | **int** | Percentage points the current step contributes when it completes | 
**steps_total** | **int** | Total number of steps in the workflow | 
**sub_step** | **str** | Phase within the current step, when the step reports one | [optional] 
**sub_step_done** | **int** | Items completed in the current phase | [optional] 
**sub_step_total** | **int** | Items the current phase will process, 0 when unknown | [optional] 

## Example

```python
from revengai.models.start_matching_output_body import StartMatchingOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of StartMatchingOutputBody from a JSON string
start_matching_output_body_instance = StartMatchingOutputBody.from_json(json)
# print the JSON string representation of the object
print(StartMatchingOutputBody.to_json())

# convert the object into a dict
start_matching_output_body_dict = start_matching_output_body_instance.to_dict()
# create an instance of StartMatchingOutputBody from a dict
start_matching_output_body_from_dict = StartMatchingOutputBody.from_dict(start_matching_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


