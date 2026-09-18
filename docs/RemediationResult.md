# RemediationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snort_rules** | **List[str]** | Generated Snort rules | 
**stix_rules** | **List[str]** | Generated STIX rules | 
**yara_rules** | **List[str]** | Generated YARA rules | 

## Example

```python
from revengai.models.remediation_result import RemediationResult

# TODO update the JSON string below
json = "{}"
# create an instance of RemediationResult from a JSON string
remediation_result_instance = RemediationResult.from_json(json)
# print the JSON string representation of the object
print(RemediationResult.to_json())

# convert the object into a dict
remediation_result_dict = remediation_result_instance.to_dict()
# create an instance of RemediationResult from a dict
remediation_result_from_dict = RemediationResult.from_dict(remediation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


