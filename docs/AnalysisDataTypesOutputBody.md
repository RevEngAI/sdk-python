# AnalysisDataTypesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**List[DataTypeEntry]**](DataTypeEntry.md) | The stored types, ordered by data_type_id. | 

## Example

```python
from revengai.models.analysis_data_types_output_body import AnalysisDataTypesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisDataTypesOutputBody from a JSON string
analysis_data_types_output_body_instance = AnalysisDataTypesOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisDataTypesOutputBody.to_json())

# convert the object into a dict
analysis_data_types_output_body_dict = analysis_data_types_output_body_instance.to_dict()
# create an instance of AnalysisDataTypesOutputBody from a dict
analysis_data_types_output_body_from_dict = AnalysisDataTypesOutputBody.from_dict(analysis_data_types_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


