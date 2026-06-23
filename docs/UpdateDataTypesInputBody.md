# UpdateDataTypesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | **object** |  | 
**data_types_version** | **int** | Current version of the function data types. The update is rejected if the stored version has moved on. Pass 0 on the first write. | 

## Example

```python
from revengai.models.update_data_types_input_body import UpdateDataTypesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataTypesInputBody from a JSON string
update_data_types_input_body_instance = UpdateDataTypesInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateDataTypesInputBody.to_json())

# convert the object into a dict
update_data_types_input_body_dict = update_data_types_input_body_instance.to_dict()
# create an instance of UpdateDataTypesInputBody from a dict
update_data_types_input_body_from_dict = UpdateDataTypesInputBody.from_dict(update_data_types_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


