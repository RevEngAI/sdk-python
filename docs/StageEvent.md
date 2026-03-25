# StageEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | [**AnalysisStage**](AnalysisStage.md) |  | 
**status** | [**AnalysisStageStatus**](AnalysisStageStatus.md) |  | 
**timestamp** | **str** |  | 

## Example

```python
from revengai.models.stage_event import StageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StageEvent from a JSON string
stage_event_instance = StageEvent.from_json(json)
# print the JSON string representation of the object
print(StageEvent.to_json())

# convert the object into a dict
stage_event_dict = stage_event_instance.to_dict()
# create an instance of StageEvent from a dict
stage_event_from_dict = StageEvent.from_dict(stage_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


