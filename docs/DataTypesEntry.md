# DataTypesEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**FunctionInfo**](FunctionInfo.md) |  | [optional] 
**function_id** | **int** |  | 

## Example

```python
from revengai.models.data_types_entry import DataTypesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypesEntry from a JSON string
data_types_entry_instance = DataTypesEntry.from_json(json)
# print the JSON string representation of the object
print(DataTypesEntry.to_json())

# convert the object into a dict
data_types_entry_dict = data_types_entry_instance.to_dict()
# create an instance of DataTypesEntry from a dict
data_types_entry_from_dict = DataTypesEntry.from_dict(data_types_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


