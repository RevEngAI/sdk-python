# StepFinishedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_reason** | **str** |  | [optional] 
**step_index** | **int** |  | [optional] 

## Example

```python
from revengai.models.step_finished_data import StepFinishedData

# TODO update the JSON string below
json = "{}"
# create an instance of StepFinishedData from a JSON string
step_finished_data_instance = StepFinishedData.from_json(json)
# print the JSON string representation of the object
print(StepFinishedData.to_json())

# convert the object into a dict
step_finished_data_dict = step_finished_data_instance.to_dict()
# create an instance of StepFinishedData from a dict
step_finished_data_from_dict = StepFinishedData.from_dict(step_finished_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


