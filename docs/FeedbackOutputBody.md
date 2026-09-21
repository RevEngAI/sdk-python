# FeedbackOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment** | **str** | The sentiment the caller recorded, or null when they have not left any | 

## Example

```python
from revengai.models.feedback_output_body import FeedbackOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackOutputBody from a JSON string
feedback_output_body_instance = FeedbackOutputBody.from_json(json)
# print the JSON string representation of the object
print(FeedbackOutputBody.to_json())

# convert the object into a dict
feedback_output_body_dict = feedback_output_body_instance.to_dict()
# create an instance of FeedbackOutputBody from a dict
feedback_output_body_from_dict = FeedbackOutputBody.from_dict(feedback_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


