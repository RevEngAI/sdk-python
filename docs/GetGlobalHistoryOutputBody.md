# GetGlobalHistoryOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history** | [**List[GlobalHistoryEntry]**](GlobalHistoryEntry.md) | Replaced values, oldest first. | 

## Example

```python
from revengai.models.get_global_history_output_body import GetGlobalHistoryOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalHistoryOutputBody from a JSON string
get_global_history_output_body_instance = GetGlobalHistoryOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetGlobalHistoryOutputBody.to_json())

# convert the object into a dict
get_global_history_output_body_dict = get_global_history_output_body_instance.to_dict()
# create an instance of GetGlobalHistoryOutputBody from a dict
get_global_history_output_body_from_dict = GetGlobalHistoryOutputBody.from_dict(get_global_history_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


