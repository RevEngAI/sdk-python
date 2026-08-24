# DataTypeFunctionParameterEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | The parameter&#39;s type. | [optional] 
**name** | **str** | Parameter name, when the producer had one. | [optional] 
**ordinal** | **int** | Zero-based argument position. | 
**size** | **int** | Parameter size in bytes. | 

## Example

```python
from revengai.models.data_type_function_parameter_entry import DataTypeFunctionParameterEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeFunctionParameterEntry from a JSON string
data_type_function_parameter_entry_instance = DataTypeFunctionParameterEntry.from_json(json)
# print the JSON string representation of the object
print(DataTypeFunctionParameterEntry.to_json())

# convert the object into a dict
data_type_function_parameter_entry_dict = data_type_function_parameter_entry_instance.to_dict()
# create an instance of DataTypeFunctionParameterEntry from a dict
data_type_function_parameter_entry_from_dict = DataTypeFunctionParameterEntry.from_dict(data_type_function_parameter_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


