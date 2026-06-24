# ListAnalysisFunctionsDataTypesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DataTypesEntry]**](DataTypesEntry.md) |  | 
**total_count** | **int** | Total functions in the analysis, ignoring pagination. | 

## Example

```python
from revengai.models.list_analysis_functions_data_types_output_body import ListAnalysisFunctionsDataTypesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnalysisFunctionsDataTypesOutputBody from a JSON string
list_analysis_functions_data_types_output_body_instance = ListAnalysisFunctionsDataTypesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAnalysisFunctionsDataTypesOutputBody.to_json())

# convert the object into a dict
list_analysis_functions_data_types_output_body_dict = list_analysis_functions_data_types_output_body_instance.to_dict()
# create an instance of ListAnalysisFunctionsDataTypesOutputBody from a dict
list_analysis_functions_data_types_output_body_from_dict = ListAnalysisFunctionsDataTypesOutputBody.from_dict(list_analysis_functions_data_types_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


