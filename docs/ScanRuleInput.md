# ScanRuleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **int** | Library rule id to reference instead of inline source | [optional] 
**source** | **str** | Inline rule source | [optional] 
**version** | **int** | Library rule version; 0 &#x3D; current | [optional] 

## Example

```python
from revengai.models.scan_rule_input import ScanRuleInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScanRuleInput from a JSON string
scan_rule_input_instance = ScanRuleInput.from_json(json)
# print the JSON string representation of the object
print(ScanRuleInput.to_json())

# convert the object into a dict
scan_rule_input_dict = scan_rule_input_instance.to_dict()
# create an instance of ScanRuleInput from a dict
scan_rule_input_from_dict = ScanRuleInput.from_dict(scan_rule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


