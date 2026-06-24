# CreateIdentityInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_url** | **str** | Issuer URL (must be trusted by this organisation) | 
**subject** | **str** | External subject identifier from the issuer | 
**user_id** | **int** | Internal user ID to link | 

## Example

```python
from revengai.models.create_identity_input_body import CreateIdentityInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIdentityInputBody from a JSON string
create_identity_input_body_instance = CreateIdentityInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateIdentityInputBody.to_json())

# convert the object into a dict
create_identity_input_body_dict = create_identity_input_body_instance.to_dict()
# create an instance of CreateIdentityInputBody from a dict
create_identity_input_body_from_dict = CreateIdentityInputBody.from_dict(create_identity_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


