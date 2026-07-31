# BaseResponseRemediationAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]
**data** | [**RemediationAgentResponse**](RemediationAgentResponse.md) |  | [optional] 
**message** | **str** |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 

## Example

```python
from revengai.models.base_response_remediation_agent_response import BaseResponseRemediationAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseRemediationAgentResponse from a JSON string
base_response_remediation_agent_response_instance = BaseResponseRemediationAgentResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseRemediationAgentResponse.to_json())

# convert the object into a dict
base_response_remediation_agent_response_dict = base_response_remediation_agent_response_instance.to_dict()
# create an instance of BaseResponseRemediationAgentResponse from a dict
base_response_remediation_agent_response_from_dict = BaseResponseRemediationAgentResponse.from_dict(base_response_remediation_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


