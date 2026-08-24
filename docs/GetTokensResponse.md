# GetTokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_decomp** | **str** | Tokenised AI-decompilation. Includes generated comments. Empty until a run has succeeded. | 
**analysis_id** | **int** | Analysis the function belongs to. Scopes every data_type_id below. | 
**placeholder_to_rendered_token** | [**Dict[str, RenderedToken]**](RenderedToken.md) | Each placeholder token mapped to the value the server would render in its place, and the record it refers to. Null until a run has succeeded. | 
**placeholder_to_user_override** | [**Dict[str, Token]**](Token.md) | The caller&#39;s own overrides, keyed by token. Null until a run has succeeded. | 

## Example

```python
from revengai.models.get_tokens_response import GetTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokensResponse from a JSON string
get_tokens_response_instance = GetTokensResponse.from_json(json)
# print the JSON string representation of the object
print(GetTokensResponse.to_json())

# convert the object into a dict
get_tokens_response_dict = get_tokens_response_instance.to_dict()
# create an instance of GetTokensResponse from a dict
get_tokens_response_from_dict = GetTokensResponse.from_dict(get_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


