# VirusTotalScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha_256_hash** | **str** | Content hash the lookup was keyed by | 
**vt** | **object** |  | 
**vt_last_updated** | **datetime** | When this result was recorded | 

## Example

```python
from revengai.models.virus_total_scan_result import VirusTotalScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of VirusTotalScanResult from a JSON string
virus_total_scan_result_instance = VirusTotalScanResult.from_json(json)
# print the JSON string representation of the object
print(VirusTotalScanResult.to_json())

# convert the object into a dict
virus_total_scan_result_dict = virus_total_scan_result_instance.to_dict()
# create an instance of VirusTotalScanResult from a dict
virus_total_scan_result_from_dict = VirusTotalScanResult.from_dict(virus_total_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


