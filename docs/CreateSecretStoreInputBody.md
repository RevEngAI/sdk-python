# CreateSecretStoreInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_provider** | **str** |  | 
**key** | **str** | The provider&#39;s API key, encrypted before storage. | 
**team_id** | **int** | Registers a team secret when set; the caller must administer that team. Registers a personal secret when omitted. | [optional] 

## Example

```python
from revengai.models.create_secret_store_input_body import CreateSecretStoreInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretStoreInputBody from a JSON string
create_secret_store_input_body_instance = CreateSecretStoreInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateSecretStoreInputBody.to_json())

# convert the object into a dict
create_secret_store_input_body_dict = create_secret_store_input_body_instance.to_dict()
# create an instance of CreateSecretStoreInputBody from a dict
create_secret_store_input_body_from_dict = CreateSecretStoreInputBody.from_dict(create_secret_store_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


