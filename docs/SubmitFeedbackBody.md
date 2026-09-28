# SubmitFeedbackBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_route** | **str** | The route the caller was on when they submitted feedback | 
**feedback** | **str** | The feedback text | 
**screen_capture_url** | **str** | Optional URL to a screen capture related to the feedback | [optional] 

## Example

```python
from revengai.models.submit_feedback_body import SubmitFeedbackBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFeedbackBody from a JSON string
submit_feedback_body_instance = SubmitFeedbackBody.from_json(json)
# print the JSON string representation of the object
print(SubmitFeedbackBody.to_json())

# convert the object into a dict
submit_feedback_body_dict = submit_feedback_body_instance.to_dict()
# create an instance of SubmitFeedbackBody from a dict
submit_feedback_body_from_dict = SubmitFeedbackBody.from_dict(submit_feedback_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


