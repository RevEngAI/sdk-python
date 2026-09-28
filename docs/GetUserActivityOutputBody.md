# GetUserActivityOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**List[ActivityBody]**](ActivityBody.md) | Recent activity visible to the caller: their own private activity, their team&#39;s, and everyone&#39;s public activity | 

## Example

```python
from revengai.models.get_user_activity_output_body import GetUserActivityOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserActivityOutputBody from a JSON string
get_user_activity_output_body_instance = GetUserActivityOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetUserActivityOutputBody.to_json())

# convert the object into a dict
get_user_activity_output_body_dict = get_user_activity_output_body_instance.to_dict()
# create an instance of GetUserActivityOutputBody from a dict
get_user_activity_output_body_from_dict = GetUserActivityOutputBody.from_dict(get_user_activity_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


