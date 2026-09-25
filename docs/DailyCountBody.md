# DailyCountBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Analyses the user created that day | 
**day** | **datetime** | Day this count covers, at midnight UTC | 

## Example

```python
from revengai.models.daily_count_body import DailyCountBody

# TODO update the JSON string below
json = "{}"
# create an instance of DailyCountBody from a JSON string
daily_count_body_instance = DailyCountBody.from_json(json)
# print the JSON string representation of the object
print(DailyCountBody.to_json())

# convert the object into a dict
daily_count_body_dict = daily_count_body_instance.to_dict()
# create an instance of DailyCountBody from a dict
daily_count_body_from_dict = DailyCountBody.from_dict(daily_count_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


