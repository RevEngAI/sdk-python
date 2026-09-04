# UpgradeAnalysisModelOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | ID of the re-queued analysis. Unchanged — the upgrade moves the existing analysis rather than creating a new one. | 
**binary_id** | **int** | ID of the binary the analysis belongs to | 
**model_id** | **int** | Model the analysis is now queued against | 

## Example

```python
from revengai.models.upgrade_analysis_model_output_body import UpgradeAnalysisModelOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeAnalysisModelOutputBody from a JSON string
upgrade_analysis_model_output_body_instance = UpgradeAnalysisModelOutputBody.from_json(json)
# print the JSON string representation of the object
print(UpgradeAnalysisModelOutputBody.to_json())

# convert the object into a dict
upgrade_analysis_model_output_body_dict = upgrade_analysis_model_output_body_instance.to_dict()
# create an instance of UpgradeAnalysisModelOutputBody from a dict
upgrade_analysis_model_output_body_from_dict = UpgradeAnalysisModelOutputBody.from_dict(upgrade_analysis_model_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


