# UpdateAnalysisDataTypesInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**List[UpdateDataTypeEntry]**](UpdateDataTypeEntry.md) | The replacements. Every data_type_id must belong to the analysis, and none may repeat. | 

## Example

```python
from revengai.models.update_analysis_data_types_input_body import UpdateAnalysisDataTypesInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnalysisDataTypesInputBody from a JSON string
update_analysis_data_types_input_body_instance = UpdateAnalysisDataTypesInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateAnalysisDataTypesInputBody.to_json())

# convert the object into a dict
update_analysis_data_types_input_body_dict = update_analysis_data_types_input_body_instance.to_dict()
# create an instance of UpdateAnalysisDataTypesInputBody from a dict
update_analysis_data_types_input_body_from_dict = UpdateAnalysisDataTypesInputBody.from_dict(update_analysis_data_types_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


