# DynamicExecutionRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**DynamicExecutionRunConfig**](DynamicExecutionRunConfig.md) | Parameters the run was started with | 
**created_at** | **datetime** | When the run was started | 
**id** | **str** | Run ID | 
**status** | **str** | Run status | 

## Example

```python
from revengai.models.dynamic_execution_run import DynamicExecutionRun

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionRun from a JSON string
dynamic_execution_run_instance = DynamicExecutionRun.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionRun.to_json())

# convert the object into a dict
dynamic_execution_run_dict = dynamic_execution_run_instance.to_dict()
# create an instance of DynamicExecutionRun from a dict
dynamic_execution_run_from_dict = DynamicExecutionRun.from_dict(dynamic_execution_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


