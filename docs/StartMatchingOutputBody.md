# StartMatchingOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[ProgressMessage]**](ProgressMessage.md) | Log messages emitted during execution | 
**status** | **str** | Current workflow status | 
**step** | **str** | Name of the current step | 
**step_index** | **int** | Zero-based index of the current step | 
**steps_total** | **int** | Total number of steps in the workflow | 

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


