# SecretsAgentResponse

Full secrets report, including metadata, findings, and evidence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**findings** | [**List[Finding]**](Finding.md) |  | [optional] 

## Example

```python
from revengai.models.secrets_agent_response import SecretsAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretsAgentResponse from a JSON string
secrets_agent_response_instance = SecretsAgentResponse.from_json(json)
# print the JSON string representation of the object
print(SecretsAgentResponse.to_json())

# convert the object into a dict
secrets_agent_response_dict = secrets_agent_response_instance.to_dict()
# create an instance of SecretsAgentResponse from a dict
secrets_agent_response_from_dict = SecretsAgentResponse.from_dict(secrets_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


