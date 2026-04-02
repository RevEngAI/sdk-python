# BulkDeleteAnalysesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_ids** | **List[int]** |  | 

## Example

```python
from revengai.models.bulk_delete_analyses_request import BulkDeleteAnalysesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteAnalysesRequest from a JSON string
bulk_delete_analyses_request_instance = BulkDeleteAnalysesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteAnalysesRequest.to_json())

# convert the object into a dict
bulk_delete_analyses_request_dict = bulk_delete_analyses_request_instance.to_dict()
# create an instance of BulkDeleteAnalysesRequest from a dict
bulk_delete_analyses_request_from_dict = BulkDeleteAnalysesRequest.from_dict(bulk_delete_analyses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


