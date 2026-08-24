# GetFunctionSignatureHistoryBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[FunctionSignatureVersion]**](FunctionSignatureVersion.md) | Every version of the signature, newest first. The first element is the current value, so the list is never empty; a signature that has never been edited has that one element only. | 

## Example

```python
from revengai.models.get_function_signature_history_body import GetFunctionSignatureHistoryBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetFunctionSignatureHistoryBody from a JSON string
get_function_signature_history_body_instance = GetFunctionSignatureHistoryBody.from_json(json)
# print the JSON string representation of the object
print(GetFunctionSignatureHistoryBody.to_json())

# convert the object into a dict
get_function_signature_history_body_dict = get_function_signature_history_body_instance.to_dict()
# create an instance of GetFunctionSignatureHistoryBody from a dict
get_function_signature_history_body_from_dict = GetFunctionSignatureHistoryBody.from_dict(get_function_signature_history_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


