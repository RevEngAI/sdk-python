# DynamicExecutionSummaryMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the most recent summary attempt. UNINITIALISED means no summary has been attempted for this analysis. | 

## Example

```python
from revengai.models.dynamic_execution_summary_metadata import DynamicExecutionSummaryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionSummaryMetadata from a JSON string
dynamic_execution_summary_metadata_instance = DynamicExecutionSummaryMetadata.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionSummaryMetadata.to_json())

# convert the object into a dict
dynamic_execution_summary_metadata_dict = dynamic_execution_summary_metadata_instance.to_dict()
# create an instance of DynamicExecutionSummaryMetadata from a dict
dynamic_execution_summary_metadata_from_dict = DynamicExecutionSummaryMetadata.from_dict(dynamic_execution_summary_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


