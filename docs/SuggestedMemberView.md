# SuggestedMemberView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_offset** | **int** | Bit offset within the containing word for a bitfield member. | 
**byte_offset** | **int** | Offset within the type. Null when no placement could be established. | 
**byte_size** | **int** | Width of the access in bytes. | 
**confidence** | **str** | Where suggested_type came from. declared and inferred were observed; width knows only the access width; model is the language model&#39;s proposal. | 
**name** | **str** | Name the member renders as: a database or frozen name where one exists, else the suggested one. | 
**origin** | **str** | Which function revealed this member: self, caller:&lt;function_id&gt; or callee:&lt;function_id&gt;. | 
**packed** | **bool** | The member sits at an offset its own width does not divide. | 
**placement** | **str** | observed means the offset was read off an access; guessed means the model proposed it; unplaced means the member has no offset. | 
**suggested_type** | **str** | Type expression for the member. | 
**token** | **str** | Placeholder this member renders as in the tokenised source. Absent for a member no access in this function revealed. | [optional] 

## Example

```python
from revengai.models.suggested_member_view import SuggestedMemberView

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedMemberView from a JSON string
suggested_member_view_instance = SuggestedMemberView.from_json(json)
# print the JSON string representation of the object
print(SuggestedMemberView.to_json())

# convert the object into a dict
suggested_member_view_dict = suggested_member_view_instance.to_dict()
# create an instance of SuggestedMemberView from a dict
suggested_member_view_from_dict = SuggestedMemberView.from_dict(suggested_member_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


