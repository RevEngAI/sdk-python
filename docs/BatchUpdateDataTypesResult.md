# BatchUpdateDataTypesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | **object** |  | [optional] 
**data_types_version** | **int** | Version after update (present when status is &#39;updated&#39;) | [optional] 
**error** | **str** | Error message (present when status is &#39;error&#39;) | [optional] 
**function_id** | **int** | Function ID | 
**status** | **str** | Outcome for this function | 

## Example

```python
from revengai.models.batch_update_data_types_result import BatchUpdateDataTypesResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateDataTypesResult from a JSON string
batch_update_data_types_result_instance = BatchUpdateDataTypesResult.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateDataTypesResult.to_json())

# convert the object into a dict
batch_update_data_types_result_dict = batch_update_data_types_result_instance.to_dict()
# create an instance of BatchUpdateDataTypesResult from a dict
batch_update_data_types_result_from_dict = BatchUpdateDataTypesResult.from_dict(batch_update_data_types_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


