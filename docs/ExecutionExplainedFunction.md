# ExecutionExplainedFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Role this function plays in the code execution | 
**function_id** | **int** | ID of the function | 
**function_name** | **str** | Name of the function | 

## Example

```python
from revengai.models.execution_explained_function import ExecutionExplainedFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionExplainedFunction from a JSON string
execution_explained_function_instance = ExecutionExplainedFunction.from_json(json)
# print the JSON string representation of the object
print(ExecutionExplainedFunction.to_json())

# convert the object into a dict
execution_explained_function_dict = execution_explained_function_instance.to_dict()
# create an instance of ExecutionExplainedFunction from a dict
execution_explained_function_from_dict = ExecutionExplainedFunction.from_dict(execution_explained_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


