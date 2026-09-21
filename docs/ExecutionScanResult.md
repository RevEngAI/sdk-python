# ExecutionScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the run was performed against | 
**findings** | [**List[ExecutionFinding]**](ExecutionFinding.md) | Functions with execution-related evidence, sorted by whether they execute code, then confidence, then evidence count | [optional] 
**total_functions** | **int** | Functions the run considered | 

## Example

```python
from revengai.models.execution_scan_result import ExecutionScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionScanResult from a JSON string
execution_scan_result_instance = ExecutionScanResult.from_json(json)
# print the JSON string representation of the object
print(ExecutionScanResult.to_json())

# convert the object into a dict
execution_scan_result_dict = execution_scan_result_instance.to_dict()
# create an instance of ExecutionScanResult from a dict
execution_scan_result_from_dict = ExecutionScanResult.from_dict(execution_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


