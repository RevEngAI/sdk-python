# RenderedToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | Data type this token names, or for a field the type that declares it. Scoped by the response&#39;s analysis_id. | [optional] 
**function_id** | **int** | Function this token calls or names. Absent when the address reaches no function of this binary. | [optional] 
**imported_function_id** | **int** | Imported function this token calls. Set instead of function_id for an external call. | [optional] 
**kind** | **str** | What the token names. | 
**vaddr** | **int** | Virtual address the token resolves to. Absent for a token with no address. | [optional] 
**value** | **str** | Name the token resolves to. | 

## Example

```python
from revengai.models.rendered_token import RenderedToken

# TODO update the JSON string below
json = "{}"
# create an instance of RenderedToken from a JSON string
rendered_token_instance = RenderedToken.from_json(json)
# print the JSON string representation of the object
print(RenderedToken.to_json())

# convert the object into a dict
rendered_token_dict = rendered_token_instance.to_dict()
# create an instance of RenderedToken from a dict
rendered_token_from_dict = RenderedToken.from_dict(rendered_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


