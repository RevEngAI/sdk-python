# BulkAddTagsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BulkAddTagsResultBody]**](BulkAddTagsResultBody.md) | One entry per requested analysis, in the order they were given | 

## Example

```python
from revengai.models.bulk_add_tags_output_body import BulkAddTagsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAddTagsOutputBody from a JSON string
bulk_add_tags_output_body_instance = BulkAddTagsOutputBody.from_json(json)
# print the JSON string representation of the object
print(BulkAddTagsOutputBody.to_json())

# convert the object into a dict
bulk_add_tags_output_body_dict = bulk_add_tags_output_body_instance.to_dict()
# create an instance of BulkAddTagsOutputBody from a dict
bulk_add_tags_output_body_from_dict = BulkAddTagsOutputBody.from_dict(bulk_add_tags_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


