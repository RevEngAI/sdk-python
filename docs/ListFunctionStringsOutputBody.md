# ListFunctionStringsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strings** | [**List[FunctionStringItem]**](FunctionStringItem.md) |  | 
**total_strings** | **int** |  | 

## Example

```python
from revengai.models.list_function_strings_output_body import ListFunctionStringsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListFunctionStringsOutputBody from a JSON string
list_function_strings_output_body_instance = ListFunctionStringsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListFunctionStringsOutputBody.to_json())

# convert the object into a dict
list_function_strings_output_body_dict = list_function_strings_output_body_instance.to_dict()
# create an instance of ListFunctionStringsOutputBody from a dict
list_function_strings_output_body_from_dict = ListFunctionStringsOutputBody.from_dict(list_function_strings_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


