# HistoryActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The user who made the change. | 
**username** | **str** | Absent when the user no longer exists. | [optional] 

## Example

```python
from revengai.models.history_actor import HistoryActor

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryActor from a JSON string
history_actor_instance = HistoryActor.from_json(json)
# print the JSON string representation of the object
print(HistoryActor.to_json())

# convert the object into a dict
history_actor_dict = history_actor_instance.to_dict()
# create an instance of HistoryActor from a dict
history_actor_from_dict = HistoryActor.from_dict(history_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


