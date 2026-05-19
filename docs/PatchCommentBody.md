# PatchCommentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment text | 
**line** | **int** | Line number to set the comment on | 

## Example

```python
from revengai.models.patch_comment_body import PatchCommentBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCommentBody from a JSON string
patch_comment_body_instance = PatchCommentBody.from_json(json)
# print the JSON string representation of the object
print(PatchCommentBody.to_json())

# convert the object into a dict
patch_comment_body_dict = patch_comment_body_instance.to_dict()
# create an instance of PatchCommentBody from a dict
patch_comment_body_from_dict = PatchCommentBody.from_dict(patch_comment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


