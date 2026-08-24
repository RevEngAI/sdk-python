# CreateAnalysisDataTypesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**List[CreateDataTypeEntry]**](CreateDataTypeEntry.md) | The types to create. Each namespace, name and kind must be new to the analysis. | 

## Example

```python
from revengai.models.create_analysis_data_types_input_body import CreateAnalysisDataTypesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnalysisDataTypesInputBody from a JSON string
create_analysis_data_types_input_body_instance = CreateAnalysisDataTypesInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateAnalysisDataTypesInputBody.to_json())

# convert the object into a dict
create_analysis_data_types_input_body_dict = create_analysis_data_types_input_body_instance.to_dict()
# create an instance of CreateAnalysisDataTypesInputBody from a dict
create_analysis_data_types_input_body_from_dict = CreateAnalysisDataTypesInputBody.from_dict(create_analysis_data_types_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


