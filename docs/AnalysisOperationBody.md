# AnalysisOperationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Resource name of the operation, polled at /v3/{name} | 
**operation** | **str** | Operation slug, the collection the operation is polled under | 
**status** | **str** | Status of the operation&#39;s latest run | 

## Example

```python
from revengai.models.analysis_operation_body import AnalysisOperationBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisOperationBody from a JSON string
analysis_operation_body_instance = AnalysisOperationBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisOperationBody.to_json())

# convert the object into a dict
analysis_operation_body_dict = analysis_operation_body_instance.to_dict()
# create an instance of AnalysisOperationBody from a dict
analysis_operation_body_from_dict = AnalysisOperationBody.from_dict(analysis_operation_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


