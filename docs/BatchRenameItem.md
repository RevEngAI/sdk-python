# BatchRenameItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** | Function ID to rename | 
**new_mangled_name** | **str** | New mangled function name | [optional] 
**new_name** | **str** | New function name | 

## Example

```python
from revengai.models.batch_rename_item import BatchRenameItem

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRenameItem from a JSON string
batch_rename_item_instance = BatchRenameItem.from_json(json)
# print the JSON string representation of the object
print(BatchRenameItem.to_json())

# convert the object into a dict
batch_rename_item_dict = batch_rename_item_instance.to_dict()
# create an instance of BatchRenameItem from a dict
batch_rename_item_from_dict = BatchRenameItem.from_dict(batch_rename_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


