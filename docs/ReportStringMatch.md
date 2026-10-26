# ReportStringMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**ReportSubject**](ReportSubject.md) | Where the string is located, absent when unknown. | [optional] 
**value** | **str** | The matched string. | 

## Example

```python
from revengai.models.report_string_match import ReportStringMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStringMatch from a JSON string
report_string_match_instance = ReportStringMatch.from_json(json)
# print the JSON string representation of the object
print(ReportStringMatch.to_json())

# convert the object into a dict
report_string_match_dict = report_string_match_instance.to_dict()
# create an instance of ReportStringMatch from a dict
report_string_match_from_dict = ReportStringMatch.from_dict(report_string_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


