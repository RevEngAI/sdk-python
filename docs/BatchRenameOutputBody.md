# BatchRenameOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**renamed_count** | **int** | Number of functions renamed | 

## Example

```python
from revengai.models.batch_rename_output_body import BatchRenameOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRenameOutputBody from a JSON string
batch_rename_output_body_instance = BatchRenameOutputBody.from_json(json)
# print the JSON string representation of the object
print(BatchRenameOutputBody.to_json())

# convert the object into a dict
batch_rename_output_body_dict = batch_rename_output_body_instance.to_dict()
# create an instance of BatchRenameOutputBody from a dict
batch_rename_output_body_from_dict = BatchRenameOutputBody.from_dict(batch_rename_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


