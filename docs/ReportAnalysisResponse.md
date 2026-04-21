# ReportAnalysisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | A markdown summary of the report | 
**software_type** | **str** | The type of software being analyzed | 
**total_number_of_functions** | **int** | The total number of functions identified in the binary | 
**number_of_analysed_functions** | **int** | The number of functions that were analyzed in the binary | 
**attack_flow_summary** | **str** | A summary in markdown format of the attack flow | 
**iocs** | [**List[IOC]**](IOC.md) | A list of IOCs (Indicators of Compromise) found in the analysis | 
**executable_techniques** | [**List[MITRETechnique]**](MITRETechnique.md) | A series of MITRE Techniques found | 
**yara_rule** | **str** | The YARA rule generated for the binary | 

## Example

```python
from revengai.models.report_analysis_response import ReportAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAnalysisResponse from a JSON string
report_analysis_response_instance = ReportAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(ReportAnalysisResponse.to_json())

# convert the object into a dict
report_analysis_response_dict = report_analysis_response_instance.to_dict()
# create an instance of ReportAnalysisResponse from a dict
report_analysis_response_from_dict = ReportAnalysisResponse.from_dict(report_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


