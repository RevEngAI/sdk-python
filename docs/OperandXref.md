# OperandXref


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruction_vaddr** | **int** | Vaddr of the instruction containing the operand. | 
**pointed_vaddr** | **int** | Address stored in the pointer slot. Resolve this to a function, import or global to name the reference. | 
**target_vaddr** | **int** | Vaddr of the pointer slot the operand references. | 

## Example

```python
from revengai.models.operand_xref import OperandXref

# TODO update the JSON string below
json = "{}"
# create an instance of OperandXref from a JSON string
operand_xref_instance = OperandXref.from_json(json)
# print the JSON string representation of the object
print(OperandXref.to_json())

# convert the object into a dict
operand_xref_dict = operand_xref_instance.to_dict()
# create an instance of OperandXref from a dict
operand_xref_from_dict = OperandXref.from_dict(operand_xref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


