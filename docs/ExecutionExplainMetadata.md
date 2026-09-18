# ExecutionExplainMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this function. | 

## Example

```python
from revengai.models.execution_explain_metadata import ExecutionExplainMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionExplainMetadata from a JSON string
execution_explain_metadata_instance = ExecutionExplainMetadata.from_json(json)
# print the JSON string representation of the object
print(ExecutionExplainMetadata.to_json())

# convert the object into a dict
execution_explain_metadata_dict = execution_explain_metadata_instance.to_dict()
# create an instance of ExecutionExplainMetadata from a dict
execution_explain_metadata_from_dict = ExecutionExplainMetadata.from_dict(execution_explain_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


