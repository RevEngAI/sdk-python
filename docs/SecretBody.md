# SecretBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**api_provider** | **str** |  | 
**creation** | **datetime** |  | 
**disabled_at** | **datetime** |  | [optional] 
**id** | **int** |  | 
**key** | **str** | Masked API key showing only the last 4 characters | 
**team_id** | **int** | Null for a personal secret | [optional] 
**user_id** | **int** |  | 
**valid** | **bool** |  | 

## Example

```python
from revengai.models.secret_body import SecretBody

# TODO update the JSON string below
json = "{}"
# create an instance of SecretBody from a JSON string
secret_body_instance = SecretBody.from_json(json)
# print the JSON string representation of the object
print(SecretBody.to_json())

# convert the object into a dict
secret_body_dict = secret_body_instance.to_dict()
# create an instance of SecretBody from a dict
secret_body_from_dict = SecretBody.from_dict(secret_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


