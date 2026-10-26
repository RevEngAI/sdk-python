# DynamicExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_available** | **bool** | Whether the run&#39;s report can be fetched from the report endpoint. Always true when the operation succeeded. | 

## Example

```python
from revengai.models.dynamic_execution_result import DynamicExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionResult from a JSON string
dynamic_execution_result_instance = DynamicExecutionResult.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionResult.to_json())

# convert the object into a dict
dynamic_execution_result_dict = dynamic_execution_result_instance.to_dict()
# create an instance of DynamicExecutionResult from a dict
dynamic_execution_result_from_dict = DynamicExecutionResult.from_dict(dynamic_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


