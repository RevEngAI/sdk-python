# SearchBinariesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**page_number** | **int** |  | 
**page_size** | **int** |  | 
**results** | [**List[BinarySearchResultBody]**](BinarySearchResultBody.md) |  | 

## Example

```python
from revengai.models.search_binaries_output_body import SearchBinariesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBinariesOutputBody from a JSON string
search_binaries_output_body_instance = SearchBinariesOutputBody.from_json(json)
# print the JSON string representation of the object
print(SearchBinariesOutputBody.to_json())

# convert the object into a dict
search_binaries_output_body_dict = search_binaries_output_body_instance.to_dict()
# create an instance of SearchBinariesOutputBody from a dict
search_binaries_output_body_from_dict = SearchBinariesOutputBody.from_dict(search_binaries_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


