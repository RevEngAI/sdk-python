# StatusBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Why the run failed. Only set when status is FAILED. | [optional] 
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this analysis. | 

## Example

```python
from revengai.models.status_body import StatusBody

# TODO update the JSON string below
json = "{}"
# create an instance of StatusBody from a JSON string
status_body_instance = StatusBody.from_json(json)
# print the JSON string representation of the object
print(StatusBody.to_json())

# convert the object into a dict
status_body_dict = status_body_instance.to_dict()
# create an instance of StatusBody from a dict
status_body_from_dict = StatusBody.from_dict(status_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


