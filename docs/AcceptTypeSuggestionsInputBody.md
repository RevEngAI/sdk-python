# AcceptTypeSuggestionsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | Keys of the suggestions to store, as the type suggestions endpoint returns them. A key repeated in one request is stored once. | 

## Example

```python
from revengai.models.accept_type_suggestions_input_body import AcceptTypeSuggestionsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptTypeSuggestionsInputBody from a JSON string
accept_type_suggestions_input_body_instance = AcceptTypeSuggestionsInputBody.from_json(json)
# print the JSON string representation of the object
print(AcceptTypeSuggestionsInputBody.to_json())

# convert the object into a dict
accept_type_suggestions_input_body_dict = accept_type_suggestions_input_body_instance.to_dict()
# create an instance of AcceptTypeSuggestionsInputBody from a dict
accept_type_suggestions_input_body_from_dict = AcceptTypeSuggestionsInputBody.from_dict(accept_type_suggestions_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


