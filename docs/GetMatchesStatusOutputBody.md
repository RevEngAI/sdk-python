# GetMatchesStatusOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from revengai.models.get_matches_status_output_body import GetMatchesStatusOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetMatchesStatusOutputBody from a JSON string
get_matches_status_output_body_instance = GetMatchesStatusOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetMatchesStatusOutputBody.to_json())

# convert the object into a dict
get_matches_status_output_body_dict = get_matches_status_output_body_instance.to_dict()
# create an instance of GetMatchesStatusOutputBody from a dict
get_matches_status_output_body_from_dict = GetMatchesStatusOutputBody.from_dict(get_matches_status_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


