# CryptoScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the run was performed against | 
**findings** | [**List[CryptoFinding]**](CryptoFinding.md) | Functions with crypto-related evidence, sorted by confidence then evidence count | [optional] 
**total_functions** | **int** | Functions the run considered | 

## Example

```python
from revengai.models.crypto_scan_result import CryptoScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoScanResult from a JSON string
crypto_scan_result_instance = CryptoScanResult.from_json(json)
# print the JSON string representation of the object
print(CryptoScanResult.to_json())

# convert the object into a dict
crypto_scan_result_dict = crypto_scan_result_instance.to_dict()
# create an instance of CryptoScanResult from a dict
crypto_scan_result_from_dict = CryptoScanResult.from_dict(crypto_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


