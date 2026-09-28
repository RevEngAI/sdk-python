# ApiKeyBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The API key | 

## Example

```python
from revengai.models.api_key_body import ApiKeyBody

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyBody from a JSON string
api_key_body_instance = ApiKeyBody.from_json(json)
# print the JSON string representation of the object
print(ApiKeyBody.to_json())

# convert the object into a dict
api_key_body_dict = api_key_body_instance.to_dict()
# create an instance of ApiKeyBody from a dict
api_key_body_from_dict = ApiKeyBody.from_dict(api_key_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


