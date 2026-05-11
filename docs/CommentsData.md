# CommentsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**inline_comments** | [**List[InlineComment]**](InlineComment.md) | Structured inline comments with line numbers | 
**task_status** | **str** | Task status | 

## Example

```python
from revengai.models.comments_data import CommentsData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsData from a JSON string
comments_data_instance = CommentsData.from_json(json)
# print the JSON string representation of the object
print(CommentsData.to_json())

# convert the object into a dict
comments_data_dict = comments_data_instance.to_dict()
# create an instance of CommentsData from a dict
comments_data_from_dict = CommentsData.from_dict(comments_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


