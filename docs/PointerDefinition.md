# PointerDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pointee_data_type_id** | **int** | The type pointed at. | [optional] 

## Example

```python
from revengai.models.pointer_definition import PointerDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PointerDefinition from a JSON string
pointer_definition_instance = PointerDefinition.from_json(json)
# print the JSON string representation of the object
print(PointerDefinition.to_json())

# convert the object into a dict
pointer_definition_dict = pointer_definition_instance.to_dict()
# create an instance of PointerDefinition from a dict
pointer_definition_from_dict = PointerDefinition.from_dict(pointer_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


