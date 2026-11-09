# CapabilityImplementation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **str** | Capability this summary describes | 
**summary** | **str** | How the function implements this capability | 

## Example

```python
from revengai.models.capability_implementation import CapabilityImplementation

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityImplementation from a JSON string
capability_implementation_instance = CapabilityImplementation.from_json(json)
# print the JSON string representation of the object
print(CapabilityImplementation.to_json())

# convert the object into a dict
capability_implementation_dict = capability_implementation_instance.to_dict()
# create an instance of CapabilityImplementation from a dict
capability_implementation_from_dict = CapabilityImplementation.from_dict(capability_implementation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


