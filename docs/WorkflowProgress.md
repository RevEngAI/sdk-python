# WorkflowProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**messages** | [**List[ProgressMessage]**](ProgressMessage.md) | Log messages emitted during execution | 
**status** | **str** | Current workflow status | 
**step** | **str** | Name of the current step | 
**step_index** | **int** | Zero-based index of the current step | 
**steps_total** | **int** | Total number of steps in the workflow | 

## Example

```python
from revengai.models.workflow_progress import WorkflowProgress

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowProgress from a JSON string
workflow_progress_instance = WorkflowProgress.from_json(json)
# print the JSON string representation of the object
print(WorkflowProgress.to_json())

# convert the object into a dict
workflow_progress_dict = workflow_progress_instance.to_dict()
# create an instance of WorkflowProgress from a dict
workflow_progress_from_dict = WorkflowProgress.from_dict(workflow_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


