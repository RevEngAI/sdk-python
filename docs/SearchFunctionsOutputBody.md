# SearchFunctionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**page_number** | **int** |  | 
**page_size** | **int** |  | 
**results** | [**List[FunctionSearchResultBody]**](FunctionSearchResultBody.md) |  | 

## Example

```python
from revengai.models.search_functions_output_body import SearchFunctionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFunctionsOutputBody from a JSON string
search_functions_output_body_instance = SearchFunctionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(SearchFunctionsOutputBody.to_json())

# convert the object into a dict
search_functions_output_body_dict = search_functions_output_body_instance.to_dict()
# create an instance of SearchFunctionsOutputBody from a dict
search_functions_output_body_from_dict = SearchFunctionsOutputBody.from_dict(search_functions_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


