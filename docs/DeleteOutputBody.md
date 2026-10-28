# DeleteOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**id** | **int** |  | 

## Example

```python
from revengai.models.delete_output_body import DeleteOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOutputBody from a JSON string
delete_output_body_instance = DeleteOutputBody.from_json(json)
# print the JSON string representation of the object
print(DeleteOutputBody.to_json())

# convert the object into a dict
delete_output_body_dict = delete_output_body_instance.to_dict()
# create an instance of DeleteOutputBody from a dict
delete_output_body_from_dict = DeleteOutputBody.from_dict(delete_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


