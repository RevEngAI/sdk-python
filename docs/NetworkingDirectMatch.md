# NetworkingDirectMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Networking category of the match | 
**how** | **str** | Detection tier that produced the match | 
**matched_name** | **str** | Name or token that matched | 
**source** | **str** | Networking source the match belongs to | 

## Example

```python
from revengai.models.networking_direct_match import NetworkingDirectMatch

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingDirectMatch from a JSON string
networking_direct_match_instance = NetworkingDirectMatch.from_json(json)
# print the JSON string representation of the object
print(NetworkingDirectMatch.to_json())

# convert the object into a dict
networking_direct_match_dict = networking_direct_match_instance.to_dict()
# create an instance of NetworkingDirectMatch from a dict
networking_direct_match_from_dict = NetworkingDirectMatch.from_dict(networking_direct_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


