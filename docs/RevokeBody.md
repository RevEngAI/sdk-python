# RevokeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | The refresh token to revoke (falls back to refresh_token cookie if omitted) | [optional] 

## Example

```python
from revengai.models.revoke_body import RevokeBody

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeBody from a JSON string
revoke_body_instance = RevokeBody.from_json(json)
# print the JSON string representation of the object
print(RevokeBody.to_json())

# convert the object into a dict
revoke_body_dict = revoke_body_instance.to_dict()
# create an instance of RevokeBody from a dict
revoke_body_from_dict = RevokeBody.from_dict(revoke_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


