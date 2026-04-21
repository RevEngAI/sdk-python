# QueuedWorkflowTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 

## Example

```python
from revengai.models.queued_workflow_task_response import QueuedWorkflowTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedWorkflowTaskResponse from a JSON string
queued_workflow_task_response_instance = QueuedWorkflowTaskResponse.from_json(json)
# print the JSON string representation of the object
print(QueuedWorkflowTaskResponse.to_json())

# convert the object into a dict
queued_workflow_task_response_dict = queued_workflow_task_response_instance.to_dict()
# create an instance of QueuedWorkflowTaskResponse from a dict
queued_workflow_task_response_from_dict = QueuedWorkflowTaskResponse.from_dict(queued_workflow_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


