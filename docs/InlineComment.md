# InlineComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | 
**line** | **int** |  | 

## Example

```python
from revengai.models.inline_comment import InlineComment

# TODO update the JSON string below
json = "{}"
# create an instance of InlineComment from a JSON string
inline_comment_instance = InlineComment.from_json(json)
# print the JSON string representation of the object
print(InlineComment.to_json())

# convert the object into a dict
inline_comment_dict = inline_comment_instance.to_dict()
# create an instance of InlineComment from a dict
inline_comment_from_dict = InlineComment.from_dict(inline_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


