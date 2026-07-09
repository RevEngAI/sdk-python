# AnalysisTagBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** | Collection this tag maps to, or null | 
**name** | **str** | Tag name | 
**origin** | **str** | Origin of the tag | 

## Example

```python
from revengai.models.analysis_tag_body import AnalysisTagBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTagBody from a JSON string
analysis_tag_body_instance = AnalysisTagBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisTagBody.to_json())

# convert the object into a dict
analysis_tag_body_dict = analysis_tag_body_instance.to_dict()
# create an instance of AnalysisTagBody from a dict
analysis_tag_body_from_dict = AnalysisTagBody.from_dict(analysis_tag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


