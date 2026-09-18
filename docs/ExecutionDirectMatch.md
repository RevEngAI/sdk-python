# ExecutionDirectMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Execution category of the match | 
**how** | **str** | Detection tier that produced the match | 
**matched_name** | **str** | Name or token that matched | 
**source** | **str** | Execution source the match belongs to | 

## Example

```python
from revengai.models.execution_direct_match import ExecutionDirectMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDirectMatch from a JSON string
execution_direct_match_instance = ExecutionDirectMatch.from_json(json)
# print the JSON string representation of the object
print(ExecutionDirectMatch.to_json())

# convert the object into a dict
execution_direct_match_dict = execution_direct_match_instance.to_dict()
# create an instance of ExecutionDirectMatch from a dict
execution_direct_match_from_dict = ExecutionDirectMatch.from_dict(execution_direct_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


