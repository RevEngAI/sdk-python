# TagSearchResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | 
**tag_id** | **int** |  | 

## Example

```python
from revengai.models.tag_search_result_body import TagSearchResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of TagSearchResultBody from a JSON string
tag_search_result_body_instance = TagSearchResultBody.from_json(json)
# print the JSON string representation of the object
print(TagSearchResultBody.to_json())

# convert the object into a dict
tag_search_result_body_dict = tag_search_result_body_instance.to_dict()
# create an instance of TagSearchResultBody from a dict
tag_search_result_body_from_dict = TagSearchResultBody.from_dict(tag_search_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


