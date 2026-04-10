# SubmitUserFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_route** | **str** | The route from where the feedback was submitted | 
**feedback** | **str** | The user&#39;s feedback | 
**screen_capture_url** | **str** |  | [optional] 

## Example

```python
from revengai.models.submit_user_feedback_request import SubmitUserFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitUserFeedbackRequest from a JSON string
submit_user_feedback_request_instance = SubmitUserFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitUserFeedbackRequest.to_json())

# convert the object into a dict
submit_user_feedback_request_dict = submit_user_feedback_request_instance.to_dict()
# create an instance of SubmitUserFeedbackRequest from a dict
submit_user_feedback_request_from_dict = SubmitUserFeedbackRequest.from_dict(submit_user_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


