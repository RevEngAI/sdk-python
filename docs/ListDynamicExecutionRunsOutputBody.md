# ListDynamicExecutionRunsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runs** | [**List[DynamicExecutionRun]**](DynamicExecutionRun.md) | The analysis&#39;s runs, newest first | 

## Example

```python
from revengai.models.list_dynamic_execution_runs_output_body import ListDynamicExecutionRunsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListDynamicExecutionRunsOutputBody from a JSON string
list_dynamic_execution_runs_output_body_instance = ListDynamicExecutionRunsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListDynamicExecutionRunsOutputBody.to_json())

# convert the object into a dict
list_dynamic_execution_runs_output_body_dict = list_dynamic_execution_runs_output_body_instance.to_dict()
# create an instance of ListDynamicExecutionRunsOutputBody from a dict
list_dynamic_execution_runs_output_body_from_dict = ListDynamicExecutionRunsOutputBody.from_dict(list_dynamic_execution_runs_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


