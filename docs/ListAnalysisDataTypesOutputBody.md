# ListAnalysisDataTypesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DataTypeEntry]**](DataTypeEntry.md) |  | 
**total_count** | **int** | Total types matching the filters, ignoring pagination. | 

## Example

```python
from revengai.models.list_analysis_data_types_output_body import ListAnalysisDataTypesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnalysisDataTypesOutputBody from a JSON string
list_analysis_data_types_output_body_instance = ListAnalysisDataTypesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAnalysisDataTypesOutputBody.to_json())

# convert the object into a dict
list_analysis_data_types_output_body_dict = list_analysis_data_types_output_body_instance.to_dict()
# create an instance of ListAnalysisDataTypesOutputBody from a dict
list_analysis_data_types_output_body_from_dict = ListAnalysisDataTypesOutputBody.from_dict(list_analysis_data_types_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


