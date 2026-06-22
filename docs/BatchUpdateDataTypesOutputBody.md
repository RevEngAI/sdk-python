# BatchUpdateDataTypesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BatchUpdateDataTypesResult]**](BatchUpdateDataTypesResult.md) | Per-function outcomes in the same order as the input | 

## Example

```python
from revengai.models.batch_update_data_types_output_body import BatchUpdateDataTypesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateDataTypesOutputBody from a JSON string
batch_update_data_types_output_body_instance = BatchUpdateDataTypesOutputBody.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateDataTypesOutputBody.to_json())

# convert the object into a dict
batch_update_data_types_output_body_dict = batch_update_data_types_output_body_instance.to_dict()
# create an instance of BatchUpdateDataTypesOutputBody from a dict
batch_update_data_types_output_body_from_dict = BatchUpdateDataTypesOutputBody.from_dict(batch_update_data_types_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


