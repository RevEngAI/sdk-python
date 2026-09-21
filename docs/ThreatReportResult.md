# ThreatReportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iocs** | [**List[IOC]**](IOC.md) | Indicators of compromise found. An indicator whose source does not resolve to a function is still listed, without function details. | 
**attack_flow_summary** | **str** | Markdown summary of the attack flow | 
**executable_techniques** | [**List[Technique]**](Technique.md) | MITRE ATT&amp;CK techniques found. A technique is listed only when both its function and its ATT&amp;CK catalogue entry resolve. | 
**number_of_analysed_functions** | **int** | Functions the agent analysed | 
**software_type** | **str** | Classification of the binary | 
**summary** | **str** | Summary of the analysis findings | 
**total_number_of_functions** | **int** | Functions identified in the binary | 
**yara_rule** | **str** | YARA rule generated for the binary | 

## Example

```python
from revengai.models.threat_report_result import ThreatReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatReportResult from a JSON string
threat_report_result_instance = ThreatReportResult.from_json(json)
# print the JSON string representation of the object
print(ThreatReportResult.to_json())

# convert the object into a dict
threat_report_result_dict = threat_report_result_instance.to_dict()
# create an instance of ThreatReportResult from a dict
threat_report_result_from_dict = ThreatReportResult.from_dict(threat_report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


