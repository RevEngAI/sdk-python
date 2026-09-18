# ExecutionExplainResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** | Whether the run was cancelled | 
**code_origin** | **str** | Where the executed code originates from | [optional] 
**executed_targets** | **List[str]** | Concrete targets that end up executed -- process names, module paths, or shellcode buffers | [optional] 
**function_id** | **int** | ID of the explained function | 
**function_name** | **str** | Name of the explained function | [optional] 
**functions_involved** | [**List[ExecutionExplainedFunction]**](ExecutionExplainedFunction.md) | Other functions involved in the code execution | [optional] 
**purpose** | **str** | Purpose of the code execution | [optional] 
**summary** | **str** | Explanation of the code execution the function performs | [optional] 
**trigger** | **str** | What triggers the execution | [optional] 
**what_executes** | **str** | What code ends up executing | [optional] 

## Example

```python
from revengai.models.execution_explain_result import ExecutionExplainResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionExplainResult from a JSON string
execution_explain_result_instance = ExecutionExplainResult.from_json(json)
# print the JSON string representation of the object
print(ExecutionExplainResult.to_json())

# convert the object into a dict
execution_explain_result_dict = execution_explain_result_instance.to_dict()
# create an instance of ExecutionExplainResult from a dict
execution_explain_result_from_dict = ExecutionExplainResult.from_dict(execution_explain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


