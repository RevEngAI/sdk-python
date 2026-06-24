# CapabilitiesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[CapabilityEntry]**](CapabilityEntry.md) |  | 

## Example

```python
from revengai.models.capabilities_output_body import CapabilitiesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesOutputBody from a JSON string
capabilities_output_body_instance = CapabilitiesOutputBody.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesOutputBody.to_json())

# convert the object into a dict
capabilities_output_body_dict = capabilities_output_body_instance.to_dict()
# create an instance of CapabilitiesOutputBody from a dict
capabilities_output_body_from_dict = CapabilitiesOutputBody.from_dict(capabilities_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


