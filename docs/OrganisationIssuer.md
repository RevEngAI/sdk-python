# OrganisationIssuer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OIDC client ID registered with the identity provider. Used to validate the audience (aud) claim in JWTs. | [optional] 
**created_at** | **datetime** |  | 
**enabled** | **bool** |  | 
**issuer_url** | **str** |  | 
**jwks_uri** | **str** | JSON Web Key Set URI discovered from the issuer&#39;s OIDC configuration. Populated automatically during issuer registration. | [optional] 
**organisation_id** | **int** |  | 
**organisation_issuer_id** | **int** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from revengai.models.organisation_issuer import OrganisationIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of OrganisationIssuer from a JSON string
organisation_issuer_instance = OrganisationIssuer.from_json(json)
# print the JSON string representation of the object
print(OrganisationIssuer.to_json())

# convert the object into a dict
organisation_issuer_dict = organisation_issuer_instance.to_dict()
# create an instance of OrganisationIssuer from a dict
organisation_issuer_from_dict = OrganisationIssuer.from_dict(organisation_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


