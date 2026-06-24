# ListAnalysisFunctionsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[AnalysisFunctionEntry]**](AnalysisFunctionEntry.md) |  | 
**total_count** | **int** | Total functions in the analysis, ignoring pagination. | 

## Example

```python
from revengai.models.list_analysis_functions_output_body import ListAnalysisFunctionsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnalysisFunctionsOutputBody from a JSON string
list_analysis_functions_output_body_instance = ListAnalysisFunctionsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAnalysisFunctionsOutputBody.to_json())

# convert the object into a dict
list_analysis_functions_output_body_dict = list_analysis_functions_output_body_instance.to_dict()
# create an instance of ListAnalysisFunctionsOutputBody from a dict
list_analysis_functions_output_body_from_dict = ListAnalysisFunctionsOutputBody.from_dict(list_analysis_functions_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


