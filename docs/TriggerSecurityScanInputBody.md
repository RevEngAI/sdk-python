# TriggerSecurityScanInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_functions_to_scan** | **int** | Stop after decompiling and scanning this many functions. Omit to process every function in the analysis. | [optional] 

## Example

```python
from revengai.models.trigger_security_scan_input_body import TriggerSecurityScanInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerSecurityScanInputBody from a JSON string
trigger_security_scan_input_body_instance = TriggerSecurityScanInputBody.from_json(json)
# print the JSON string representation of the object
print(TriggerSecurityScanInputBody.to_json())

# convert the object into a dict
trigger_security_scan_input_body_dict = trigger_security_scan_input_body_instance.to_dict()
# create an instance of TriggerSecurityScanInputBody from a dict
trigger_security_scan_input_body_from_dict = TriggerSecurityScanInputBody.from_dict(trigger_security_scan_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


