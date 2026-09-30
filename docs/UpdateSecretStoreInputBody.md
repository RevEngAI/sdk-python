# UpdateSecretStoreInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Activates or deactivates the secret. Omit to leave unchanged. | [optional] 
**key** | **str** | New API key. Omit to leave the current key unchanged. | [optional] 

## Example

```python
from revengai.models.update_secret_store_input_body import UpdateSecretStoreInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecretStoreInputBody from a JSON string
update_secret_store_input_body_instance = UpdateSecretStoreInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateSecretStoreInputBody.to_json())

# convert the object into a dict
update_secret_store_input_body_dict = update_secret_store_input_body_instance.to_dict()
# create an instance of UpdateSecretStoreInputBody from a dict
update_secret_store_input_body_from_dict = UpdateSecretStoreInputBody.from_dict(update_secret_store_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


