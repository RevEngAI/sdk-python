# FunctionSignatureBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calling_convention** | **str** | Calling convention, when the producer reported one. | [optional] 
**created_at** | **datetime** | When this signature was extracted. | [optional] 
**data_types** | [**List[DataTypeEntry]**](DataTypeEntry.md) | The types the signature names — its parameter types and its return type — ordered by data_type_id. Each entry is identical to the one the data types endpoints serve for that id. Returned only when include_data_types is true. | [optional] 
**function_id** | **int** |  | 
**function_name** | **str** | Current name of the function. | 
**has_signature** | **bool** | Whether a signature was extracted for this function. False is a normal result: no signature is recorded unless data type extraction ran for the analysis, and thunks and external functions are skipped when it does. | 
**parameters** | [**List[SignatureParameterEntry]**](SignatureParameterEntry.md) | Parameters in argument order. Empty with has_signature true means the function is known to take no arguments. | 
**return_data_type_id** | **int** | Return type, resolvable against the analysis data types list. Absent for an unresolved return type. | [optional] 
**source_function_id** | **int** | The function this signature was copied from, when it was transferred rather than extracted. | [optional] 
**source_type** | **str** | Where this signature came from. | [optional] 

## Example

```python
from revengai.models.function_signature_body import FunctionSignatureBody

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSignatureBody from a JSON string
function_signature_body_instance = FunctionSignatureBody.from_json(json)
# print the JSON string representation of the object
print(FunctionSignatureBody.to_json())

# convert the object into a dict
function_signature_body_dict = function_signature_body_instance.to_dict()
# create an instance of FunctionSignatureBody from a dict
function_signature_body_from_dict = FunctionSignatureBody.from_dict(function_signature_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


