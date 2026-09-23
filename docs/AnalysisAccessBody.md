# AnalysisAccessBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **bool** | True when the caller owns this analysis | 
**username** | **str** | Username of the analysis owner | 

## Example

```python
from revengai.models.analysis_access_body import AnalysisAccessBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisAccessBody from a JSON string
analysis_access_body_instance = AnalysisAccessBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisAccessBody.to_json())

# convert the object into a dict
analysis_access_body_dict = analysis_access_body_instance.to_dict()
# create an instance of AnalysisAccessBody from a dict
analysis_access_body_from_dict = AnalysisAccessBody.from_dict(analysis_access_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


