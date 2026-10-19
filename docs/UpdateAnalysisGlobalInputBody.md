# UpdateAnalysisGlobalInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **int** | Analysis data type to assign. Omit to leave the type as it is. | [optional] 
**name** | **str** | New name for the global. Omit to leave the name as it is. | [optional] 

## Example

```python
from revengai.models.update_analysis_global_input_body import UpdateAnalysisGlobalInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnalysisGlobalInputBody from a JSON string
update_analysis_global_input_body_instance = UpdateAnalysisGlobalInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateAnalysisGlobalInputBody.to_json())

# convert the object into a dict
update_analysis_global_input_body_dict = update_analysis_global_input_body_instance.to_dict()
# create an instance of UpdateAnalysisGlobalInputBody from a dict
update_analysis_global_input_body_from_dict = UpdateAnalysisGlobalInputBody.from_dict(update_analysis_global_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


