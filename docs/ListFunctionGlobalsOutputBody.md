# ListFunctionGlobalsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**globals** | [**List[GlobalVariable]**](GlobalVariable.md) |  | 

## Example

```python
from revengai.models.list_function_globals_output_body import ListFunctionGlobalsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListFunctionGlobalsOutputBody from a JSON string
list_function_globals_output_body_instance = ListFunctionGlobalsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListFunctionGlobalsOutputBody.to_json())

# convert the object into a dict
list_function_globals_output_body_dict = list_function_globals_output_body_instance.to_dict()
# create an instance of ListFunctionGlobalsOutputBody from a dict
list_function_globals_output_body_from_dict = ListFunctionGlobalsOutputBody.from_dict(list_function_globals_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


