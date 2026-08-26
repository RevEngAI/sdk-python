# SecurityScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the run was performed against | 
**cancelled** | **bool** | Whether the run was cancelled before it covered every function | 
**decompiled** | **int** | Functions successfully decompiled and scanned | 
**failed** | **int** | Functions whose decompilation or scan attempt errored | 
**security_scan** | **Dict[str, object]** | Raw semgrep findings, keyed by the scanner&#39;s own result shape | [optional] 
**source** | **str** | Decompiler that produced the source scanned | 
**total** | **int** | Functions the run considered | 

## Example

```python
from revengai.models.security_scan_result import SecurityScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityScanResult from a JSON string
security_scan_result_instance = SecurityScanResult.from_json(json)
# print the JSON string representation of the object
print(SecurityScanResult.to_json())

# convert the object into a dict
security_scan_result_dict = security_scan_result_instance.to_dict()
# create an instance of SecurityScanResult from a dict
security_scan_result_from_dict = SecurityScanResult.from_dict(security_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


