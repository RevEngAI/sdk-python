# SubmitFeedbackInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment** | **str** | How useful the caller found this agent&#39;s output | 

## Example

```python
from revengai.models.submit_feedback_input_body import SubmitFeedbackInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFeedbackInputBody from a JSON string
submit_feedback_input_body_instance = SubmitFeedbackInputBody.from_json(json)
# print the JSON string representation of the object
print(SubmitFeedbackInputBody.to_json())

# convert the object into a dict
submit_feedback_input_body_dict = submit_feedback_input_body_instance.to_dict()
# create an instance of SubmitFeedbackInputBody from a dict
submit_feedback_input_body_from_dict = SubmitFeedbackInputBody.from_dict(submit_feedback_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


