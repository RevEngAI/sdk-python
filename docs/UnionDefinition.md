# UnionDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[DataTypeMemberEntry]**](DataTypeMemberEntry.md) | The type&#39;s fields. Every member starts at offset 0. | 

## Example

```python
from revengai.models.union_definition import UnionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of UnionDefinition from a JSON string
union_definition_instance = UnionDefinition.from_json(json)
# print the JSON string representation of the object
print(UnionDefinition.to_json())

# convert the object into a dict
union_definition_dict = union_definition_instance.to_dict()
# create an instance of UnionDefinition from a dict
union_definition_from_dict = UnionDefinition.from_dict(union_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


