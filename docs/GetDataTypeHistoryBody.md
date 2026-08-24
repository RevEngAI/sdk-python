# GetDataTypeHistoryBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[DataTypeVersion]**](DataTypeVersion.md) | Every version of the type, newest first. The first element is the current value, so the list is never empty; a type that has never been edited has that one element only. | 

## Example

```python
from revengai.models.get_data_type_history_body import GetDataTypeHistoryBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataTypeHistoryBody from a JSON string
get_data_type_history_body_instance = GetDataTypeHistoryBody.from_json(json)
# print the JSON string representation of the object
print(GetDataTypeHistoryBody.to_json())

# convert the object into a dict
get_data_type_history_body_dict = get_data_type_history_body_instance.to_dict()
# create an instance of GetDataTypeHistoryBody from a dict
get_data_type_history_body_from_dict = GetDataTypeHistoryBody.from_dict(get_data_type_history_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


