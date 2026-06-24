# AddIssuerDomainInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Email domain to allow (e.g. acme.com) | 

## Example

```python
from revengai.models.add_issuer_domain_input_body import AddIssuerDomainInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddIssuerDomainInputBody from a JSON string
add_issuer_domain_input_body_instance = AddIssuerDomainInputBody.from_json(json)
# print the JSON string representation of the object
print(AddIssuerDomainInputBody.to_json())

# convert the object into a dict
add_issuer_domain_input_body_dict = add_issuer_domain_input_body_instance.to_dict()
# create an instance of AddIssuerDomainInputBody from a dict
add_issuer_domain_input_body_from_dict = AddIssuerDomainInputBody.from_dict(add_issuer_domain_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


