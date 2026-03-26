# AnalysisBulkAddTagsResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | 
**error** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from revengai.models.analysis_bulk_add_tags_response_item import AnalysisBulkAddTagsResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisBulkAddTagsResponseItem from a JSON string
analysis_bulk_add_tags_response_item_instance = AnalysisBulkAddTagsResponseItem.from_json(json)
# print the JSON string representation of the object
print(AnalysisBulkAddTagsResponseItem.to_json())

# convert the object into a dict
analysis_bulk_add_tags_response_item_dict = analysis_bulk_add_tags_response_item_instance.to_dict()
# create an instance of AnalysisBulkAddTagsResponseItem from a dict
analysis_bulk_add_tags_response_item_from_dict = AnalysisBulkAddTagsResponseItem.from_dict(analysis_bulk_add_tags_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


