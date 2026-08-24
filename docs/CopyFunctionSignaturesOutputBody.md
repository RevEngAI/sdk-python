# CopyFunctionSignaturesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**List[DataTypeEntry]**](DataTypeEntry.md) | The data types this analysis gained or had replaced, ordered by data_type_id. Empty when every type the copied signatures need was already stored unchanged. | 
**signatures** | [**List[FunctionSignatureEntry]**](FunctionSignatureEntry.md) | The stored signatures of the target functions, in request order. | 

## Example

```python
from revengai.models.copy_function_signatures_output_body import CopyFunctionSignaturesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CopyFunctionSignaturesOutputBody from a JSON string
copy_function_signatures_output_body_instance = CopyFunctionSignaturesOutputBody.from_json(json)
# print the JSON string representation of the object
print(CopyFunctionSignaturesOutputBody.to_json())

# convert the object into a dict
copy_function_signatures_output_body_dict = copy_function_signatures_output_body_instance.to_dict()
# create an instance of CopyFunctionSignaturesOutputBody from a dict
copy_function_signatures_output_body_from_dict = CopyFunctionSignaturesOutputBody.from_dict(copy_function_signatures_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


