# Capability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **str** | The capability itself | 
**description** | **str** | What the function does to exhibit the capability | 
**function_id** | **int** | ID of the function | 
**function_name** | **str** | Name of the function | 
**function_vaddr** | **str** | Virtual address of the function, hex-encoded | 
**type** | **str** | Capability category | 

## Example

```python
from revengai.models.capability import Capability

# TODO update the JSON string below
json = "{}"
# create an instance of Capability from a JSON string
capability_instance = Capability.from_json(json)
# print the JSON string representation of the object
print(Capability.to_json())

# convert the object into a dict
capability_dict = capability_instance.to_dict()
# create an instance of Capability from a dict
capability_from_dict = Capability.from_dict(capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


