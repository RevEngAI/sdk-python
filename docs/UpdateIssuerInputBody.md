# UpdateIssuerInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the issuer is enabled | 

## Example

```python
from revengai.models.update_issuer_input_body import UpdateIssuerInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIssuerInputBody from a JSON string
update_issuer_input_body_instance = UpdateIssuerInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateIssuerInputBody.to_json())

# convert the object into a dict
update_issuer_input_body_dict = update_issuer_input_body_instance.to_dict()
# create an instance of UpdateIssuerInputBody from a dict
update_issuer_input_body_from_dict = UpdateIssuerInputBody.from_dict(update_issuer_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


