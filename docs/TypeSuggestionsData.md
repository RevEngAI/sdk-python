# TypeSuggestionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Language model that produced the suggestions. | [optional] 
**status** | **str** | Status of the AI decompilation run that would have produced these suggestions. | 
**types** | [**List[SuggestedTypeView]**](SuggestedTypeView.md) | One entry per suggested type. Empty for a run that produced none, and for a run that predates type suggestion — the two are not distinguished. | 

## Example

```python
from revengai.models.type_suggestions_data import TypeSuggestionsData

# TODO update the JSON string below
json = "{}"
# create an instance of TypeSuggestionsData from a JSON string
type_suggestions_data_instance = TypeSuggestionsData.from_json(json)
# print the JSON string representation of the object
print(TypeSuggestionsData.to_json())

# convert the object into a dict
type_suggestions_data_dict = type_suggestions_data_instance.to_dict()
# create an instance of TypeSuggestionsData from a dict
type_suggestions_data_from_dict = TypeSuggestionsData.from_dict(type_suggestions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


