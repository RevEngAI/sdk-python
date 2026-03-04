# AnalysisBulkAddTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | 
**analysis_ids** | **List[int]** |  | 

## Example

```python
from revengai.models.analysis_bulk_add_tags_request import AnalysisBulkAddTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisBulkAddTagsRequest from a JSON string
analysis_bulk_add_tags_request_instance = AnalysisBulkAddTagsRequest.from_json(json)
# print the JSON string representation of the object
print(AnalysisBulkAddTagsRequest.to_json())

# convert the object into a dict
analysis_bulk_add_tags_request_dict = analysis_bulk_add_tags_request_instance.to_dict()
# create an instance of AnalysisBulkAddTagsRequest from a dict
analysis_bulk_add_tags_request_from_dict = AnalysisBulkAddTagsRequest.from_dict(analysis_bulk_add_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


