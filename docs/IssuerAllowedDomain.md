# IssuerAllowedDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_token** | **str** | DNS TXT challenge token. Add a TXT record at _reveng-verification.&lt;domain&gt; with this value. | [optional] 
**created_at** | **datetime** |  | 
**domain** | **str** | Email domain (e.g. acme.com) | 
**issuer_allowed_domain_id** | **int** |  | 
**organisation_issuer_id** | **int** |  | 
**verification_status** | **str** | Domain ownership verification status: PENDING, VERIFIED, or FAILED | 

## Example

```python
from revengai.models.issuer_allowed_domain import IssuerAllowedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of IssuerAllowedDomain from a JSON string
issuer_allowed_domain_instance = IssuerAllowedDomain.from_json(json)
# print the JSON string representation of the object
print(IssuerAllowedDomain.to_json())

# convert the object into a dict
issuer_allowed_domain_dict = issuer_allowed_domain_instance.to_dict()
# create an instance of IssuerAllowedDomain from a dict
issuer_allowed_domain_from_dict = IssuerAllowedDomain.from_dict(issuer_allowed_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


