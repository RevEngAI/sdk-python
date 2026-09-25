# BulkAddTagsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_ids** | **List[int]** | IDs of the analyses to tag. The caller must own every one, or none are changed | 
**tags** | **List[str]** | Tags to add. A binary that already carries a tag, under any origin, is left as-is for that name | 

## Example

```python
from revengai.models.bulk_add_tags_input_body import BulkAddTagsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAddTagsInputBody from a JSON string
bulk_add_tags_input_body_instance = BulkAddTagsInputBody.from_json(json)
# print the JSON string representation of the object
print(BulkAddTagsInputBody.to_json())

# convert the object into a dict
bulk_add_tags_input_body_dict = bulk_add_tags_input_body_instance.to_dict()
# create an instance of BulkAddTagsInputBody from a dict
bulk_add_tags_input_body_from_dict = BulkAddTagsInputBody.from_dict(bulk_add_tags_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


