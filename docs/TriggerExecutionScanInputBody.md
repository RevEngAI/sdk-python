# TriggerExecutionScanInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Restrict findings to these categories. Omit to scan the default executes-code set. | [optional] 
**direct_only** | **bool** | Only report functions whose own name matches a known execution API; skips the calls-into-execution pass, avoiding a bulk call-graph fetch. | [optional] 
**sources** | **List[str]** | Restrict findings to these sources. Omit to scan every source. | [optional] 

## Example

```python
from revengai.models.trigger_execution_scan_input_body import TriggerExecutionScanInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExecutionScanInputBody from a JSON string
trigger_execution_scan_input_body_instance = TriggerExecutionScanInputBody.from_json(json)
# print the JSON string representation of the object
print(TriggerExecutionScanInputBody.to_json())

# convert the object into a dict
trigger_execution_scan_input_body_dict = trigger_execution_scan_input_body_instance.to_dict()
# create an instance of TriggerExecutionScanInputBody from a dict
trigger_execution_scan_input_body_from_dict = TriggerExecutionScanInputBody.from_dict(trigger_execution_scan_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


