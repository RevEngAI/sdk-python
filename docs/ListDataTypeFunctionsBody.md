# ListDataTypeFunctionsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DataTypeFunctionEntry]**](DataTypeFunctionEntry.md) | The page of matching functions, in ascending function ID order. Empty when no function uses the type. | 
**next_after_function_id** | **int** | Pass as after_function_id to fetch the next page. Absent on the last page. | [optional] 

## Example

```python
from revengai.models.list_data_type_functions_body import ListDataTypeFunctionsBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListDataTypeFunctionsBody from a JSON string
list_data_type_functions_body_instance = ListDataTypeFunctionsBody.from_json(json)
# print the JSON string representation of the object
print(ListDataTypeFunctionsBody.to_json())

# convert the object into a dict
list_data_type_functions_body_dict = list_data_type_functions_body_instance.to_dict()
# create an instance of ListDataTypeFunctionsBody from a dict
list_data_type_functions_body_from_dict = ListDataTypeFunctionsBody.from_dict(list_data_type_functions_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


