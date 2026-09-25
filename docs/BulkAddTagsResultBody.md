# BulkAddTagsResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_tags** | **List[str]** | Tags actually added; empty when the binary already carried every requested name | 
**analysis_id** | **int** | ID of the analysis | 

## Example

```python
from revengai.models.bulk_add_tags_result_body import BulkAddTagsResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAddTagsResultBody from a JSON string
bulk_add_tags_result_body_instance = BulkAddTagsResultBody.from_json(json)
# print the JSON string representation of the object
print(BulkAddTagsResultBody.to_json())

# convert the object into a dict
bulk_add_tags_result_body_dict = bulk_add_tags_result_body_instance.to_dict()
# create an instance of BulkAddTagsResultBody from a dict
bulk_add_tags_result_body_from_dict = BulkAddTagsResultBody.from_dict(bulk_add_tags_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


