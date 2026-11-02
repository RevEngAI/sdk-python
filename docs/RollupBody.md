# RollupBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **List[int]** | Files added and findings recorded in each of the last 24 hours, oldest first. | 
**agent_status** | **str** | State of the agents as a whole: queued while every run is pending, running while any is pending or running, complete otherwise. Null when no agent has run. | 
**agents** | [**List[AgentBody]**](AgentBody.md) | Agents run on the investigation&#39;s files that you may see, each with its state across the files. Empty until an agent has run. | 
**file_count** | **int** | Files in the investigation that you are permitted to see. | 
**findings** | [**FindingCountsBody**](FindingCountsBody.md) |  | 
**findings_severity** | **str** | The highest severity among the findings, independent of the investigation&#39;s own severity. Null when there are no findings. | 
**first_file_name** | **str** | Name of the first file added that you are permitted to see. Null when there is none. | 
**last_activity_at** | **datetime** | The latest of an edit to the investigation, a file being added and a finding being recorded. | 

## Example

```python
from revengai.models.rollup_body import RollupBody

# TODO update the JSON string below
json = "{}"
# create an instance of RollupBody from a JSON string
rollup_body_instance = RollupBody.from_json(json)
# print the JSON string representation of the object
print(RollupBody.to_json())

# convert the object into a dict
rollup_body_dict = rollup_body_instance.to_dict()
# create an instance of RollupBody from a dict
rollup_body_from_dict = RollupBody.from_dict(rollup_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


