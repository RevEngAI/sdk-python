# BatchUpdateDataTypesItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | **object** |  | 
**data_types_version** | **int** | Current stored version. Pass 0 on the first write. | 
**function_id** | **int** | Function ID | 

## Example

```python
from revengai.models.batch_update_data_types_item import BatchUpdateDataTypesItem

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateDataTypesItem from a JSON string
batch_update_data_types_item_instance = BatchUpdateDataTypesItem.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateDataTypesItem.to_json())

# convert the object into a dict
batch_update_data_types_item_dict = batch_update_data_types_item_instance.to_dict()
# create an instance of BatchUpdateDataTypesItem from a dict
batch_update_data_types_item_from_dict = BatchUpdateDataTypesItem.from_dict(batch_update_data_types_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


