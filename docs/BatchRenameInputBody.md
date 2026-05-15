# BatchRenameInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[BatchRenameItem]**](BatchRenameItem.md) | List of functions to rename | 

## Example

```python
from revengai.models.batch_rename_input_body import BatchRenameInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRenameInputBody from a JSON string
batch_rename_input_body_instance = BatchRenameInputBody.from_json(json)
# print the JSON string representation of the object
print(BatchRenameInputBody.to_json())

# convert the object into a dict
batch_rename_input_body_dict = batch_rename_input_body_instance.to_dict()
# create an instance of BatchRenameInputBody from a dict
batch_rename_input_body_from_dict = BatchRenameInputBody.from_dict(batch_rename_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


