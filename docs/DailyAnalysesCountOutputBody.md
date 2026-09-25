# DailyAnalysesCountOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_counts** | [**List[DailyCountBody]**](DailyCountBody.md) | One entry per day of the last 31 days, oldest first | 

## Example

```python
from revengai.models.daily_analyses_count_output_body import DailyAnalysesCountOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of DailyAnalysesCountOutputBody from a JSON string
daily_analyses_count_output_body_instance = DailyAnalysesCountOutputBody.from_json(json)
# print the JSON string representation of the object
print(DailyAnalysesCountOutputBody.to_json())

# convert the object into a dict
daily_analyses_count_output_body_dict = daily_analyses_count_output_body_instance.to_dict()
# create an instance of DailyAnalysesCountOutputBody from a dict
daily_analyses_count_output_body_from_dict = DailyAnalysesCountOutputBody.from_dict(daily_analyses_count_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


