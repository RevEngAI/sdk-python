# DisassemblyOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_blocks** | **object** |  | [optional] 
**function_id** | **int** |  | 
**local_variables** | **object** |  | [optional] 
**params** | **object** |  | [optional] 
**return_type** | **str** |  | [optional] 
**returns** | **bool** |  | 

## Example

```python
from revengai.models.disassembly_output_body import DisassemblyOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of DisassemblyOutputBody from a JSON string
disassembly_output_body_instance = DisassemblyOutputBody.from_json(json)
# print the JSON string representation of the object
print(DisassemblyOutputBody.to_json())

# convert the object into a dict
disassembly_output_body_dict = disassembly_output_body_instance.to_dict()
# create an instance of DisassemblyOutputBody from a dict
disassembly_output_body_from_dict = DisassemblyOutputBody.from_dict(disassembly_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


