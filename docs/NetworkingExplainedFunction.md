# NetworkingExplainedFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Role this function plays in the network communication | 
**function_id** | **int** | ID of the function | 
**function_name** | **str** | Name of the function | 

## Example

```python
from revengai.models.networking_explained_function import NetworkingExplainedFunction

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingExplainedFunction from a JSON string
networking_explained_function_instance = NetworkingExplainedFunction.from_json(json)
# print the JSON string representation of the object
print(NetworkingExplainedFunction.to_json())

# convert the object into a dict
networking_explained_function_dict = networking_explained_function_instance.to_dict()
# create an instance of NetworkingExplainedFunction from a dict
networking_explained_function_from_dict = NetworkingExplainedFunction.from_dict(networking_explained_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


