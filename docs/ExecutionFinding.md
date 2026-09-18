# ExecutionFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Function&#39;s virtual address, hex-encoded | 
**categories** | **List[str]** | Distinct execution categories evidenced by this function | 
**confidence** | **str** | High when a direct name match was found, medium when the function only calls into execution APIs | 
**direct_matches** | [**List[ExecutionDirectMatch]**](ExecutionDirectMatch.md) | Matches against the function&#39;s own name | [optional] 
**evidence_count** | **int** | Total number of direct matches and execution calls | 
**executes** | **bool** | Whether this function evidences executing code rather than only supporting it | 
**execution_calls** | [**List[ExecutionCall]**](ExecutionCall.md) | Matches against names this function calls | [optional] 
**function_id** | **int** | ID of the function the finding was reported in | 
**function_name** | **str** | Name of the function the finding was reported in | 
**function_size** | **int** | Size of the function in bytes | 
**sources** | **List[str]** | Distinct execution sources evidenced by this function | 

## Example

```python
from revengai.models.execution_finding import ExecutionFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionFinding from a JSON string
execution_finding_instance = ExecutionFinding.from_json(json)
# print the JSON string representation of the object
print(ExecutionFinding.to_json())

# convert the object into a dict
execution_finding_dict = execution_finding_instance.to_dict()
# create an instance of ExecutionFinding from a dict
execution_finding_from_dict = ExecutionFinding.from_dict(execution_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


