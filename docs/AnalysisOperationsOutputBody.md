# AnalysisOperationsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[AnalysisOperationBody]**](AnalysisOperationBody.md) | The analysis&#39; static-analysis operation, followed by the latest run of each other operation started on its binary. Operations that have never run are omitted | 

## Example

```python
from revengai.models.analysis_operations_output_body import AnalysisOperationsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisOperationsOutputBody from a JSON string
analysis_operations_output_body_instance = AnalysisOperationsOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisOperationsOutputBody.to_json())

# convert the object into a dict
analysis_operations_output_body_dict = analysis_operations_output_body_instance.to_dict()
# create an instance of AnalysisOperationsOutputBody from a dict
analysis_operations_output_body_from_dict = AnalysisOperationsOutputBody.from_dict(analysis_operations_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


