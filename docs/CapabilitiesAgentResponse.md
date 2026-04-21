# CapabilitiesAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[AppApiRestV2AgentSchemaCapability]**](AppApiRestV2AgentSchemaCapability.md) | List of enriched capability data | 

## Example

```python
from revengai.models.capabilities_agent_response import CapabilitiesAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesAgentResponse from a JSON string
capabilities_agent_response_instance = CapabilitiesAgentResponse.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesAgentResponse.to_json())

# convert the object into a dict
capabilities_agent_response_dict = capabilities_agent_response_instance.to_dict()
# create an instance of CapabilitiesAgentResponse from a dict
capabilities_agent_response_from_dict = CapabilitiesAgentResponse.from_dict(capabilities_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


