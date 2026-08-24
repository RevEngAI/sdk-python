# UpdatePointerDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | The type to replace, as returned by the data types list for this analysis. | 
**definition** | [**PointerDefinition**](PointerDefinition.md) |  | 
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.update_pointer_data_type import UpdatePointerDataType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePointerDataType from a JSON string
update_pointer_data_type_instance = UpdatePointerDataType.from_json(json)
# print the JSON string representation of the object
print(UpdatePointerDataType.to_json())

# convert the object into a dict
update_pointer_data_type_dict = update_pointer_data_type_instance.to_dict()
# create an instance of UpdatePointerDataType from a dict
update_pointer_data_type_from_dict = UpdatePointerDataType.from_dict(update_pointer_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


