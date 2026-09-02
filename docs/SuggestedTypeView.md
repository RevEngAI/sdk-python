# SuggestedTypeView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | Existing data type the members were accessed through. Null when nothing resolved to a row; never minted for a suggestion. | [optional] 
**holes** | [**List[SuggestedHole]**](SuggestedHole.md) | Gaps between consecutive placed members, in offset order. | 
**implied_size** | **int** | Highest byte_offset+byte_size across the members. A lower bound on the type&#39;s size, not its size. | [optional] 
**key** | **str** | Identity of the suggestion: index:&lt;data_type_id&gt; where the access named a row, else token:&lt;type_token&gt;. | 
**members** | [**List[SuggestedMemberView]**](SuggestedMemberView.md) | Members in offset order, unplaced ones last. | 
**name** | **str** | Name the type renders as: a database or frozen name where one exists, else the suggested one. | 
**type_token** | **str** | Placeholder the type renders as, when it appears in this function&#39;s source. | [optional] 
**underlying_type** | **str** | Set only for a type with no observed members, where the suggestion is a name and a scalar type rather than a layout. | [optional] 

## Example

```python
from revengai.models.suggested_type_view import SuggestedTypeView

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedTypeView from a JSON string
suggested_type_view_instance = SuggestedTypeView.from_json(json)
# print the JSON string representation of the object
print(SuggestedTypeView.to_json())

# convert the object into a dict
suggested_type_view_dict = suggested_type_view_instance.to_dict()
# create an instance of SuggestedTypeView from a dict
suggested_type_view_from_dict = SuggestedTypeView.from_dict(suggested_type_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


