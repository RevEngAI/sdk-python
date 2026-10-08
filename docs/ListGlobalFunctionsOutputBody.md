# ListGlobalFunctionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[FunctionUsage]**](FunctionUsage.md) |  | 

## Example

```python
from revengai.models.list_global_functions_output_body import ListGlobalFunctionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListGlobalFunctionsOutputBody from a JSON string
list_global_functions_output_body_instance = ListGlobalFunctionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListGlobalFunctionsOutputBody.to_json())

# convert the object into a dict
list_global_functions_output_body_dict = list_global_functions_output_body_instance.to_dict()
# create an instance of ListGlobalFunctionsOutputBody from a dict
list_global_functions_output_body_from_dict = ListGlobalFunctionsOutputBody.from_dict(list_global_functions_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


