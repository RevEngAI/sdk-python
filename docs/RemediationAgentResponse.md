# RemediationAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yara_rules** | **List[str]** | Generated YARA rules for the binary | 
**snort_rules** | **List[str]** | Generated Snort rules for the binary | 
**stix_rules** | **List[str]** | Generated STIX rules for the binary | 

## Example

```python
from revengai.models.remediation_agent_response import RemediationAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemediationAgentResponse from a JSON string
remediation_agent_response_instance = RemediationAgentResponse.from_json(json)
# print the JSON string representation of the object
print(RemediationAgentResponse.to_json())

# convert the object into a dict
remediation_agent_response_dict = remediation_agent_response_instance.to_dict()
# create an instance of RemediationAgentResponse from a dict
remediation_agent_response_from_dict = RemediationAgentResponse.from_dict(remediation_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


