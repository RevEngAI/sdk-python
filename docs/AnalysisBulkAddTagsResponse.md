# AnalysisBulkAddTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AnalysisBulkAddTagsResponseItem]**](AnalysisBulkAddTagsResponseItem.md) |  | 

## Example

```python
from revengai.models.analysis_bulk_add_tags_response import AnalysisBulkAddTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisBulkAddTagsResponse from a JSON string
analysis_bulk_add_tags_response_instance = AnalysisBulkAddTagsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalysisBulkAddTagsResponse.to_json())

# convert the object into a dict
analysis_bulk_add_tags_response_dict = analysis_bulk_add_tags_response_instance.to_dict()
# create an instance of AnalysisBulkAddTagsResponse from a dict
analysis_bulk_add_tags_response_from_dict = AnalysisBulkAddTagsResponse.from_dict(analysis_bulk_add_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


