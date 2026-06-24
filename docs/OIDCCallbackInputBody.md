# OIDCCallbackInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Authorization code from the identity provider | 
**code_verifier** | **str** | PKCE code verifier (the raw secret, not the challenge) | 
**issuer** | **str** | OIDC issuer URL (as returned by the SSO providers endpoint) | 
**redirect_uri** | **str** | Redirect URI used when initiating the authorization request; must match exactly | 

## Example

```python
from revengai.models.oidc_callback_input_body import OIDCCallbackInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCCallbackInputBody from a JSON string
oidc_callback_input_body_instance = OIDCCallbackInputBody.from_json(json)
# print the JSON string representation of the object
print(OIDCCallbackInputBody.to_json())

# convert the object into a dict
oidc_callback_input_body_dict = oidc_callback_input_body_instance.to_dict()
# create an instance of OIDCCallbackInputBody from a dict
oidc_callback_input_body_from_dict = OIDCCallbackInputBody.from_dict(oidc_callback_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


