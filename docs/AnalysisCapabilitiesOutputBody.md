# AnalysisCapabilitiesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[AnalysisCapabilityBody]**](AnalysisCapabilityBody.md) | Capabilities found across the binary, ordered by function address. Empty when the binary has no capability record | 

## Example

```python
from revengai.models.analysis_capabilities_output_body import AnalysisCapabilitiesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCapabilitiesOutputBody from a JSON string
analysis_capabilities_output_body_instance = AnalysisCapabilitiesOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisCapabilitiesOutputBody.to_json())

# convert the object into a dict
analysis_capabilities_output_body_dict = analysis_capabilities_output_body_instance.to_dict()
# create an instance of AnalysisCapabilitiesOutputBody from a dict
analysis_capabilities_output_body_from_dict = AnalysisCapabilitiesOutputBody.from_dict(analysis_capabilities_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


