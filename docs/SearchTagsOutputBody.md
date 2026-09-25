# SearchTagsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**page_number** | **int** |  | 
**page_size** | **int** |  | 
**results** | [**List[TagSearchResultBody]**](TagSearchResultBody.md) |  | 

## Example

```python
from revengai.models.search_tags_output_body import SearchTagsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTagsOutputBody from a JSON string
search_tags_output_body_instance = SearchTagsOutputBody.from_json(json)
# print the JSON string representation of the object
print(SearchTagsOutputBody.to_json())

# convert the object into a dict
search_tags_output_body_dict = search_tags_output_body_instance.to_dict()
# create an instance of SearchTagsOutputBody from a dict
search_tags_output_body_from_dict = SearchTagsOutputBody.from_dict(search_tags_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


