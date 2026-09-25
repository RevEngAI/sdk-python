# AcceptTypeSuggestionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | [**List[AcceptedType]**](AcceptedType.md) | One entry per requested suggestion, in request order. | 
**data_types** | [**List[DataTypeEntry]**](DataTypeEntry.md) | The type each requested suggestion resolved to, plus every type minted to satisfy one, ordered by data_type_id. | 

## Example

```python
from revengai.models.accept_type_suggestions_output_body import AcceptTypeSuggestionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptTypeSuggestionsOutputBody from a JSON string
accept_type_suggestions_output_body_instance = AcceptTypeSuggestionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(AcceptTypeSuggestionsOutputBody.to_json())

# convert the object into a dict
accept_type_suggestions_output_body_dict = accept_type_suggestions_output_body_instance.to_dict()
# create an instance of AcceptTypeSuggestionsOutputBody from a dict
accept_type_suggestions_output_body_from_dict = AcceptTypeSuggestionsOutputBody.from_dict(accept_type_suggestions_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


