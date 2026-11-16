# RecordedFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | The context recorded with the feedback, or null when there is none | 
**sentiment** | **str** | The sentiment the caller recorded, or null when they have not left any | 

## Example

```python
from revengai.models.recorded_feedback import RecordedFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of RecordedFeedback from a JSON string
recorded_feedback_instance = RecordedFeedback.from_json(json)
# print the JSON string representation of the object
print(RecordedFeedback.to_json())

# convert the object into a dict
recorded_feedback_dict = recorded_feedback_instance.to_dict()
# create an instance of RecordedFeedback from a dict
recorded_feedback_from_dict = RecordedFeedback.from_dict(recorded_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


