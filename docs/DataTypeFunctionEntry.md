# DataTypeFunctionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** |  | 
**function_name** | **str** | Current name of the function. | 

## Example

```python
from revengai.models.data_type_function_entry import DataTypeFunctionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeFunctionEntry from a JSON string
data_type_function_entry_instance = DataTypeFunctionEntry.from_json(json)
# print the JSON string representation of the object
print(DataTypeFunctionEntry.to_json())

# convert the object into a dict
data_type_function_entry_dict = data_type_function_entry_instance.to_dict()
# create an instance of DataTypeFunctionEntry from a dict
data_type_function_entry_from_dict = DataTypeFunctionEntry.from_dict(data_type_function_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


