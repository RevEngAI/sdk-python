# UpdateAnalysisInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_scope** | **str** | The analysis&#39; visibility. Changing to a non-PUBLIC scope requires a subscription tier that supports private analyses | [optional] 
**binary_name** | **str** | Renames the analysis&#39; binary. Empty or whitespace-only is rejected | [optional] 

## Example

```python
from revengai.models.update_analysis_input_body import UpdateAnalysisInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnalysisInputBody from a JSON string
update_analysis_input_body_instance = UpdateAnalysisInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateAnalysisInputBody.to_json())

# convert the object into a dict
update_analysis_input_body_dict = update_analysis_input_body_instance.to_dict()
# create an instance of UpdateAnalysisInputBody from a dict
update_analysis_input_body_from_dict = UpdateAnalysisInputBody.from_dict(update_analysis_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


