# StructDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[DataTypeMemberEntry]**](DataTypeMemberEntry.md) | The type&#39;s fields, in offset order. | 

## Example

```python
from revengai.models.struct_definition import StructDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StructDefinition from a JSON string
struct_definition_instance = StructDefinition.from_json(json)
# print the JSON string representation of the object
print(StructDefinition.to_json())

# convert the object into a dict
struct_definition_dict = struct_definition_instance.to_dict()
# create an instance of StructDefinition from a dict
struct_definition_from_dict = StructDefinition.from_dict(struct_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


