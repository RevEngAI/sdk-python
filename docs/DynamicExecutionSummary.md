# DynamicExecutionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_at** | **datetime** | When the summary was generated | 
**summary** | **str** | Markdown summary of the run | 

## Example

```python
from revengai.models.dynamic_execution_summary import DynamicExecutionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionSummary from a JSON string
dynamic_execution_summary_instance = DynamicExecutionSummary.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionSummary.to_json())

# convert the object into a dict
dynamic_execution_summary_dict = dynamic_execution_summary_instance.to_dict()
# create an instance of DynamicExecutionSummary from a dict
dynamic_execution_summary_from_dict = DynamicExecutionSummary.from_dict(dynamic_execution_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


