# ExecutionCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_name** | **str** | Name of the called function | 
**category** | **str** | Execution category of the match | 
**how** | **str** | Detection tier that produced the match | 
**matched_name** | **str** | Name or token that matched | 
**source** | **str** | Execution source the match belongs to | 

## Example

```python
from revengai.models.execution_call import ExecutionCall

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionCall from a JSON string
execution_call_instance = ExecutionCall.from_json(json)
# print the JSON string representation of the object
print(ExecutionCall.to_json())

# convert the object into a dict
execution_call_dict = execution_call_instance.to_dict()
# create an instance of ExecutionCall from a dict
execution_call_from_dict = ExecutionCall.from_dict(execution_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


