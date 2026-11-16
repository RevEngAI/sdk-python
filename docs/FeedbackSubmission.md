# FeedbackSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | Context the client captured with the feedback, stored as-is (e.g. the binary hash and the matches the caller was shown) | [optional] 
**sentiment** | **str** | How useful the caller found the result | 

## Example

```python
from revengai.models.feedback_submission import FeedbackSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackSubmission from a JSON string
feedback_submission_instance = FeedbackSubmission.from_json(json)
# print the JSON string representation of the object
print(FeedbackSubmission.to_json())

# convert the object into a dict
feedback_submission_dict = feedback_submission_instance.to_dict()
# create an instance of FeedbackSubmission from a dict
feedback_submission_from_dict = FeedbackSubmission.from_dict(feedback_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


