# ScanSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**dataset** | **str** |  | 
**error** | **str** |  | [optional] 
**files_scanned** | **int** |  | 
**files_total** | **int** |  | 
**finished_at** | **datetime** |  | [optional] 
**matches_found** | **int** |  | 
**run_mode** | **str** |  | 
**scan_id** | **int** |  | 
**started_at** | **datetime** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from revengai.models.scan_summary import ScanSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ScanSummary from a JSON string
scan_summary_instance = ScanSummary.from_json(json)
# print the JSON string representation of the object
print(ScanSummary.to_json())

# convert the object into a dict
scan_summary_dict = scan_summary_instance.to_dict()
# create an instance of ScanSummary from a dict
scan_summary_from_dict = ScanSummary.from_dict(scan_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


