# OperationWorkflowProgressResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Whether the operation has reached a terminal state. | 
**error** | [**Status**](Status.md) | Failure detail, populated only when done is true and the operation failed. | [optional] 
**metadata** | [**WorkflowProgress**](WorkflowProgress.md) | In-flight information and details. | [optional] 
**name** | **str** | API resource name. | 
**response** | [**ResultBody**](ResultBody.md) | Result, set only when done is true and the operation succeeded. | [optional] 

## Example

```python
from revengai.models.operation_workflow_progress_result_body import OperationWorkflowProgressResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of OperationWorkflowProgressResultBody from a JSON string
operation_workflow_progress_result_body_instance = OperationWorkflowProgressResultBody.from_json(json)
# print the JSON string representation of the object
print(OperationWorkflowProgressResultBody.to_json())

# convert the object into a dict
operation_workflow_progress_result_body_dict = operation_workflow_progress_result_body_instance.to_dict()
# create an instance of OperationWorkflowProgressResultBody from a dict
operation_workflow_progress_result_body_from_dict = OperationWorkflowProgressResultBody.from_dict(operation_workflow_progress_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


