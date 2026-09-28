# SubmitFeedbackOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Confirmation message | 

## Example

```python
from revengai.models.submit_feedback_output_body import SubmitFeedbackOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFeedbackOutputBody from a JSON string
submit_feedback_output_body_instance = SubmitFeedbackOutputBody.from_json(json)
# print the JSON string representation of the object
print(SubmitFeedbackOutputBody.to_json())

# convert the object into a dict
submit_feedback_output_body_dict = submit_feedback_output_body_instance.to_dict()
# create an instance of SubmitFeedbackOutputBody from a dict
submit_feedback_output_body_from_dict = SubmitFeedbackOutputBody.from_dict(submit_feedback_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


