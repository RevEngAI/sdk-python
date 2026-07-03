# AnalysisBasicInfoOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_scope** | **str** | PUBLIC, PRIVATE, or TEAM | 
**base_address** | **int** | Base address of the binary, null when unknown | 
**binary_id** | **int** | Binary ID | 
**binary_name** | **str** | Binary filename | 
**binary_size** | **int** | Binary size in bytes | 
**binary_uuid** | **str** | UUID of the binary, omitted when not set | 
**creation** | **datetime** | When the binary was uploaded | 
**debug** | **bool** | True when the binary was analysed with debug symbols | 
**function_count** | **int** | Number of functions in the binary | 
**is_advanced** | **bool** | True when the analysis was run in advanced mode | 
**is_owner** | **bool** | True when the caller is the analysis owner | 
**is_system** | **bool** | True when the analysis is owned by a system user | 
**model_id** | **int** | Model ID | 
**model_name** | **str** | Model used for analysis | 
**owner_username** | **str** | Username of the analysis owner | 
**sequencer_version** | **str** | Sequencer version, omitted when not set | [optional] 
**sha_256_hash** | **str** | SHA-256 hash of the binary | 
**team_id** | **int** | Team ID of the analysis | 

## Example

```python
from revengai.models.analysis_basic_info_output_body import AnalysisBasicInfoOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisBasicInfoOutputBody from a JSON string
analysis_basic_info_output_body_instance = AnalysisBasicInfoOutputBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisBasicInfoOutputBody.to_json())

# convert the object into a dict
analysis_basic_info_output_body_dict = analysis_basic_info_output_body_instance.to_dict()
# create an instance of AnalysisBasicInfoOutputBody from a dict
analysis_basic_info_output_body_from_dict = AnalysisBasicInfoOutputBody.from_dict(analysis_basic_info_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


