# ListFunctionsDataTypesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DataTypesEntry]**](DataTypesEntry.md) |  | 

## Example

```python
from revengai.models.list_functions_data_types_output_body import ListFunctionsDataTypesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListFunctionsDataTypesOutputBody from a JSON string
list_functions_data_types_output_body_instance = ListFunctionsDataTypesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListFunctionsDataTypesOutputBody.to_json())

# convert the object into a dict
list_functions_data_types_output_body_dict = list_functions_data_types_output_body_instance.to_dict()
# create an instance of ListFunctionsDataTypesOutputBody from a dict
list_functions_data_types_output_body_from_dict = ListFunctionsDataTypesOutputBody.from_dict(list_functions_data_types_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


