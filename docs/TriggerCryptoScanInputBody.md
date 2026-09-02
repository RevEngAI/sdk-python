# TriggerCryptoScanInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Restrict findings to these categories. Omit to scan every category. | [optional] 
**direct_only** | **bool** | Only report functions whose own name matches a known crypto API; skips the calls-into-crypto pass, avoiding a bulk call-graph fetch. | [optional] 
**libraries** | **List[str]** | Restrict findings to these libraries. Omit to scan every library. | [optional] 

## Example

```python
from revengai.models.trigger_crypto_scan_input_body import TriggerCryptoScanInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerCryptoScanInputBody from a JSON string
trigger_crypto_scan_input_body_instance = TriggerCryptoScanInputBody.from_json(json)
# print the JSON string representation of the object
print(TriggerCryptoScanInputBody.to_json())

# convert the object into a dict
trigger_crypto_scan_input_body_dict = trigger_crypto_scan_input_body_instance.to_dict()
# create an instance of TriggerCryptoScanInputBody from a dict
trigger_crypto_scan_input_body_from_dict = TriggerCryptoScanInputBody.from_dict(trigger_crypto_scan_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


