# NetworkingCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_name** | **str** | Name of the called function | 
**category** | **str** | Networking category of the match | 
**how** | **str** | Detection tier that produced the match | 
**matched_name** | **str** | Name or token that matched | 
**source** | **str** | Networking source the match belongs to | 

## Example

```python
from revengai.models.networking_call import NetworkingCall

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingCall from a JSON string
networking_call_instance = NetworkingCall.from_json(json)
# print the JSON string representation of the object
print(NetworkingCall.to_json())

# convert the object into a dict
networking_call_dict = networking_call_instance.to_dict()
# create an instance of NetworkingCall from a dict
networking_call_from_dict = NetworkingCall.from_dict(networking_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


