# ListSecretStoreOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[SecretBody]**](SecretBody.md) |  | 

## Example

```python
from revengai.models.list_secret_store_output_body import ListSecretStoreOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListSecretStoreOutputBody from a JSON string
list_secret_store_output_body_instance = ListSecretStoreOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListSecretStoreOutputBody.to_json())

# convert the object into a dict
list_secret_store_output_body_dict = list_secret_store_output_body_instance.to_dict()
# create an instance of ListSecretStoreOutputBody from a dict
list_secret_store_output_body_from_dict = ListSecretStoreOutputBody.from_dict(list_secret_store_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


