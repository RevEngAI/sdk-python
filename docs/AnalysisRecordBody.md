# AnalysisRecordBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis ID | 
**analysis_scope** | **str** | Scope of the analysis | 
**base_address** | **int** | Binary base address | 
**binary_id** | **int** | Binary ID | 
**binary_name** | **str** | Binary filename | 
**binary_size** | **int** | Binary size in bytes | 
**creation** | **datetime** | When the analysis was created | 
**function_boundaries_hash** | **str** | Hash of the binary&#39;s provided function boundaries | 
**is_owner** | **bool** | True when the caller owns the analysis | 
**model_id** | **int** | Model ID | 
**model_name** | **str** | Model name | 
**sha_256_hash** | **str** | SHA-256 hash of the binary | 
**status** | **str** | Analysis status | 
**tags** | [**List[AnalysisTagBody]**](AnalysisTagBody.md) | Tags associated with the binary | 
**username** | **str** | Username of the analysis owner | 

## Example

```python
from revengai.models.analysis_record_body import AnalysisRecordBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRecordBody from a JSON string
analysis_record_body_instance = AnalysisRecordBody.from_json(json)
# print the JSON string representation of the object
print(AnalysisRecordBody.to_json())

# convert the object into a dict
analysis_record_body_dict = analysis_record_body_instance.to_dict()
# create an instance of AnalysisRecordBody from a dict
analysis_record_body_from_dict = AnalysisRecordBody.from_dict(analysis_record_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


