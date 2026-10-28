# WorkflowDayBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyse_capabilities** | [**AgentCompletedBody**](AgentCompletedBody.md) | ANALYSE_CAPABILITIES agent-task stats for the day | 
**cryptography_binary** | [**AgentCompletedBody**](AgentCompletedBody.md) | CRYPTOGRAPHY_BINARY agent-task stats for the day | 
**var_date** | **str** | Day this entry covers | 
**protocols** | [**AgentCompletedBody**](AgentCompletedBody.md) | PROTOCOLS agent-task stats for the day | 
**remediation** | [**AgentCompletedBody**](AgentCompletedBody.md) | REMEDIATION agent-task stats for the day | 
**report_analysis** | [**ReportAnalysisBody**](ReportAnalysisBody.md) | REPORT_ANALYSIS agent-task stats for the day | 
**secrets** | [**AgentCompletedBody**](AgentCompletedBody.md) | SECRETS agent-task stats for the day | 
**triage** | [**AgentCompletedBody**](AgentCompletedBody.md) | TRIAGE agent-task stats for the day | 

## Example

```python
from revengai.models.workflow_day_body import WorkflowDayBody

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDayBody from a JSON string
workflow_day_body_instance = WorkflowDayBody.from_json(json)
# print the JSON string representation of the object
print(WorkflowDayBody.to_json())

# convert the object into a dict
workflow_day_body_dict = workflow_day_body_instance.to_dict()
# create an instance of WorkflowDayBody from a dict
workflow_day_body_from_dict = WorkflowDayBody.from_dict(workflow_day_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


