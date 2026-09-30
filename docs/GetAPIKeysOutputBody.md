# GetAPIKeysOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[ApiKeyBody]**](ApiKeyBody.md) | The caller&#39;s active API keys. Currently always exactly one, created on first request if the caller doesn&#39;t have one yet | 

## Example

```python
from revengai.models.get_api_keys_output_body import GetAPIKeysOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetAPIKeysOutputBody from a JSON string
get_api_keys_output_body_instance = GetAPIKeysOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetAPIKeysOutputBody.to_json())

# convert the object into a dict
get_api_keys_output_body_dict = get_api_keys_output_body_instance.to_dict()
# create an instance of GetAPIKeysOutputBody from a dict
get_api_keys_output_body_from_dict = GetAPIKeysOutputBody.from_dict(get_api_keys_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


