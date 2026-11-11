# ScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**files** | [**List[FileResult]**](FileResult.md) |  | 
**files_scanned** | **int** |  | 
**files_total** | **int** |  | 
**matches_found** | **int** |  | 
**scan_id** | **int** |  | [optional] 

## Example

```python
from revengai.models.scan_result import ScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResult from a JSON string
scan_result_instance = ScanResult.from_json(json)
# print the JSON string representation of the object
print(ScanResult.to_json())

# convert the object into a dict
scan_result_dict = scan_result_instance.to_dict()
# create an instance of ScanResult from a dict
scan_result_from_dict = ScanResult.from_dict(scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


