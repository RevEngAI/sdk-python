# ArrayDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Element count. Zero is a genuinely empty trailing array; absent means it could not be determined. | [optional] 
**element_data_type_id** | **int** | The element type. | [optional] 

## Example

```python
from revengai.models.array_definition import ArrayDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayDefinition from a JSON string
array_definition_instance = ArrayDefinition.from_json(json)
# print the JSON string representation of the object
print(ArrayDefinition.to_json())

# convert the object into a dict
array_definition_dict = array_definition_instance.to_dict()
# create an instance of ArrayDefinition from a dict
array_definition_from_dict = ArrayDefinition.from_dict(array_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


