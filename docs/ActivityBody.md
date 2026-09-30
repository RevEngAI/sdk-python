# ActivityBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **str** | The kind of action taken | 
**activity_scope** | **str** | Who can see this activity entry | 
**created_at** | **datetime** | When the action happened | 
**message** | **str** | Human-readable description of the action | 
**sources** | **str** | The resource kind the action applied to | 
**username** | **str** | The user who performed the action | 

## Example

```python
from revengai.models.activity_body import ActivityBody

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityBody from a JSON string
activity_body_instance = ActivityBody.from_json(json)
# print the JSON string representation of the object
print(ActivityBody.to_json())

# convert the object into a dict
activity_body_dict = activity_body_instance.to_dict()
# create an instance of ActivityBody from a dict
activity_body_from_dict = ActivityBody.from_dict(activity_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


