# AnalysisDataTypesGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | 
**items** | [**List[DataTypeEntry]**](DataTypeEntry.md) | The analysis&#39;s types the returned signatures name, ordered by data_type_id. | 

## Example

```python
from revengai.models.analysis_data_types_group import AnalysisDataTypesGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisDataTypesGroup from a JSON string
analysis_data_types_group_instance = AnalysisDataTypesGroup.from_json(json)
# print the JSON string representation of the object
print(AnalysisDataTypesGroup.to_json())

# convert the object into a dict
analysis_data_types_group_dict = analysis_data_types_group_instance.to_dict()
# create an instance of AnalysisDataTypesGroup from a dict
analysis_data_types_group_from_dict = AnalysisDataTypesGroup.from_dict(analysis_data_types_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


