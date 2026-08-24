# TypedefDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_data_type_id** | **int** | The type being aliased. | [optional] 

## Example

```python
from revengai.models.typedef_definition import TypedefDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TypedefDefinition from a JSON string
typedef_definition_instance = TypedefDefinition.from_json(json)
# print the JSON string representation of the object
print(TypedefDefinition.to_json())

# convert the object into a dict
typedef_definition_dict = typedef_definition_instance.to_dict()
# create an instance of TypedefDefinition from a dict
typedef_definition_from_dict = TypedefDefinition.from_dict(typedef_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


