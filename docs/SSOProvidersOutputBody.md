# SSOProvidersOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[SSOProvider]**](SSOProvider.md) |  | 

## Example

```python
from revengai.models.sso_providers_output_body import SSOProvidersOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SSOProvidersOutputBody from a JSON string
sso_providers_output_body_instance = SSOProvidersOutputBody.from_json(json)
# print the JSON string representation of the object
print(SSOProvidersOutputBody.to_json())

# convert the object into a dict
sso_providers_output_body_dict = sso_providers_output_body_instance.to_dict()
# create an instance of SSOProvidersOutputBody from a dict
sso_providers_output_body_from_dict = SSOProvidersOutputBody.from_dict(sso_providers_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


