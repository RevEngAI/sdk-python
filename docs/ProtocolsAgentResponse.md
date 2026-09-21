# ProtocolsAgentResponse

Full protocols report, including metadata, findings, and evidence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**findings** | [**List[Finding]**](Finding.md) |  | [optional] 

## Example

```python
from revengai.models.protocols_agent_response import ProtocolsAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolsAgentResponse from a JSON string
protocols_agent_response_instance = ProtocolsAgentResponse.from_json(json)
# print the JSON string representation of the object
print(ProtocolsAgentResponse.to_json())

# convert the object into a dict
protocols_agent_response_dict = protocols_agent_response_instance.to_dict()
# create an instance of ProtocolsAgentResponse from a dict
protocols_agent_response_from_dict = ProtocolsAgentResponse.from_dict(protocols_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


