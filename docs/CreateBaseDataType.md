# CreateBaseDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**name** | **str** | Type name. Unique within the analysis for a given namespace and kind. | 
**namespace** | **str** | The scope qualifying the type name. Omit for a type of the binary&#39;s own. | [optional] 
**size** | **int** | Size in bytes. Omit when it is not known. | [optional] 

## Example

```python
from revengai.models.create_base_data_type import CreateBaseDataType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBaseDataType from a JSON string
create_base_data_type_instance = CreateBaseDataType.from_json(json)
# print the JSON string representation of the object
print(CreateBaseDataType.to_json())

# convert the object into a dict
create_base_data_type_dict = create_base_data_type_instance.to_dict()
# create an instance of CreateBaseDataType from a dict
create_base_data_type_from_dict = CreateBaseDataType.from_dict(create_base_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


