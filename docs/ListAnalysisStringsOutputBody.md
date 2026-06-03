# ListAnalysisStringsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strings** | [**List[AnalysisStringItem]**](AnalysisStringItem.md) |  | 
**total_strings** | **int** |  | 

## Example

```python
from revengai.models.list_analysis_strings_output_body import ListAnalysisStringsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnalysisStringsOutputBody from a JSON string
list_analysis_strings_output_body_instance = ListAnalysisStringsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAnalysisStringsOutputBody.to_json())

# convert the object into a dict
list_analysis_strings_output_body_dict = list_analysis_strings_output_body_instance.to_dict()
# create an instance of ListAnalysisStringsOutputBody from a dict
list_analysis_strings_output_body_from_dict = ListAnalysisStringsOutputBody.from_dict(list_analysis_strings_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


