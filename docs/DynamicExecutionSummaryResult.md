# DynamicExecutionSummaryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary_available** | **bool** | Whether the summary can be fetched from the summary endpoint. Always true when the operation succeeded. | 

## Example

```python
from revengai.models.dynamic_execution_summary_result import DynamicExecutionSummaryResult

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionSummaryResult from a JSON string
dynamic_execution_summary_result_instance = DynamicExecutionSummaryResult.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionSummaryResult.to_json())

# convert the object into a dict
dynamic_execution_summary_result_dict = dynamic_execution_summary_result_instance.to_dict()
# create an instance of DynamicExecutionSummaryResult from a dict
dynamic_execution_summary_result_from_dict = DynamicExecutionSummaryResult.from_dict(dynamic_execution_summary_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


