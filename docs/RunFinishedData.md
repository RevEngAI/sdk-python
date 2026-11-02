# RunFinishedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** |  | [optional] 
**definition_name** | **str** |  | [optional] 
**input_tokens** | **int** |  | [optional] 
**output_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 

## Example

```python
from revengai.models.run_finished_data import RunFinishedData

# TODO update the JSON string below
json = "{}"
# create an instance of RunFinishedData from a JSON string
run_finished_data_instance = RunFinishedData.from_json(json)
# print the JSON string representation of the object
print(RunFinishedData.to_json())

# convert the object into a dict
run_finished_data_dict = run_finished_data_instance.to_dict()
# create an instance of RunFinishedData from a dict
run_finished_data_from_dict = RunFinishedData.from_dict(run_finished_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


