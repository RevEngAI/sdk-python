# BulkDeleteAnalysesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_ids** | **List[int]** | IDs of the analyses to delete. The caller must own every one, or none are deleted | 

## Example

```python
from revengai.models.bulk_delete_analyses_input_body import BulkDeleteAnalysesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteAnalysesInputBody from a JSON string
bulk_delete_analyses_input_body_instance = BulkDeleteAnalysesInputBody.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteAnalysesInputBody.to_json())

# convert the object into a dict
bulk_delete_analyses_input_body_dict = bulk_delete_analyses_input_body_instance.to_dict()
# create an instance of BulkDeleteAnalysesInputBody from a dict
bulk_delete_analyses_input_body_from_dict = BulkDeleteAnalysesInputBody.from_dict(bulk_delete_analyses_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


