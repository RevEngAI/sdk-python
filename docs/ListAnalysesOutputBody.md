# ListAnalysesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Opaque cursor to fetch the next page; empty on the last page | [optional] 
**page_size** | **int** | Number of results in this page | 
**results** | [**List[AnalysisRecordBody]**](AnalysisRecordBody.md) | The page of matching analyses | 

## Example

```python
from revengai.models.list_analyses_output_body import ListAnalysesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnalysesOutputBody from a JSON string
list_analyses_output_body_instance = ListAnalysesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAnalysesOutputBody.to_json())

# convert the object into a dict
list_analyses_output_body_dict = list_analyses_output_body_instance.to_dict()
# create an instance of ListAnalysesOutputBody from a dict
list_analyses_output_body_from_dict = ListAnalysesOutputBody.from_dict(list_analyses_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


