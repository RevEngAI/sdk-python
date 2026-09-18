# CapabilitiesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[Capability]**](Capability.md) | Capabilities found. A capability whose address no longer resolves within the analysis is omitted. | 

## Example

```python
from revengai.models.capabilities_result import CapabilitiesResult

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesResult from a JSON string
capabilities_result_instance = CapabilitiesResult.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesResult.to_json())

# convert the object into a dict
capabilities_result_dict = capabilities_result_instance.to_dict()
# create an instance of CapabilitiesResult from a dict
capabilities_result_from_dict = CapabilitiesResult.from_dict(capabilities_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


