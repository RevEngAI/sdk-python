# CryptoFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Function&#39;s virtual address, hex-encoded | 
**categories** | **List[str]** | Distinct crypto categories evidenced by this function | 
**confidence** | **str** | High when a direct name match was found, medium when the function only calls into crypto APIs | 
**crypto_calls** | [**List[CryptoCall]**](CryptoCall.md) | Matches against names this function calls | [optional] 
**direct_matches** | [**List[CryptoDirectMatch]**](CryptoDirectMatch.md) | Matches against the function&#39;s own name | [optional] 
**evidence_count** | **int** | Total number of direct matches and crypto calls | 
**function_id** | **int** | ID of the function the finding was reported in | 
**function_name** | **str** | Name of the function the finding was reported in | 
**function_size** | **int** | Size of the function in bytes | 
**libraries** | **List[str]** | Distinct crypto libraries evidenced by this function | 

## Example

```python
from revengai.models.crypto_finding import CryptoFinding

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoFinding from a JSON string
crypto_finding_instance = CryptoFinding.from_json(json)
# print the JSON string representation of the object
print(CryptoFinding.to_json())

# convert the object into a dict
crypto_finding_dict = crypto_finding_instance.to_dict()
# create an instance of CryptoFinding from a dict
crypto_finding_from_dict = CryptoFinding.from_dict(crypto_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


