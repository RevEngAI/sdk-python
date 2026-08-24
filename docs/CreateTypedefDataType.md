# CreateTypedefDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**TypedefDefinition**](TypedefDefinition.md) |  | 
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.create_typedef_data_type import CreateTypedefDataType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTypedefDataType from a JSON string
create_typedef_data_type_instance = CreateTypedefDataType.from_json(json)
# print the JSON string representation of the object
print(CreateTypedefDataType.to_json())

# convert the object into a dict
create_typedef_data_type_dict = create_typedef_data_type_instance.to_dict()
# create an instance of CreateTypedefDataType from a dict
create_typedef_data_type_from_dict = CreateTypedefDataType.from_dict(create_typedef_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


