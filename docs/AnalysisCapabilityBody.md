# AnalysisCapabilityBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** | Capabilities attributed to the function | 
**function_name** | **str** | Name of the function the capability was found in | 
**function_vaddr** | **int** | Virtual address of that function | 

## Example

```python
from revengai.models.analysis_capability_body import AnalysisCapabilityBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCapabilityBody from a JSON string
analysis_capability_body_instance = AnalysisCapabilityBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisCapabilityBody.to_json())

# convert the object into a dict
analysis_capability_body_dict = analysis_capability_body_instance.to_dict()
# create an instance of AnalysisCapabilityBody from a dict
analysis_capability_body_from_dict = AnalysisCapabilityBody.from_dict(analysis_capability_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


