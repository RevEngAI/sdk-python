# SummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**ai_summary** | **str** | Summary with code tags removed | 
**summary** | **str** | Raw summary from the model | 
**task_status** | **str** | Task status | 

## Example

```python
from revengai.models.summary_data import SummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryData from a JSON string
summary_data_instance = SummaryData.from_json(json)
# print the JSON string representation of the object
print(SummaryData.to_json())

# convert the object into a dict
summary_data_dict = summary_data_instance.to_dict()
# create an instance of SummaryData from a dict
summary_data_from_dict = SummaryData.from_dict(summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


