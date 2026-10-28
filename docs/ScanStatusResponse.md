# ScanStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**dataset** | **str** |  | 
**error** | **str** |  | [optional] 
**files_scanned** | **int** |  | 
**files_total** | **int** |  | 
**matches_found** | **int** |  | 
**progress** | [**WorkflowProgress**](WorkflowProgress.md) | Live workflow progress for a running async scan | [optional] 
**run_mode** | **str** |  | 
**scan_id** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from revengai.models.scan_status_response import ScanStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScanStatusResponse from a JSON string
scan_status_response_instance = ScanStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ScanStatusResponse.to_json())

# convert the object into a dict
scan_status_response_dict = scan_status_response_instance.to_dict()
# create an instance of ScanStatusResponse from a dict
scan_status_response_from_dict = ScanStatusResponse.from_dict(scan_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


