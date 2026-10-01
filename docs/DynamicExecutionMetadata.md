# DynamicExecutionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**AnalysisLogs**](AnalysisLogs.md) | Sandbox status log messages captured during the run. Empty when none have been captured yet. | 
**status** | **str** | Run status. UNINITIALISED means this analysis has never had a run triggered. | 

## Example

```python
from revengai.models.dynamic_execution_metadata import DynamicExecutionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionMetadata from a JSON string
dynamic_execution_metadata_instance = DynamicExecutionMetadata.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionMetadata.to_json())

# convert the object into a dict
dynamic_execution_metadata_dict = dynamic_execution_metadata_instance.to_dict()
# create an instance of DynamicExecutionMetadata from a dict
dynamic_execution_metadata_from_dict = DynamicExecutionMetadata.from_dict(dynamic_execution_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


