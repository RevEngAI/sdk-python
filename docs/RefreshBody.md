# RefreshBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | The refresh token to rotate (falls back to refresh_token cookie if omitted) | [optional] 

## Example

```python
from revengai.models.refresh_body import RefreshBody

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshBody from a JSON string
refresh_body_instance = RefreshBody.from_json(json)
# print the JSON string representation of the object
print(RefreshBody.to_json())

# convert the object into a dict
refresh_body_dict = refresh_body_instance.to_dict()
# create an instance of RefreshBody from a dict
refresh_body_from_dict = RefreshBody.from_dict(refresh_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


