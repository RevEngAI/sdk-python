# BatchUpdateDataTypesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[BatchUpdateDataTypesItem]**](BatchUpdateDataTypesItem.md) | List of functions to update. All function IDs must belong to the analysis in the URL. | 

## Example

```python
from revengai.models.batch_update_data_types_input_body import BatchUpdateDataTypesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateDataTypesInputBody from a JSON string
batch_update_data_types_input_body_instance = BatchUpdateDataTypesInputBody.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateDataTypesInputBody.to_json())

# convert the object into a dict
batch_update_data_types_input_body_dict = batch_update_data_types_input_body_instance.to_dict()
# create an instance of BatchUpdateDataTypesInputBody from a dict
batch_update_data_types_input_body_from_dict = BatchUpdateDataTypesInputBody.from_dict(batch_update_data_types_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


