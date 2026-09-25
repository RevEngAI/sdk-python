# AnalysisTagsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[AnalysisTagBody]**](AnalysisTagBody.md) | Every tag on the analysis&#39; binary, of any origin | 

## Example

```python
from revengai.models.analysis_tags_output_body import AnalysisTagsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTagsOutputBody from a JSON string
analysis_tags_output_body_instance = AnalysisTagsOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisTagsOutputBody.to_json())

# convert the object into a dict
analysis_tags_output_body_dict = analysis_tags_output_body_instance.to_dict()
# create an instance of AnalysisTagsOutputBody from a dict
analysis_tags_output_body_from_dict = AnalysisTagsOutputBody.from_dict(analysis_tags_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


