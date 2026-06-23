# UpdateDataTypesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | **object** |  | 
**data_types_version** | **int** | Version of the stored function data types after the update | 
**function_id** | **int** | Function ID | 

## Example

```python
from revengai.models.update_data_types_output_body import UpdateDataTypesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataTypesOutputBody from a JSON string
update_data_types_output_body_instance = UpdateDataTypesOutputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateDataTypesOutputBody.to_json())

# convert the object into a dict
update_data_types_output_body_dict = update_data_types_output_body_instance.to_dict()
# create an instance of UpdateDataTypesOutputBody from a dict
update_data_types_output_body_from_dict = UpdateDataTypesOutputBody.from_dict(update_data_types_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


