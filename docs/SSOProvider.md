# SSOProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** | Base authorization URL. Append code_challenge, code_challenge_method, redirect_uri, and state query parameters to complete the PKCE flow. | 
**issuer** | **str** | Issuer URL of the identity provider. Pass this value as the issuer field in the SSO callback request. | 

## Example

```python
from revengai.models.sso_provider import SSOProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SSOProvider from a JSON string
sso_provider_instance = SSOProvider.from_json(json)
# print the JSON string representation of the object
print(SSOProvider.to_json())

# convert the object into a dict
sso_provider_dict = sso_provider_instance.to_dict()
# create an instance of SSOProvider from a dict
sso_provider_from_dict = SSOProvider.from_dict(sso_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


