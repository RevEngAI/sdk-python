# AnalysisRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** | CreateAnalysis field paths that must be provided or enabled to satisfy this requirement. | 
**reason** | **str** | Why this requirement unblocks analysis. | 
**values** | **Dict[str, str]** | Field paths that must carry a specific value, keyed the same way as fields. | [optional] 

## Example

```python
from revengai.models.analysis_requirement import AnalysisRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRequirement from a JSON string
analysis_requirement_instance = AnalysisRequirement.from_json(json)
# print the JSON string representation of the object
print(AnalysisRequirement.to_json())

# convert the object into a dict
analysis_requirement_dict = analysis_requirement_instance.to_dict()
# create an instance of AnalysisRequirement from a dict
analysis_requirement_from_dict = AnalysisRequirement.from_dict(analysis_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


