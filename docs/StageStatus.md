# StageStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | [**AnalysisStage**](AnalysisStage.md) |  | 
**status** | [**PipelineStageStatus**](PipelineStageStatus.md) |  | 
**num_ahead** | **int** |  | 

## Example

```python
from revengai.models.stage_status import StageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StageStatus from a JSON string
stage_status_instance = StageStatus.from_json(json)
# print the JSON string representation of the object
print(StageStatus.to_json())

# convert the object into a dict
stage_status_dict = stage_status_instance.to_dict()
# create an instance of StageStatus from a dict
stage_status_from_dict = StageStatus.from_dict(stage_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


