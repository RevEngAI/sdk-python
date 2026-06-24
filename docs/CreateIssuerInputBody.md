# CreateIssuerInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OIDC client ID for audience validation (recommended) | [optional] 
**issuer_url** | **str** | OIDC issuer URL to trust | 

## Example

```python
from revengai.models.create_issuer_input_body import CreateIssuerInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssuerInputBody from a JSON string
create_issuer_input_body_instance = CreateIssuerInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateIssuerInputBody.to_json())

# convert the object into a dict
create_issuer_input_body_dict = create_issuer_input_body_instance.to_dict()
# create an instance of CreateIssuerInputBody from a dict
create_issuer_input_body_from_dict = CreateIssuerInputBody.from_dict(create_issuer_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


